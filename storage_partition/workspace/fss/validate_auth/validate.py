from fss.helper.sql_queries import DatabaseQueryHelper
from fss.helper.conf_reader import get_conf_value


class Validate(object):
    def __init__(self, cursor, query):
        self.__cursor = cursor
        self.__sql_get_query = query

    def get_id_token(self):
        __is_verified = False
        __try_count = int(get_conf_value("accessibility", "auth_try_count"))
        while __is_verified is False and __try_count >= 1:
            __client_id = input("Please provide id...\n")
            __auth_token = input("Please provide token...\n")
            self.__cursor.execute(DatabaseQueryHelper.GET_CLIENT_ID_QUERY)
            db_client_id = self.__cursor.fetchall()
            self.__cursor.execute(DatabaseQueryHelper.GET_AUTH_TOKEN_QUERY)
            db_auth_token = self.__cursor.fetchall()
            for str_id, token in zip(db_client_id, db_auth_token):
                if str(str_id[0]) == __client_id and token[0] == __auth_token:
                    __is_verified = True
            if __is_verified:
                print("Successfully verified.")
                print("*" * 40)
                return __client_id
            else:
                __try_count -= 1
                if __try_count > 0:
                    print("Incorrect details, please try again.")
                    print("Remaining attempt: ", __try_count)
                    print("*" * 40)
                else:
                    print("Terminated.")
                    exit()
