import pytest
from datetime import datetime


class TestDb:

    def test_db_operations(self,db_connection):
        insert_sql = "INSERT INTO crypto.test VALUES ('test', 3)"
        update_sql = "UPDATE crypto.test SET test_number = 4 WHERE test_number <> 4"
        delete_sql = "DELETE FROM crypto.test WHERE test_number = 4"
        insert_ret_sql = "INSERT INTO crypto.test VALUES ('test', 3)"

        statusmessage, query = db_connection.execute_db(insert_sql)
        assert statusmessage[-1] != '0'
        assert query == insert_sql.encode('utf-8')

        statusmessage, query = db_connection.execute_db(update_sql)
        print(statusmessage)
        assert statusmessage[-1] != '0'
        assert query == update_sql.encode('utf-8')

        statusmessage, query = db_connection.execute_db(delete_sql)
        assert statusmessage[-1] != '0'
        assert query == delete_sql.encode('utf-8')

        r_value = 'test_date'
        statusmessage, query, returned_value = db_connection.insert_returning(insert_ret_sql, r_value)
        insert_ret_sql = f"{insert_ret_sql} RETURNING {r_value}"
        now = datetime.now()
        assert statusmessage[-1] != '0'
        assert query == insert_ret_sql.encode('utf-8')
        assert returned_value.strftime("%Y-%m-%d") == now.strftime("%Y-%m-%d")