# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from create_db import Country

engine = create_engine('sqlite:///countries.db')

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Country).filter(Country.Continent=="EU").order_by(Country.capital).all()
print(query)