from sqlalchemy import create_engine

engine = create_engine('sqlite:///countries.db')

from sqlalchemy.ext.declarative import declarative_base
db = declarative_base()


from sqlalchemy import Column, Integer, String

class Country(db):
    __tablename__ = 'Country'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)
    Continent = Column(String)
    dial = Column(String)
    geoname = Column(String)
    itu = Column(String)
    languages = Column(String)
    independent = Column(String)

    def __repr__(self):
        return "Paises: nombre=%s capital=%s continente:%s dial:%s geoname:%s itu:%s languages:%s independent:%s" % (
                        self.name, 
                        self.capital, 
                        self.Continent,
                        self.dial,
                        self.geoname,
                        self.itu,
                        self.languages,
                        self.independent)

db.metadata.create_all(engine)
