from schemas import create_user as create_user_schema,get_details_request
from crud import create_user,get_user_details
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database_connection import SessionLocal, ENGINE
models.Base.metadata.create_all(bind=ENGINE)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user_endpoint(user: create_user_schema, db: Session = Depends(get_db)):
    # db_user = crud.get_user_by_email(db, email=user.email)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)
@app.get("/get_user")
def get_user(data:get_details_request,db:Session = Depends(get_db)):
    return get_user_details(data,db=db)