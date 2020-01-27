import unittest

import mock

from MGNREGA.Admin_login import *

class Testgpm(unittest.TestCase):

#Show Job Card
    @mock.patch('Admin_login.db_connection')
    @mock.patch('GPM.Gpm.jobCard', result_value=('aa', 'aa', 21, 'male'))
    def test_jobCard(self, mock_test, mock_db_conn):
        result = jobcard()

        self.assertEqual(result, ('aa', 'aa', 21, 'male'))

#Show GPM id.
    @mock.patch('Admin_login.db_connection')
    @mock.patch('GPM.Gpm.gpm_id', result_value=[(13,)])
    def test_gpm_id(self, mock_test, mock_db_conn):
        result = gpmid()

        self.assertEqual(result, [(13,)])

#Update project
    @mock.patch('Admin_login.db_connection')
    @mock.patch('GPM.Gpm.update_project', result_value=(20, 'Road Construction'))
    @mock.patch('builtins.input', side_effect=["20", "Road Construction"])
    def test_update_project(self, mock_inout, mock_test, mock_db_conn):
        result = updateproject()

        self.assertEqual(result, (20, 'Road Construction'))

