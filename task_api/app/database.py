from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



# URL do banco PostgreSQL na Neon
from dotenv import load_dotenv
from os import getenv

load_dotenv()
NEONDB_POSTRGRE_URL= getenv("NEONDB_POSTRGRE_URL")

# Criação do engine com melhorias
engine = create_engine(
    NEONDB_POSTRGRE_URL,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"}  # Importante para NeonDB
)
print("Conexão carregada:", NEONDB_POSTRGRE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependência para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
