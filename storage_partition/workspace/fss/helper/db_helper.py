import psycopg2
import psycopg2.extras


class DbHelper(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        __conn = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                  database=self.database)
        __conn.autocommit = True
        cursor = __conn.cursor()
        return cursor
