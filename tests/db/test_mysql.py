import unittest
import mock
from datalib.db.mysql import MySql, MySqlConfig

from pymysql.connections import Connection
from pymysql.cursors import Cursor

class TestMySql(unittest.TestCase):
    @mock.patch("datalib.db.mysql.pymysql")
    def test_conn(self, pymysql_mock):
        config = {
                "host": "host",
                "user": "foo",
                "passwd": "password",
                "db": "dbname",
                "port": 3306
                }

        connection = mock.Mock()
        pymysql_mock.connect.return_value = connection

        cursor_mock = mock.Mock()
        connection.cursor.return_value = cursor_mock

        with MySql(config) as client:
            self.assertEqual(type(client), MySql)
            self.assertEqual(client.config, config)

        with MySql(config).conn() as conn:
            self.assertEqual(conn, connection)

        pymysql_mock.connect.assert_called_with(**config)

        with MySql(config).cursor() as cursor:
            self.assertEqual(cursor, cursor_mock)
