from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models 
import schemas 
from database import engine, SessionLocal
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Porra, chefe, tá rodando e o banco tá pronto!"}


@app.post("/lancamentos/", response_model=schemas.Lancamento)
def criar_lancamento(
    lancamento: schemas.LancamentoCreate, 
    db: Session = Depends(get_db)
):
    db_lancamento = models.Lancamento(
        descricao=lancamento.descricao,
        valor=lancamento.valor
    )
    
    db.add(db_lancamento) 
    db.commit()          
    db.refresh(db_lancamento) 
    
    return db_lancamento

@app.get("/lancamentos/", response_model=List[schemas.Lancamento])
def ler_lancamentos(db: Session = Depends(get_db)):
    
    lancamentos = db.query(models.Lancamento).all()
    
    return lancamentos