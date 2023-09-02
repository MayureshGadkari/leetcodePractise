from sqlalchemy import Column,Integer,String
from database import Base

class local_db(Base):
    __table_name__ = "dbo.ilm_platform_onboarding_master"
    id=Column(Integer)
    technologyId = Column(Integer)
    technologyCatId = Column(Integer)
    status=Column(String)
    enabled = Column(String)
