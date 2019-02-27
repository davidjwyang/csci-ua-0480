# columns and their types, including fk relationships
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# declarative base 
# function that gives back class.
# keeps track of all your other classes
# (it holds a catalog of tables)
from sqlalchemy.ext.declarative import declarative_base

# create the base class (declarative base)
# call it Base!
Base = declarative_base()

# implement the following three classes...

# class Scooter(Base):
class Scooter(Base):
	__tablename__ = 'scooter'

	scooter_id = Column('scooter_id', Integer, primary_key=True)
	acquired_date = Column('acquired_date' , Date)
	retired = Column('retired', Boolean, default=False)
	#'scooter_type_id',
	scooter_type_id = Column(Integer, ForeignKey("scooter_type.scooter_type_id"))
	
	scooter_type = relationship("ScooterType", back_populates="scooters")
	
	def __str__(self):
		return f'id: {self.scooter_id} retired: {self.retired}'\
			+ f' acquired_date: {self.acquired_date}'
	def __repr__(self):
			return f'id: {self.scooter_id} retired: {self.retired}' \
				+ f' acquired_date: {self.acquired_date}'

	def to_dict(self):
		scooter_dict = {}
		scooter_dict.update({ "acquired_date" : self.acquired_date.strftime('%Y-%m-%d') })
		scooter_dict.update({ "retired": self.retired })
		scooter_dict.update({ "scooter_type" : self.scooter_type.model })
		scooter_dict.update({ "max_speed" : self.scooter_type.max_speed })
		scooter_dict.update({ "weight" : self.scooter_type.weight })
		scooter_dict.update({ "company" : self.scooter_type.company.name })
		scooter_dict.update({ "website" : self.scooter_type.company.website })
		return scooter_dict
			
# class ScooterType(Base):
class ScooterType(Base):
	__tablename__ = 'scooter_type'

	scooter_type_id = Column('scooter_type_id', Integer, primary_key=True)
	model = Column('model', String)
	max_range = Column('max_range', Integer)
	weight = Column('weight', Integer)
	max_speed = Column('max_speed', Integer)
	#'company_id',
	company_id = Column(Integer, ForeignKey("company.company_id"))
	
	company = relationship("Company", back_populates="scooter_types")
	scooters = relationship("Scooter", back_populates="scooter_type")

	def __str__(self):
		return f'{self.company.name} {self.model}: max speed is {self.max_speed}' \
			+ f' weight is {self.weight}'
	def __repr__(self):
		return f'{self.company.name} {self.model}: max speed is {self.max_speed}' \
			+ f' weight is {self.weight}'
		
# class Company(Base):
class Company(Base):
	__tablename__ = 'company'

	company_id = Column('company_id', Integer, primary_key=True)
	name = Column('name', String)
	website = Column('website', String)
	founded = Column('founded', Integer)

	scooter_types = relationship("ScooterType", back_populates="company")

	def __str__(self):
		return f'{self.name} ({self.founded}): website is {self.website}'
	def __repr__(self):
		return f'{self.name} ({self.founded}): website is {self.website}'

