import os
from configparser import ConfigParser
from fss.settings import CONF_ROOT


def get_conf_value(section, option):
    __config = ConfigParser()
    __conf_file_path = os.path.join(CONF_ROOT, 'conf.ini')
    __config.read(__conf_file_path)
    return __config.get(section=section, option=option)
