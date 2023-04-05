from server.database import getconection
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from server.models.exception_schema import excecaoNegocioResponse
from pycpfcnpj import cpfcnpj
from server.services.sequence import getNextSequence, retornarSequence
from datetime import datetime

colletion = 'formulario'

def formulario_helper(formulario) -> dict:
    return {
        "formularioId": formulario["formularioId"],
        "nome": formulario["nome"],
        "descricao": formulario["descricao"],
        "documentoFiscal": formulario["documentoFiscal"],
        "logo": formulario["logo"],
        "banner": formulario["banner"],
        "telefone": formulario["telefone"],
        "whatsapp": formulario["whatsapp"],
        "email": formulario["email"],
        "uf": formulario["uf"],
        "cidade": formulario["cidade"],
        "bairro": formulario["bairro"],
        "endereco": formulario["endereco"],
        "numero": formulario["numero"],
        "createdAt": formulario["createdAt"],
        "updatedAt": formulario["updatedAt"]
    }

async def listar_formularios():
    formularios_colletion = await getconection(colletion)
    formularios = []
    for formulario in formularios_colletion.find():
        formularios.append(formulario_helper(formulario))
    if not formularios:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=excecaoNegocioResponse(status.HTTP_400_BAD_REQUEST,'Lista vázia',''))
    return formularios

async def buscar_formulario(formularioId):
    formularios_colletion = await getconection(colletion)
    query = {"formularioId": formularioId}
    formulario = formularios_colletion.find_one(query)
    if not formulario:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=excecaoNegocioResponse(status.HTTP_400_BAD_REQUEST,'Loja não encontrada',''))
    return formulario_helper(formulario)

async def inserir_formulario(formulario):
    formulario = jsonable_encoder(formulario)
    try:
        formulario['formularioId'] = await getNextSequence('formularioId')
        formulario['createdAt'] = datetime.now()
        formulario['updatedAt'] = datetime.now()
        formularios_colletion = await getconection(colletion)
        formularios_colletion.insert_one(formulario_helper(formulario))
        return await buscar_formulario(formulario['formularioId'])
    except:
        await retornarSequence('formularioId')
        raise "Entre em contato com o administrador"
    
async def atualizar_formulario(formulario):
    formulario = jsonable_encoder(formulario)
    try:
        formulario['createdAt'] = buscar_formulario(formulario['formularioId'])['createdAt']
        formulario['updatedAt'] = datetime.now()
        formularios_colletion = await getconection(colletion)
        query = {'formularioId': formulario['formularioId']}
        return await formularios_colletion.find_one_and_update(query, formulario)
    except:
        raise "Entre em contato com o administrador"