from selenium import webdriver
import json
from datetime import datetime
import time


from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, union
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


CONNECTION_STRING = 'postgresql+psycopg2://django_user:SuperNewPassword2019@localhost/django_db'
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


def get_goods_parameters_selenium():
    query_time_limit = 'select * from ' \
                       '(select distinct on (results.task_id_id) tasks.id, tasks.link, tasks.update_time, ' \
                       'results.task_id_id, results.datetime ' \
                       'from mainapp_parsingtasks as tasks ' \
                       'left join mainapp_parsingresults as results ' \
                       'on results.task_id_id = tasks.id order by results.task_id_id, results.datetime desc) ' \
                       'as final_table ' \
                       'where now() - (final_table.update_time * INTERVAL \'1 hour\') ' \
                       '> final_table.datetime or final_table.datetime is Null'
    profile = webdriver.FirefoxProfile(r'C:\Users\DK\AppData\Roaming\Mozilla\Firefox\Profiles\i4xmbm85.default')
    browser = webdriver.Firefox(profile)

    while True:
        print('Run iteration...')

        distinct_tasks = session.execute(query_time_limit)
        for task in distinct_tasks:
            browser.get(task[1])

            result_dict = {}

            title = browser.find_element_by_class_name('product-title')
            print(title.text)
            result_dict['title'] = title.text
            price = browser.find_element_by_class_name('product-price-value')
            print(price.text)
            result_dict['price'] = price.text
            json_result = json.dumps(result_dict)
            print(json_result)

            new_record = ParsingResults()
            new_record.status = 1
            new_record.datetime = datetime.now()
            new_record.task_id_id = task[0]
            new_record.json = json_result
            session.add(new_record)
            session.commit()

        print('Sleeping time...')
        time.sleep(60 * 5)


get_goods_parameters_selenium()
