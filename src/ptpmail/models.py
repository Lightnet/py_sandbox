# https://sqlmodel.tiangolo.com/tutorial/code-structure/
# https://www.geeksforgeeks.org/using-sqlalchemy-to-insert-mysql-timestamp-column-values/
# 
# 
# 
# database set up

import datetime
import sqlalchemy as db

engine = db.create_engine("sqlite:///maildb.sqlite")
conn = engine.connect() 
metadata = db.MetaData() #extracting the metadata
#division= db.Table('divisions', metadata, autoload=True, autoload_with=engine) #Table object
#print(repr(metadata.tables['divisions']))
#================================================
# TABLE
#================================================
"""
Student = db.Table('Student', metadata,
  db.Column('Id', db.Integer(),primary_key=True),
  db.Column('Name', db.String(255), nullable=False),
  db.Column('Major', db.String(255), default="Math"),
  db.Column('Pass', db.Boolean(), default=True)
)
"""

User = db.Table('User', metadata,
  db.Column('Id', db.Integer(),primary_key=True),
  db.Column('alias', db.String(255), nullable=False),
  db.Column('passphrase', db.String(255), nullable=False),
  db.Column('pass_hash', db.String(255)),
  db.Column('role', db.String(32), default="member"),
  db.Column('status', db.String(16), default="offline"),
  db.Column('groupid', db.String(16), default="default"),
  db.Column('ban', db.Boolean(), default=False),
  db.Column('created_at', db.types.DateTime(timezone=True), default=datetime.datetime.utcnow)
)
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
"""
"""
MapData = db.Table('MapData', metadata,
  db.Column('Id', db.Integer(),primary_key=True),
  db.Column('userid', db.String(255), nullable=False),
  db.Column('hashid', db.String(255), nullable=False),
  db.Column('name', db.String(255), nullable=False),
  db.Column('data', db.String(), nullable=False),
  db.Column('x', db.Float(), default=0),
  db.Column('y', db.Float(), default=0),
  db.Column('z', db.Float(), default=0),
  db.Column('role', db.String(255), default="public"),
  db.Column('locked', db.Boolean(), default=False),
  db.Column('ban', db.Boolean(), default=False)
)
"""

"""
GroupPermission = db.Table('GroupPermission', metadata,
  db.Column('Id', db.Integer(),primary_key=True),
  db.Column('name', db.String(255), nullable=False),
  db.Column('data', db.String(), nullable=False),
  db.Column('role', db.String(255), default="member"),
  db.Column('locked', db.Boolean(), default=False),
  db.Column('ban', db.Boolean(), default=False)
)
"""

metadata.create_all(engine)


#================================================
# Test
#================================================
#query = db.insert(Student).values(Id=1, Name='Matthew', Major="English", Pass=True)
#Result = conn.execute(query)
#output = conn.execute(Student.select()).fetchall()
#print(output)
#conn.commit()# save data