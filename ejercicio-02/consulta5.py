# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from create_db import Country

engine = create_engine('sqlite:///countries.db')

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Country).filter(or_(Country.name.like("%uador"), Country.capital.like("%ito"))).all()
print(query)
