from fss.helper.sql_queries import DatabaseQueryHelper
from fss.validate_auth import cursor


class RetrieveDir(object):
    def __init__(self, __client_id):
        self.__client_id = __client_id

    def retrieve_directory_list(self):
        get_directory_list_query = DatabaseQueryHelper.GET_DIRECTORY_LIST_QUERY % self.__client_id
        cursor.execute(get_directory_list_query)
        directory_list = cursor.fetchall()
        print("List of directories: ")
        for val in directory_list:
            print(val[0])
