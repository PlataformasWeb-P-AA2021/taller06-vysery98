# Presentar todos los países del continente americano

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from create_db import Country

engine = create_engine('sqlite:///countries.db')

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Country).filter(Country.Continent=="NA").all()
print(query)