from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import DATABASE_URL

# Создание движка для взаимодействия с базой данных
engine = create_engine(DATABASE_URL)

# Базовый класс для моделей SQLAlchemy
Base = declarative_base()

# Конфигурация сессии
Session = sessionmaker(bind=engine)

# Создание экземпляра сессии
session = Session()


# Проверка соединения с базой данных
def test_connection():
    try:
        with engine.connect() as connection:
            print("Подключение к БД произошло успешно")
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")


# Вызов проверки
test_connection()
