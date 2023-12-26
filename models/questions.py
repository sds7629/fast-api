from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base


class Question(Base):
    __tablename__ = "question"

    id: int = Column(Integer, primary_key=True)
    subject: str = Column(String, nullable=False)
    content: str = Column(Text, nullable=False)
    create_data: str = Column(DateTime, nullable=False)


class Answer(Base):
    __tablename__ = "answer"

    id: int = Column(Integer, primary_key=True)
    content: str = Column(Text, nullable=False)
    create_date: str = Column(String, nullable=False)
    question_id: int = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answer")
