import json
import csv
import os
import time
from datetime import datetime
import logging
from models import session, ParsingResults, ParsingSettings, ExportHistory, get_tasks_by_hist_id, \
    get_django_static_path, update_history_by_id, get_export_task_ids, get_default_settings


logger = logging.getLogger('export')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('logs/export.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


def get_simple_export_string(json_):
    return [json_[value] for value in json_]


def get_histories(hist_id):
    try:
        logger.info(f'Try export history id {hist_id}')
        tasks = get_tasks_by_hist_id(hist_id)

        django_path = get_django_static_path()

        csv_file = f'export_files\\task{hist_id}_{datetime.now().date()}.csv'
        csv_file_path = os.path.join(django_path, csv_file)

        with open(csv_file_path, 'w', newline='') as out_file:
            writer = csv.writer(out_file, delimiter=';')
            for task in tasks:
                json_obj = json.loads(task[1])
                str_ = get_simple_export_string(json_obj)
                writer.writerow([task[0].date(), *str_])
            update_history_by_id(hist_id, csv_file)
            logger.info(f'Save history id {hist_id} to {csv_file_path}')
    except Exception as e:
        logger.error(f'Failed export history id {hist_id}\n{e}')


while True:
    print('Run export iteration...')
    logger.info('Run export iteration...')
    default_settings = get_default_settings()
    export_tasks = get_export_task_ids()
    for export_task in export_tasks:
        id_ = export_task[0]
        get_histories(id_)
    print('Sleeping time...')
    time.sleep(60 * default_settings.sleeping_time)
