from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.events import Event
from models.users import User

database_file = "practice.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(
    database_connection_string,
    echo=True,
    connect_args=connect_args,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_url)

Base = declarative_base()

# def conn():
#     SQLModel.metadata.create_all(engine_url)


# def get_session():
#     with Session(engine_url) as session:
#         yield session
