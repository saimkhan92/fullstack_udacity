from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine=create_engine("sqlite:///restaurantmenu.db")

Base.metadata.bind=engine

DBSession=sessionmaker(bind=engine)

session=DBSession()

#mySecondRestaurant= Restaurant(name="Tiffins")
#session.add(mySecondRestaurant)
#session.commit()
session.query(Restaurant).all()

for i in session.query(Restaurant).all():
	print(i.name)
