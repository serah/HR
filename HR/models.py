import ibm_db_sa.ibm_db_sa
#from sqlalchemy.orm import sessionmaker
from HR import create_engine, Column, String, Text, Integer
from HR import declarative_base

engine = create_engine('ibm_db_sa://db2inst1:db2admin@localhost:50000/hr')
Base = declarative_base()

#db_session = sessionmaker(bind=engine, autoflush=True, transactional=True)
#session = db_session()

class users(Base):
  """
  User class is mapped with users table
  """

  __tablename__ = 'users'
  id = Column(Integer, autoincrement=True)
  name = Column(String(50))
  email = Column(String(100),primary_key=True,unique=True)
  password = Column(Text)
  dob = Column(Text)
  expertise = Column(Text)
  headline = Column(Text)
  level = Column(Integer)
  experience = Column(Text)
  number = Column(Text)

  def __init__(self, name, email, password, level, \
 	dob, expertise, headline, experience, number ):
 		self.name = name
 		self.email = email
 		self.password = password
 		self.level = level
 		self.dob = dob
 		self.expertise = expertise
 		self.headline = headline
 		self.experience = experience
 		self.number = number

class vacancy(Base):
 	"""
 	This is a table for creating vacancies
 	"""
 	__tablename__ = 'vacancy'
 	id = Column(String(100), primary_key=True)
 	name = Column(String(50))
 	department = Column(String(50))
 	description = Column(Text)
 	responsibilities = Column(Text)
 	experience = Column(String(50))
 	education = Column(Text)
 	location = Column(String(100))

 	def __init__(self, _id ,name, department, description):
 		self._id = _id
 		self.name = name
 		self.department = department
 		self.description = description

def init_db():
  """docstring for init_db"""
  Base.metadata.create_all(bind=engine)

