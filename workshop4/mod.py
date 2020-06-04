from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from conect import engine

Base = declarative_base()


class users(Base):
    __tablename__  = 'users'

    user_id = Column(Integer, primary_key=True)

    user_name = Column(String(50), nullable=False)
    user_phone = Column(String(14), nullable=False, unique=True)

class taxi(Base):
    __tablename__ = 'taxi'

    taxi_id = Column(Integer, primary_key=True)

    name_company = Column(String(50), nullable=False)
    cars = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)


class zamov(Base):
    __tablename__  = 'zamov'

    id_zamov = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey(users.user_id), primary_key=True)
    id_taxi = Column(Integer, ForeignKey(taxi.taxi_id), primary_key=True)

    date_c = Column(Date, nullable=False)
    place_A = Column(String(50), nullable=False)
    place_B = Column(String(50), nullable=False)
    f_price = Column(Float, nullable=False)
    distance = Column(Float, nullable=False)




Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)


