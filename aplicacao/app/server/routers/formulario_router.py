from fastapi import APIRouter, status, Body

from server.models.exception_schema import ExcecaoNegocio
from app.server.services.formulario_service import (
                                          listar_formularios,
                                          buscar_formulario,
                                          inserir_formulario
                                        )

from app.server.models.formulario_schema import (
                                        FormularioSchema,
                                        UpdateFormularioModel,
                                        CreateFormularioModel
                                        )
router = APIRouter(
    prefix="/api/v1/formularios",
    tags=["formularios"],
    responses={400:{"model":ExcecaoNegocio}}
)

@router.get("/", response_description="lista de formularios")
async def listar() -> list[FormularioSchema]:
    return await listar_formularios()

@router.get("/formulario", response_description="retorna dados de uma formulario")
async def formulario(formularioId: int = 0) -> FormularioSchema:
    return await buscar_formulario(formularioId)

@router.post("/cadastrar", response_description="cadastra novo ")
async def cadastrar(formulario: CreateFormularioModel = Body(...)) -> FormularioSchema:
    return await inserir_formulario(formulario)

