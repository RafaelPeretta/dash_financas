from pydantic import BaseModel

class LancamentoCreate(BaseModel):
    descricao: str
    valor: float