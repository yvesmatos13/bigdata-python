from pydantic import BaseModel

class ExcecaoNegocio(BaseModel):
    codigo:int
    mensagem: str
    detalhes: str 

    class Config:
        schema_extra = {
            "example": {
                "codigo":400,
                "mensagem": "string",
                "detalhes": "string"
            }
        }

def excecaoNegocioResponse(codigo, menssagem, detalhes):
    return {"codigo":codigo, "menssagem":menssagem, "detalhes":detalhes}
