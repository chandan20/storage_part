import os
from fss.helper.sql_queries import DatabaseQueryHelper
from fss.settings import DATA_ROOT
from fss.validate_auth import cursor


class RemoveFile(object):
    def __init__(self, __dir_key, __file_key, __client_id):
        self.__dir_key = __dir_key
        self.__file_key = __file_key
        self.__client_id = __client_id

    def remove_files(self):
        self.__show_dir_id_name()
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
        __remove_file = DatabaseQueryHelper.REMOVE_FILE_QUERY % self.__file_key
        cursor.execute(__remove_file)
        os.remove(os.path.join(DATA_ROOT, __dir_name, __file_name))
        print("File removed successfully.")

    def __show_dir_id_name(self):
        get_dir_id_name = DatabaseQueryHelper.GET_DIR_ID_NAME_QUERY % self.__client_id
        cursor.execute(get_dir_id_name)
        get_dir_id_name_vals = cursor.fetchall()
        print("Your directory and directory id: ")
        print("dir_name" + "\t" + "dir_id")
        print("*" * 8 + "\t" + "*" * 6)
        for val in get_dir_id_name_vals:
            print(val[0] + "\t\t" + str(val[1]))
