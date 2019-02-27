from sqlalchemy.orm import sessionmaker
import db
from model import Company, ScooterType, Scooter, Base
from datetime import datetime
import random

# use the session object and imported classes (Company, Scooter, etc.)
# ... to create companies, types and scooters in the database

Session = sessionmaker(db.engine)
session = Session()

# scooter_types = {"company1": "type1", "company1": "type2", "company1": "type3", "company1": "type4",\
# 				"company2": "type1", "company2": "type2", "company2": "type3", \
# 				"company3": "type1", "company3": "type2",
# 				"company4": "type1"}

# companies = {"name": "company1", "website": "company1.com", "founded": 2001 }
# scooter_types.append({"model": "", "max_range": "", "weight": "", "max_speed": "",\
# 		"company_id": ""})

companies = []
for i in range(4):
	c = Company()
	c.name = f"company{i}"
	c.website = f"company{i}.com"
	c.founded = 2000 + i
	companies.append(c)



scooter_types = []
for i in range(16):
	c = random.choice(companies)
	st = ScooterType()
	st.model = f"model{random.randint(1,10)}"
	st.max_range = random.randint(30,40) 
	st.weight = random.randint(25,30)
	st.max_speed = random.randint(20,25)
	st.company = c
	scooter_types.append(st)

scooters = []
for i in range(112):
	st = random.choice(scooter_types)
	s = Scooter()
	s.acquired_date = f'{random.randint(2014,2018)}-{random.randint(1, 12):02}-{random.randint(1,28):02}'
	if random.randint(0,1):
		s.retired = True
	s.scooter_type = st
	scooters.append(s)

session.add_all(scooters)

session.commit()

for c in session.query(Company):
 print(f'The company, {c}, has the following scooter models:');
 for i, scooter_type in enumerate(c.scooter_types):
  print(i, scooter_type)
 print('\n')

for s in session.query(ScooterType):
 print(f'{s.company.name} ==> {s.model}')