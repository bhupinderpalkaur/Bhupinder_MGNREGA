import unittest

import mock

from MGNREGA.Admin_login import *


class Testadmin(unittest.TestCase):

# Admin login.
    @mock.patch('Admin_login.db_connection')
    @mock.patch('Admin_login.login.test', return_value=('admin', 'admin'))
    @mock.patch('builtins.input', side_effect=["admin", "admin"])
    def test_bdo(self, mock_input, mock_test, mock_db_conn):

        result = bdo()

        self.assertEqual(result, ('admin', 'admin'))

# GPM login
    @mock.patch('Admin_login.db_connection')
    @mock.patch('Admin_login.login.testgpm', return_value=('GPM', 'GPM'))
    # @mock.patch('builtins.input', side_effect=["GPM", "GPM"])
    def testgpm_GPM(self, mock_test, mock_db_conn):
        result = GPM()

        self.assertEqual(result, ('GPM', 'GPM'))

# Show complaints
    @mock.patch('Admin_login.db_connection')
    @mock.patch('Admin_login.login.show_complaint', return_value=[('aa', '1', 'sdwwedf'), ('aa', '2', 'water is not good')])
    def testcomplaint_show_complain(self, mock_test, mock_db_conn):
        result = show_complain()

        self.assertEqual(result, [('aa', '1', 'sdwwedf'), ('aa', '2', 'water is not good')])



