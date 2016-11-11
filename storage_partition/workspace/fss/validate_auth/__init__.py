from fss.helper import conf_reader
from fss.helper.db_helper import DbHelper


__host = conf_reader.get_conf_value('database', 'host')
__port = conf_reader.get_conf_value('database', 'port')
__user = conf_reader.get_conf_value('database', 'user')
__password = conf_reader.get_conf_value('database', 'password')
__database = conf_reader.get_conf_value('database', 'db_name')
__db_helper = DbHelper(__host, __port, __user, __password, __database)
cursor = __db_helper.connect()
