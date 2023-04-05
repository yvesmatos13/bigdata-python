from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class FormularioSchema(BaseModel):
    formularioId: int
    nome: str
    descricao: str
    documentoFiscal: str = Field(unique=True)
    logo: str
    banner: str
    telefone: int
    whatsapp: int
    email: str
    uf:str
    cidade: str
    bairro: str
    endereco:str
    numero: str
    createdAt: datetime = datetime.now()
    updatedAt: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "formularioId":0,
                "nome": "string",
                "descricao": "string",
                "documentoFiscal": "string",
                "logo": "base64",
                "banner": "base64",
                "telefone": 0,
                "whatsapp": 0,
                "email": "string",
                "uf": "string",
                "cidade": "string",
                "bairro": "string",
                "endereco": "string",
                "createdAt": "2013-10-02T01:11:18.965Z",
                "updatedAt": "2013-10-02T01:11:18.965Z"
            }
        }

class CreateFormularioModel(BaseModel):
    nome: str
    descricao: str
    documentoFiscal: str = Field(unique=True)
    logo: str
    banner: str
    telefone: int
    whatsapp: int
    email: str
    uf:str
    cidade: str
    bairro: str
    endereco:str
    numero: str

    class Config:
        schema_extra = {
            "example": {
                "nome": "string",
                "descricao": "string",
                "documentoFiscal": "string",
                "logo": "base64",
                "banner": "base64",
                "telefone": 0,
                "whatsapp": 0,
                "email": "string",
                "uf": "string",
                "cidade": "string",
                "bairro": "string",
                "endereco": "string",
                "numero":"string"
            }
        }

class UpdateFormularioModel(BaseModel):
    formularioId: Optional[int]
    nome: Optional[str]
    descricao: Optional[str]
    documentoFiscal: Optional[str]
    logo: Optional[str]
    banner: Optional[str]
    telefone: Optional[int]
    whatsapp: Optional[int]
    email: Optional[str]
    uf: Optional[str]
    cidade: Optional[str]
    bairro: Optional[str]
    endereco: Optional[str]
    numero: Optional[str]
    updatedAt: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "formularioId":0,
                "descricao": "string",
                "documentoFiscal": "string",
                "nome": "string",
                "logo": "base64",
                "banner": "base64",
                "telefone": 0,
                "whatsapp": 0,
                "email": "string",
                "uf": "string",
                "cidade": "string",
                "bairro": "string",
                "endereco": "string",
                "numero": "string",
                "createdAt": "2013-10-02T01:11:18.965Z",
                "updatedAt": "2013-10-02T01:11:18.965Z"
            }
        }