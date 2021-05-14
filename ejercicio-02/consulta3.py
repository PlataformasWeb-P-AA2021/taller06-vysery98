# Presentar los lenguajes de cada país.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from create_db import Country

engine = create_engine('sqlite:///countries.db')

Session = sessionmaker(bind=engine)
session = Session()

filtro_country = session.query(Country).all()

for Country in filtro_country:
    print("Country: %s\nLanguage(s): %s\n\n" % (Country.name, Country.languages))
