from sqlalchemy import Column, Integer, String
from database.config import Base

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

    def __repr__(self):
        return (
            f"<Partner(id={self.id}, type='{self.type}', company_name='{self.company_name}', address='{self.address}', "
            f"inn='{self.inn}', boss_name='{self.boss_name}', phone_number='{self.phone_number}', mail='{self.mail}', "
            f"rank='{self.rank}')>"
        )