from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_CONNECTION=(
    "mssql+pyodbc://FASTAPI:Maya@1997@LAPTOP-5JRMBJI4/mayuresh"
)
engine = create_engine(
    SQL_CONNECTION,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

