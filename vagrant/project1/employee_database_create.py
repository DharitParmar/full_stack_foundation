from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from employee_database_setup import Base, Employee, Address

engine = create_engine('sqlite:///employeedata.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

# enter values into Employee table
employee1 = Employee(name = "Dharit Parmar")
session.add(employee1)
session.commit()

# enter values into Address table
address1 = Address(street = "271 rutgers", zip = 1001, employee = employee1)
session.add(address1)
session.commit()

# enter values into Employee table
employee2 = Employee(name = "Ashwin Patel")
session.add(employee2)
session.commit()


# enter values into Address table
address2 = Address(street = "272 rutgers", zip = 1003, employee = employee2)
session.add(address2)
session.commit()

# enter values into Employee table
employee3 = Employee(name = "Dhruvil Patel")
session.add(employee3)
session.commit()


# enter values into Address table
address3 = Address(street = "273 rutgers", zip = 1003, employee = employee3)
session.add(address3)
session.commit()

print "Added menu item!"


