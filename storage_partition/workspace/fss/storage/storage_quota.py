import os
from fss.helper.sql_queries import DatabaseQueryHelper
from fss.settings import DATA_ROOT
from fss.validate_auth import cursor


class StorageQuota(object):
    def __init__(self, __client_id):
        self.__client_id = __client_id

    def dir_size(self):
        __total_size = 0
        get_directory_list_query = DatabaseQueryHelper.GET_DIRECTORY_LIST_QUERY % self.__client_id
        cursor.execute(get_directory_list_query)
        directory_list = cursor.fetchall()
        for val in directory_list:
            dir_path = os.path.join(DATA_ROOT, val[0])
            for file in os.listdir(dir_path):
                __total_size += os.path.getsize(os.path.join(dir_path, file))
        __total_size /= 1000000000
        if __total_size > 1:
            print("Storage size exceeded.")
            print("Delete some data before processing.")
            print("Terminated.")
            exit()
