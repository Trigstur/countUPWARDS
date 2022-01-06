import logging
import os
import time

import config

project_root: str = os.path.dirname(os.path.abspath(__file__ + "\.."))
dir_path = config.logs['log_dir']
session = int(time.time())

try:
    os.stat(dir_path)
except:
    os.mkdir(dir_path)

logging.basicConfig(
    filename='{}/{}.log'.format(dir_path, session),
    level=logging.DEBUG,
    filemode='w',
    format='%(asctime)s [ %(levelname)s ] : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


class Logger:
    message: str

    def log(self):
        logging.info(self)

    def note(self):
        print(self)
        logging.info(self)

    def debug(self):
        logging.debug(self)

    def warn(self):
        logging.warning(self)

    def error(self):
        print("[ERROR] {}".format(self))
        print("Error log saved at {}\{}\{}.log".format(project_root, dir_path, session))
        logging.error(self)
        exit()


Logger.log('Log Cleaner initialized')
experation_date = time.time() - config.logs['expire_days'] * 86400
entries = os.listdir(dir_path)
Logger.debug(f'\n<======Log Cleaner Config======> \n'
             f'Directory : /{dir_path} \n'
             f'File expiration : {config.logs["expire_days"]} days \n'
             f'Logs to scan: {len(entries)}\n'
             '<=========================>')

for entry in entries:
    time_created = os.stat(os.path.join(dir_path, entry)).st_ctime
    if time_created < experation_date:
        try:
            Logger.log('Deleted for exceeding expiration limit : %s' % (config.logs['log_dir'] + '/' + entry))
            os.remove(config.logs['log_dir'] + '/' + entry)
        except Exception as e:
            Logger.error('%s' % e)
