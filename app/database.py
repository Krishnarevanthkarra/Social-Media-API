from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# import psycopg2
# from psycopg2.extras import RealDictCursor  # TO GET COL NAMES
# import time

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:krishna%402004@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="fastapi",
#             user="postgres",
#             password="krishna@2004",
#             cursor_factory=RealDictCursor,
#         )
#         cursor = conn.cursor()
#         print("Database Connection was successfull")
#         break
#     except Exception as error:
#         print("Connecting to DataBase Failed")
#         print("Error was:", error)
#         time.sleep(2)
