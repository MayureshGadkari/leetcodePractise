# app/main.py
from fastapi import FastAPI, Depends, HTTPException, Form, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import List
from models import Vehicle, VehicleType, SubscriptionType

app = FastAPI()

# Database configuration
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
Base: DeclarativeMeta = declarative_base()

# Database models
class VehicleModel(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String, unique=True, index=True)
    owner_name = Column(String)
    contact_number = Column(String)
    vehicle_type = Column(SQLAlchemyEnum(VehicleType), nullable=False)
    subscription_type = Column(SQLAlchemyEnum(SubscriptionType), nullable=False)
    subscription_end_date = Column(DateTime(timezone=True), server_default=func.now())

Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

# Templates configuration
templates = Jinja2Templates(directory="app/templates")

# Routes

@app.post("/register_vehicle/")
async def register_vehicle(
    vehicle: Vehicle,
    db: Session = Depends(get_db)
):
    # Register a new vehicle
    db_vehicle = VehicleModel(**vehicle.dict(), subscription_end_date=datetime.now())
    db.add(db_vehicle)
    db.commit()
    return {"message": "Vehicle registered successfully"}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/search_vehicle/")
async def search_vehicle(plate_number: str = Form(...), db: Session = Depends(get_db)):
    # Search for vehicle details by plate number
    vehicle = db.query(VehicleModel).filter_by(plate_number=plate_number).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)