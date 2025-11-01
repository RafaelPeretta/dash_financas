from pydantic import BaseModel
from datetime import datetime 

class LancamentoCreate(BaseModel):
    descricao: str
    valor: float

class Lancamento(BaseModel):
    id: int
    descricao: str
    valor: float
    data_criacao: datetime

    class Config:
        from_attributes = True 