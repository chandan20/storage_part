import os
from fss.helper.sql_queries import DatabaseQueryHelper
from fss.settings import DATA_ROOT
from fss.validate_auth import cursor


class RetrieveFilesInDir(object):
    def __init__(self, __dir_key, __client_id):
        self.__dir_key = __dir_key
        self.__client_id = __client_id

    def retrieve_file_list(self):
        __dir_name = self.__dir_key
        if isinstance(self.__dir_key, int):
            __get_dir_name_by_id = DatabaseQueryHelper.GET_DIR_NAME_BY_ID_QUERY % self.__dir_key
            cursor.execute(__get_dir_name_by_id)
            __dir_name = cursor.fetchall()[0][0]
        __dir_path = os.path.join(DATA_ROOT, __dir_name)
        print("Files in " + __dir_name + " directory:")
        print(os.listdir(__dir_path))
