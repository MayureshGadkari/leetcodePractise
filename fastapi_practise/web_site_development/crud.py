from sqlalchemy.orm import Session
from models import User,Vehicle
from schemas import create_user as create_user_schema
# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.user_id == user_id).first()
def create_user(db:Session,user:create_user_schema):
    output_list = []
    db_user = User(user_name=user.user_name,
                   phone_number=user.phone_number,
                   email_id=user.email_id,
                   gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    pk = db_user.user_id
    db_vehicle = Vehicle(category=user.category,
                         model=user.model,
                         plate_number=user.plate_no,
                         user_id=pk)
    db.add(db_vehicle)
    db.commit()
    db.refresh

    return [db_user,db_vehicle]

def get_user_details(db:Session, user_id:int):
    return db.query(Vehicle).join(User,Vehicle.user_id==User.user_id).filter(User.user_id == user_id).all()