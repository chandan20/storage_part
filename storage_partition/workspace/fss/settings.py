import os


# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
PROJ_ROOT = os.path.abspath(os.path.join(APP_ROOT, ".."))
CONF_ROOT = os.path.join(APP_ROOT, 'config')
DATA_ROOT = os.path.join(APP_ROOT, 'data')
