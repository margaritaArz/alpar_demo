from configparser import RawConfigParser

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, union
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import os

local_config_path = os.path.join(os.getcwd(), 'local.conf')
config = RawConfigParser()
config.read(local_config_path)

user = config.get('main', 'USER')
passwd = config.get('main', 'PASSWORD')

CONNECTION_STRING = f'postgresql+psycopg2://{user}:{passwd}@localhost/django_db'
engine = create_engine(CONNECTION_STRING, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class ParsingTasks(Base):
    __tablename__ = 'mainapp_parsingtasks'

    id = Column(Integer, primary_key=True)
    link = Column(String)
    activate = Column(Boolean)
    update_time = Column(Integer)
    results = relationship('ParsingResults', backref='parsingtasks')

    def __repr__(self):
        return f"<Task({self.id}, {self.activate}, {self.update_time})>"


class ParsingResults(Base):
    __tablename__ = 'mainapp_parsingresults'

    id = Column(Integer, primary_key=True)
    status = Column(Integer)
    task_id_id = Column(Integer, ForeignKey('mainapp_parsingtasks.id'))
    datetime = Column(DateTime)
    json = Column(String)

    def __repr__(self):
        return f"<Result({self.id}, {self.json})>"


class ParsingSettings(Base):
    __tablename__ = 'settingapp_parsingsettings'

    id = Column(Integer, primary_key=True)
    worker_name = Column(String)
    firefox_profile = Column(String)
    sleeping_time = Column(Integer)
    start_iteration_time = Column(DateTime)
    finish_iteration_time = Column(DateTime)
    last_ping_time = Column(DateTime)

    def __repr__(self):
        return f"<Settings({self.id}, {self.worker_name})>"
