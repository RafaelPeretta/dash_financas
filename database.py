from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Onde caralhos tá o banco?
# "sqlite:///./financas.db" significa:
# "sqlite": É um banco SQLite.
# "///./": Na mesma pasta do projeto.
# "financas.db": O nome do arquivo do nosso cofre.
SQLALCHEMY_DATABASE_URL = "sqlite:///./financas.db"

# 2. O "Motor" - O cara que vai se conectar
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# (A parte do "connect_args" é uma chatice específica do SQLite. Só aceita e vai)

# 3. A "Sessão" - O balcão de atendimento
# Toda vez que a gente for falar com o banco (pedir ou salvar dados),
# a gente vai abrir um "atendimento" (uma Session).
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. A "Base" - O molde
# Todos os nossos "modelos" (tipo o "Lançamento") vão usar essa Base como molde.
Base = declarative_base()