import unittest

import mock

from MGNREGA.Admin_login import *

class TestMember(unittest.TestCase):

# Show wage.
    @mock.patch('Admin_login.db_connection')
    @mock.patch('Admin_login.login.test', return_value=[(300, 3)])
    @mock.patch('builtins.input', side_effect=[1, 1])
    def test_ShowWage(self, mock_input, mock_test, mock_db_conn):

        result= wage()

        self.assertEqual(result,[(300, 3)] )