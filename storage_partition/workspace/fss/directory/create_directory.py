import os
from fss.helper.sql_queries import DatabaseQueryHelper
from fss.validate_auth import cursor
from fss.settings import DATA_ROOT


class CreateDirectory(object):
    def __init__(self, dir_name, client_id):
        self.__dir_name = dir_name
        self.__is_created = False
        self.__client_id = client_id

    def create_dir(self):
        self.__is_created = False
        if not os.path.exists(os.path.join(DATA_ROOT, self.__dir_name)):
            os.makedirs(os.path.join(DATA_ROOT, self.__dir_name))
            self.__is_created = True

    def insert_db(self):
        if self.__is_created:
            insert_query = DatabaseQueryHelper.INSERT_T_DIR_QUERY % (self.__dir_name, self.__client_id)
            cursor.execute(insert_query)
            cursor.execute(DatabaseQueryHelper.GET_DIR_ID_QUERY)
            dir_id = str(cursor.fetchall()[0][0])
            print("Directory created successfully.")
            print("Your unique directory id is:", dir_id)
        else:
            print("A directory with this name already exist.")
