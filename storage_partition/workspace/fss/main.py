import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
PROJ_ROOT = os.path.abspath(os.path.join(APP_ROOT, ".."))
CONF_ROOT = os.path.join(APP_ROOT, 'config')
DATA_ROOT = os.path.join(APP_ROOT, 'data')

from fss.directory.retrieve_dir import RetrieveDir
from fss.file.remove_file import RemoveFile
from fss.file.retrieve_file import RetrieveFile
from fss.file.retrieve_files_in_dir import RetrieveFilesInDir
from fss.storage.storage_quota import StorageQuota
from fss.validate_auth.main import auth_main
from fss.directory.create_directory import CreateDirectory
from fss.file.store_file import CreateFile
from fss.helper.conf_reader import get_conf_value


def main():
    __try_count = int(get_conf_value("accessibility", "auth_try_count"))
    if __try_count > 0:
        __client_id = auth_main()
        __storage = StorageQuota(__client_id)
        __storage.dir_size()
    else:
        print("Please provide proper try_count value.")
        print("Terminated.")
        exit()
    while True:
        print("Please enter any of the following option:")
        print("=" * 40)
        print("Enter 1 To create directory.")
        print("Enter 2 to create file.")
        print("Enter 3 to remove a file.")
        print("Enter 4 to retrieve file content.")
        print("Enter 5 to list files in a directory.")
        print("Enter 6 to get list of directories.")
        print("Enter 7 to exit.")
        value = input("Enter your choice:\n")
        if int(value) == 1:
            dir_name = input("Enter directory name to be created...\n")
            create_dir = CreateDirectory(dir_name, __client_id)
            create_dir.create_dir()
            create_dir.insert_db()
        elif int(value) == 2:
            create_file = CreateFile(__client_id)
            create_file.get_dir_list()
        elif int(value) == 3:
            __dir_key = input("Enter directory name/id.\n")
            __file_key = input("Enter file name/id.\n")
            remove_file = RemoveFile(__dir_key, __file_key, __client_id)
            remove_file.remove_files()
        elif int(value) == 4:
            __dir_key = input("Enter directory name/id.\n")
            __file_key = input("Enter file name/id.\n")
            remove_file = RetrieveFile(__dir_key, __file_key, __client_id)
            remove_file.retrieve_files()
        elif int(value) == 5:
            __dir_key = input("Enter directory name/id.\n")
            file_list = RetrieveFilesInDir(__dir_key, __client_id)
            file_list.retrieve_file_list()
        elif int(value) == 6:
            retrieve_dir = RetrieveDir(__client_id)
            retrieve_dir.retrieve_directory_list()
        elif int(value) == 7:
            print("Terminated.")
            exit()
        else:
            print("Wrong input, please select once again. \n")

if __name__ == '__main__':
    main()
