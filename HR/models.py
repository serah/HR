import sqlalchemy
import ibm_db_sa.ibm_db_sa
from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db2 = sqlalchemy.create_engine('ibm_db_sa://db2inst1:db2admin@localhost:50000/hr')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                         bind=db2))
Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  name = Column(String(50), unique=True)
  email = Column(String(120), unique=True)
  password = Column(String(100),unique=True)
  applicant = relation('Applicant',backref='user')

  def __init__(self, name=None, email=None, password=None):
      self.name = name
      self.email = email
      self.password = password

class Applicant(Base):
  __tablename__ = 'applicant'
  id = Column(Integer, primary_key=True)
  dob = Column(Date(), nullable=False)
  number = Column(Integer(20), unique=True)
  experience = Column(String(100),nullable=False)
  expertise = Column(String(500))
  header = Column(String(100),nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  status = relation('Applicant',backref='status')

  def __init__(self, dob=None, number=None, experience=None, expertise=None,
               header=None):
      self.dob = dob
      self.number = number
      self.experience = experience
      self.expertise = expertise
      self.header = header

class Vacancies(Base):
  __tablename__ = 'vacancies'
  id = Column(Integer, primary_key=True)
  date = Column(Date(), unique=True)
  position = Column(String(100))
  location = Column(String(100))
  vacancy = relation('Vacancies',backref='vacancy')

  def __init__(self, date=None, position=None, location=None):
      self.date = date
      self.position = position
      self.location = location

class Vacancy(Base):
  __bind_key__ = 'vacancy'
  __tablename__ = 'vacancy'
  id = Column(Integer, primary_key=True)
  responsibilities = Column(String(1000))
  description = Column(String(1000))
  experience = Column(Integer(2))
  education = Column(String(50))
  industry = Column(String(50))
  position_id = Column(Integer, ForeignKey('vacancies.id'))

  def __init__(self, responsibilities=None, description=None, experience=None,
               education=None, industry=None):
      self.responsibilities = responsibilities
      self.description = description
      self.experience = education
      self.industry = industry

class Status(Base):
  __bind_key__ = 'status'
  __tablename__ = 'status'
  id = Column(Integer, primary_key=True)
  DOI = Column(Date())
  approved = Column(Boolean)
  applicant = Column(Integer, ForeignKey('applicant.id'))

  def __init__(self, date=None, position=None, location=None):
      self.date = date
      self.position = position
      self.location = location

def init_db():
  Base.metadata.create_all(bind=db2)

