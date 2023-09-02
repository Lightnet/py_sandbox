# https://sqlmodel.tiangolo.com/tutorial/code-structure/
# https://www.geeksforgeeks.org/using-sqlalchemy-to-insert-mysql-timestamp-column-values/
# 
# 
# 
# database set up

import datetime
import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, TIMESTAMP, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
#from sqlalchemy.orm import relationship
#from sqlalchemy.orm import Session
from sqlalchemy import create_engine
#from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

#================================================
# TABLE
#================================================
class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__ = "user_account"

  serialize_only = ('id','alias','role')

  id: Mapped[int] = mapped_column(primary_key=True)
  #name: Mapped[str] = mapped_column(String(30))
  name: Mapped[Optional[str]]
  fullname: Mapped[Optional[str]]
  alias: Mapped[str] = mapped_column(String(30))
  passphrase: Mapped[str] = mapped_column(String(64))
  role: Mapped[str] = mapped_column(String(64),default="member")
  groupid: Mapped[str] = mapped_column(String(64),default="member")
  ban: Mapped[Boolean] = mapped_column(Boolean,default=False)
  created_at: Mapped[TIMESTAMP] = mapped_column(
    #DateTime(timezone=True),
    TIMESTAMP,
    default=datetime.datetime.utcnow
  )
  updated_at: Mapped[datetime.datetime] = mapped_column(
    DateTime(timezone=True),
    default=datetime.datetime.utcnow,
    onupdate=datetime.datetime.utcnow
  )

  def __repr__(self) -> str:
    return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}, alias={self.alias})"

class Entity(Base):
  __tablename__ = "entity"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[Optional[str]]

  created_at: Mapped[TIMESTAMP] = mapped_column(
    TIMESTAMP,
    default=datetime.datetime.utcnow
  )
  updated_at: Mapped[datetime.datetime] = mapped_column(
    DateTime(timezone=True),
    default=datetime.datetime.utcnow,
    onupdate=datetime.datetime.utcnow
  )

  def __repr__(self) -> str:
    return f"User(id={self.id!r}, name={self.name!r})"

from sqlalchemy import JSON
import json
class Task(Base):
  __tablename__ = "task"
  impl = JSON
  #serialize_only = ('id','content','isDone')

  id: Mapped[int] = mapped_column(primary_key=True)
  content: Mapped[str]
  isDone: Mapped[Boolean] = mapped_column(Boolean,default=False)

  created_at: Mapped[TIMESTAMP] = mapped_column(
    TIMESTAMP,
    default=datetime.datetime.utcnow
  )
  updated_at: Mapped[datetime.datetime] = mapped_column(
    DateTime(timezone=True),
    default=datetime.datetime.utcnow,
    onupdate=datetime.datetime.utcnow
  )

  def __repr__(self) -> str:
    return f"User(id={self.id!r})"
  
  def to_json(self):
    return {"id":self.id,"content":self.content, "isDone":self.isDone}
  
  def process_bind_param(self, value, dialect):
    if value is not None:
      value = json.dumps(value)
    return value
  
  def process_result_value(self, value, dialect):
    if value is not None:
      value = json.loads(value)
    return value

#init set up database
engine = create_engine("sqlite:///database.sqlite", echo=True)
#create table
Base.metadata.create_all(engine)
# create a session factory
#Session = sessionmaker(bind=engine)
# insert some data
#session = Session()

#================================================
# TABLE
#================================================

"""
Entity = db.Table('Entity', metadata,
  db.Column('Id', db.Integer(),primary_key=True),
  db.Column('userid', db.String(255), nullable=False),
  db.Column('hashid', db.String(255), nullable=False),
  db.Column('blockid', db.String(), nullable=False),#x,y,z
  db.Column('name', db.String(255), nullable=False),
  db.Column('data', db.String(), nullable=False),
  db.Column('x', db.Float(), default=0),
  db.Column('y', db.Float(), default=0),
  db.Column('z', db.Float(), default=0),
  db.Column('role', db.String(255), default="public"),
  db.Column('locked', db.Boolean(), default=False),
  db.Column('ban', db.Boolean(), default=False)
)

GroupPermission = db.Table('GroupPermission', metadata,
  db.Column('Id', db.Integer(),primary_key=True),
  db.Column('name', db.String(255), nullable=False),
  db.Column('data', db.String(), nullable=False),
  db.Column('role', db.String(255), default="member"),
  db.Column('locked', db.Boolean(), default=False),
  db.Column('ban', db.Boolean(), default=False)
)
"""
#================================================
# Test
#================================================
#query = db.insert(Student).values(Id=1, Name='Matthew', Major="English", Pass=True)
#Result = conn.execute(query)
#output = conn.execute(Student.select()).fetchall()
#print(output)
#conn.commit()# save data