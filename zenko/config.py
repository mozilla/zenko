import os
import importlib
import sys


CONFIG_PATH_LOCATIONS = [
    '/etc/zenko',
    os.path.abspath(os.path.dirname(__file__))
    ]
DEFAULT_CONFIG = 'zenko.config.DefaultConfig'


class DefaultConfig(object):
    host = 'localhost'
    dbname = 'tiles'
    user = 'read_only'
    password = 'secret'

    def login_string(self):
        return ' '.join([
            "host='%s'" % self.host,
            "dbname='%s'" % self.dbname,
            "user='%s'" % self.user,
            "password='%s'" % self.password,
            ])


def load_config(object_name=os.environ.get('ZENKO_SETTINGS', DEFAULT_CONFIG)):
    for path in CONFIG_PATH_LOCATIONS:
        sys.path.append(path)
    module_name, class_name = object_name.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)()


config = load_config()
