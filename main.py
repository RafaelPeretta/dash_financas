from fastapi import FastAPI
import models # IMPORTA NOSSOS MODELOS
from database import engine # IMPORTA O "MOTOR" DO BANCO

# Essa linha é MÁGICA
# Ela diz: "Olha todos os moldes que usam 'Base' (lá do models.py)
# e CRIE ELES no banco de dados (o 'engine')"
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Porra, chefe, tá rodando e o banco tá pronto!"}