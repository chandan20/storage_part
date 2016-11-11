from fss.helper.sql_queries import DatabaseQueryHelper
from fss.validate_auth.validate import Validate
from fss.validate_auth import cursor


def auth_main():
    validate = Validate(cursor, DatabaseQueryHelper.GET_CLIENT_ID_QUERY)
    return validate.get_id_token()

if __name__ == '__main__':
    auth_main()
