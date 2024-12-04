from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных PostGreSQL
engine = create_engine("postgresql+psycopg://postgres:123321na123321NA@localhost:5432/test")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()