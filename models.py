from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base # Importa o "molde" que a gente criou

# Este é o "molde" de um Lançamento no nosso banco
class Lancamento(Base):
    __tablename__ = "lancamentos" # Nome da "tabela" (planilha) no banco

    # As colunas da nossa tabela:
    id = Column(Integer, primary_key=True, index=True) # ID único (1, 2, 3...)
    descricao = Column(String, index=True) # O texto (ex: "Padaria")
    valor = Column(Float) # O valor (ex: 10.50)
    
    # Data e hora que foi criado (com um valor padrão automático)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())