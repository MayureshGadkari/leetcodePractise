# app/models.py
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class VehicleType(str, Enum):
    two_wheeler = "Two Wheeler"
    three_wheeler = "Three Wheeler"
    four_wheeler = "Four Wheeler"
    heavy_vehicle = "Heavy Vehicle"

class SubscriptionType(str, Enum):
    daily = "Daily"
    monthly = "Monthly"
    yearly = "Yearly"

class Vehicle(BaseModel):
    plate_number: str
    owner_name: str
    contact_number: str
    vehicle_type: VehicleType
    subscription_type: SubscriptionType
    subscription_end_date: datetime