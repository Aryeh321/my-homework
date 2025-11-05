from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('mysql+pymysql://root:root@localhost:3306/hashavas_aveidah')
Base = declarative_base()
Session = sessionmaker(bind=engine)