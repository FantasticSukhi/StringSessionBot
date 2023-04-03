from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from env import DATABASE_URL

count_ = 0
def start() -> scoped_session:
    if DATABASE_URL == "":
        if count_ < 1:
            count += 1
            return print("𝔇𝔞𝔱𝔞𝔟𝔞𝔰𝔢 𝔲𝔯𝔩 𝔫𝔬𝔱 𝔭𝔯𝔬𝔳𝔦𝔡𝔢𝔡..\n𝔅𝔲𝔱 𝔱𝔥𝔦𝔰 𝔱𝔦𝔪𝔢 ℑ 𝔴𝔬𝔫'𝔱 𝔰𝔱𝔬𝔭 😉")
        return
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

if DATABASE_URL != "":
    BASE = declarative_base()
    SESSION = start()
