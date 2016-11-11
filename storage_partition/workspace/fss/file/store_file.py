import os
import shutil
from fss.helper.sql_queries import DatabaseQueryHelper
from fss.validate_auth import cursor
from fss.settings import DATA_ROOT
from fss.directory.create_directory import CreateDirectory


class CreateFile(object):
    def __init__(self, client_id):
        self.__client_id = int(client_id)
        self.__get_dir_name = ''
        self.__is_created = False

    def get_dir_list(self):
        get_dir_list_query = DatabaseQueryHelper.GET_DIR_LIST_QUERY % self.__client_id
        cursor.execute(get_dir_list_query)
        dir_list = cursor.fetchall()
        print("Your directory list: ")
        for dir_name in dir_list:
            print(dir_name[0])
        self.__get_dir_name = input("Enter directory name to store file...\n")
        if os.path.exists(os.path.join(DATA_ROOT, self.__get_dir_name)):
            self.__store_file()
        else:
            print("Directory does not exit.")
            dir_choice = input("Do you want to create a new one (y/n)?\n")
            if dir_choice.lower() == 'y':
                dir_obj = CreateDirectory(self.__get_dir_name, self.__client_id)
                dir_obj.create_dir()
                dir_obj.insert_db()

    def __store_file(self):
        input_file_path = input("Enter file path to make copy... \n")
        __is_valid_size = self.__check_file_size(input_file_path)
        if __is_valid_size:
            file_name = input("Enter new name for this file... \n")
            __is_file_exist = self.__check_file_exist(file_name, self.__client_id)
            if __is_file_exist is False:
                if os.path.isfile(input_file_path):
                    shutil.copyfile(input_file_path, os.path.join(DATA_ROOT, self.__get_dir_name, file_name))
                    self.__is_created = True
                if self.__is_created:
                    self.__insert_db(file_name)
            else:
                shutil.copyfile(input_file_path, os.path.join(DATA_ROOT, self.__get_dir_name, file_name))
                print("File overridden.")
                print("*" * 40)
        else:
            print("Please insert a file of lesser size.")
            print("*" * 40)

    def __insert_db(self, __file_name):
        if self.__is_created:
            insert_query = DatabaseQueryHelper.INSERT_T_FILE_QUERY % (__file_name, self.__client_id)
            cursor.execute(insert_query)
            cursor.execute(DatabaseQueryHelper.GET_FILE_ID_QUERY)
            file_id = str(cursor.fetchall()[0][0])
            print("File stored successfully.")
            print("Your unique file id is:", file_id)

    def __check_file_exist(self, __file_name, __client_id):
        __is_file_exist = False
        __get_file_name_query = DatabaseQueryHelper.GET_FILE_NAME_QUERY % __client_id
        cursor.execute(__get_file_name_query)
        get_file_name_list = cursor.fetchall()
        for name in get_file_name_list:
            if name[0] == __file_name:
                __is_file_exist = True
        return __is_file_exist

    def __check_file_size(self, __file_path):
        __file_size = os.path.getsize(__file_path)
        if __file_size <= 10000000:
            return True
        else:
            return False
