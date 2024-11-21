from sqlalchemy import Column, Integer, String
from config import Base

# Определение модели
class PartnerModel(Base):
    __tablename__ = 'partners'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(10), nullable=False)
    company_name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=True)
    inn = Column(String, nullable=False)
    boss_name = Column(String(50), nullable=False)
    phone_number = Column(String(30), nullable=False)
    mail = Column(String(100), nullable=True)
    rank = Column(Integer, nullable=False)