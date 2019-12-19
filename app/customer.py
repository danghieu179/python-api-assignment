from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Date, create_engine
from config import DATABASE_URL 
Base = declarative_base()


class Customers(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    dob = Column(Date)
    updated_at = Column(DateTime(timezone=True),default=datetime.utcnow(),onupdate=datetime.utcnow())


if __name__ == "__main__":
    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

