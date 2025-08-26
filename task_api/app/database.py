from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from dotenv import load_dotenv
from os import getenv

load_dotenv()
NEONDB_POSTRGRE_URL= getenv("NEONDB_POSTRGRE_URL")

engine = create_engine(
    NEONDB_POSTRGRE_URL,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"}
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
