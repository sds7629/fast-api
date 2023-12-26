from db.connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

## sqlalchemy.orm.relationship


class User(Base):
    __tablename__ = "user"

    team_id = Column(Integer, ForeignKey("team.id"))


class Team(Base):
    __tablename__ = "team"

    users = relationship("User")


## One to Many


class User(Base):
    __tablename__ = "user"

    team_id = Column(Integer, ForeignKey("team.id"))
    team = relationship("Team", back_populates="users")


class Team(Base):
    __tablename__ = "team"

    users = relationship("User", back_populates="team")


## One to One


class User(Base):
    __tablename__ = "user"

    team_id = Column(Integer, ForeignKey("team.id"))
    team = relationship("Team", back_populates="user")  # Many to one 관계의 참조 변수


class Team(Base):
    __tablename__ = "team"
    # One to Many 의 참조 변수, uselist를 False로 설정하여 하나의 객체만 참조하도록 설정
    user = relationship("User", back_populates="team", uselist=False)


## Many to Many

association_table = Table(
    "association",
    Base.metadata,
    Column("left_id", ForeignKey("left.id"), primary_key=True),
    Column("right_id", ForeignKey("right.id"), primary_key=True),
)


class Left(Base):
    __tablename__ = "left"

    rights = relationship("Right", secondary=association_table, back_populates="lefts")


class Right(Base):
    __tablename__ = "right"

    lefts = relationship("Left", secondary=association_table, back_populates="rights")
