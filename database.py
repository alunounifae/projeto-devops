from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from dotenv import load_dotenv
from os import getenv

# Carrega o .env base (variáveis padrão)
load_dotenv()

# Se estiver no ambiente de teste, carrega variáveis do .env.test sobrescrevendo as anteriores
if getenv("ENV") == "test":
    load_dotenv(".env.test", override=True)

DATABASE_URL = getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não está definida. Verifique seu .env ou .env.test.")

# Ajusta connect_args somente se for SQLite (sqlite precisa de check_same_thread)
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependência para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()