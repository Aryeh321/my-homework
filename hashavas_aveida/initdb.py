from sqlalchemy.orm import sessionmaker
from database import engine, Base, Session
from classes import Aveidah

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db_session = Session()
db_session.add_all([
    Aveidah(name="wallet", color="brown", size="small", shape="one fold", location="parking lot"),
    Aveidah(name="sippy cup", color="blue", size="small", shape="round", location="shul"),
    Aveidah(name="watch", color="silver", size="small", shape="round face", location="npgs"),
    Aveidah(name="pen", color="green", size="small", shape="parker", location="park")
])
db_session.commit()
db_session.close()