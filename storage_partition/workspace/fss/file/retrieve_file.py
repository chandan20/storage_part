import os

from fss.helper.sql_queries import DatabaseQueryHelper
from fss.settings import DATA_ROOT
from fss.validate_auth import cursor


class RetrieveFile(object):
    def __init__(self, __dir_key, __file_key, __client_id):
        self.__dir_key = __dir_key
        self.__file_key = __file_key
        self.__client_id = __client_id

    def retrieve_files(self):
        __dir_name = self.__dir_key
        __file_name = self.__file_key
        if isinstance(self.__dir_key, int):
            __get_dir_name_by_id = DatabaseQueryHelper.GET_DIR_NAME_BY_ID_QUERY % self.__dir_key
            cursor.execute(__get_dir_name_by_id)
            __dir_name = cursor.fetchall()[0][0]
        if isinstance(self.__file_key, int):
            __get_file_name_by_id = DatabaseQueryHelper.GET_FILE_NAME_BY_ID_QUERY % self.__file_key
            cursor.execute(__get_file_name_by_id)
            __file_name = cursor.fetchall()[0][0]
        else:
            __get_file_id_by_name = DatabaseQueryHelper.GET_FILE_ID_BY_NAME_QUERY % (self.__file_key, self.__client_id)
            cursor.execute(__get_file_id_by_name)
            self.__file_key = cursor.fetchall()[0][0]
        __file_path = (os.path.join(DATA_ROOT, __dir_name, __file_name))
        with open(__file_path) as f:
            print(f.read())
