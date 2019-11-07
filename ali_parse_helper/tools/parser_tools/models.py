from configparser import RawConfigParser

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, union, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import os
import sys
from datetime import datetime

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


association_h_and_t = Table('hist_and_task', Base.metadata,
    Column('parsingresults_id', Integer, ForeignKey('mainapp_parsingresults.id')),
    Column('exporthistory_id', Integer, ForeignKey('exportapp_exporthistory.id'))
)


class ExportHistory(Base):
    __tablename__ = 'exportapp_exporthistory'

    id = Column(Integer, primary_key=True)
    out_file_path = Column(String)
    catch_time = Column(DateTime)
    results_id = relationship("ParsingResults", secondary=association_h_and_t)

    def __repr__(self):
        return f"<History({self.id}, {self.out_file_path})>"


def get_tasks_by_hist_id(hist_id):
    task_for_export = 'select main_pars_res.datetime, main_pars_res.json, ' \
                      'main_pars_t.link from exportapp_exporthistory_results_id as exp_h_r ' \
                      'inner join mainapp_parsingresults as ' \
                      'main_pars_res on main_pars_res.id = exp_h_r.parsingresults_id ' \
                      'inner join mainapp_parsingtasks as ' \
                      'main_pars_t on main_pars_t.id = main_pars_res.task_id_id ' \
                      'inner join exportapp_exporthistory as ' \
                      'exp_hist on exp_hist.id = exp_h_r.exporthistory_id ' \
                      f'where exp_h_r.exporthistory_id = {hist_id} and exp_hist.user_id_id = main_pars_t.task_user_id_id;'
    return session.execute(task_for_export)


def get_django_static_path():
    # rework_to_sql
    sys.path.append(r"C:\Users\DK\Desktop\ali_parser\alpar_demo\ali_parse_helper")
    from ali_parse_helper import settings

    return settings.STATICFILES_DIRS[0]


def update_history_by_id(id, file_path):
    history = session.query(ExportHistory).filter_by(id=id).first()
    history.out_file_path = file_path
    history.catch_time = datetime.now()
    session.commit()


def get_export_task_ids():
    ids = 'select exp_hist.id from exportapp_exporthistory as exp_hist where exp_hist.catch_time is Null;'
    return session.execute(ids)


def get_default_settings():
    return session.query(ParsingSettings).filter_by(worker_name='default').first()
