from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_db import Country

import json
import requests

engine = create_engine('sqlite:///countries.db')

Session = sessionmaker(bind=engine)
session = Session()

archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
data_json = archivo.json()

for d in data_json:
    p = Country(name=d['CLDR display name'], capital=d['Capital'], Continent=d['Continent'], dial=d['Dial'], geoname=d['Geoname ID'], \
            itu=d['ITU'], languages=d['Languages'], independent=d['is_independent'])

    session.add(p)

session.commit()
