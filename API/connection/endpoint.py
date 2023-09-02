from fastapi import FastAPI,HTTPException,Depends
import models
from sqlalchemy.orm import Session
from database import engine,SessionLocal
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close

@app.get("/")
async def hello(db:Session = Depends(get_db())):
    return db.query(models.local_db).all()

