import unittest

import mock

from MGNREGA.Admin_login import *

class Testbdo(unittest.TestCase):

#Show GPM Data
#   @mock.patch('Admin_login.db_connection')
    @mock.patch('bdo.Bdo.show_gpm', return_value=[('Bhupinder', 'Patiala', 140401, 13), ('Nishant', '1404011', 1233, 22), ('bhupinder', 'rajpura', 140401, 23), ('aaaaa', 'aaaaaaaa', 123456, 24), ('John', 'Koramangala', 560034, 25), ('John', 'Koramangala 1st block', 560034, 26), ('John', 'Koramangala', 560034, 27), ('John', 'Koramangala', 560034, 28)])
    def test_show_gpm(self, mock_test):
        result = gpmshow()

        self.assertEqual(result, [('Bhupinder', 'Patiala', 140401, 13), ('Nishant', '1404011', 1233, 22), ('bhupinder', 'rajpura', 140401, 23), ('aaaaa', 'aaaaaaaa', 123456, 24), ('John', 'Koramangala', 560034, 25), ('John', 'Koramangala 1st block', 560034, 26), ('John', 'Koramangala', 560034, 27), ('John', 'Koramangala', 560034, 28)]
)

# Show Pending Task Approval
    @mock.patch('Admin_login.db_connection')
    @mock.patch('bdo.Bdo.pendingapprovalTask', [('asas', 'as', 'Approval Pending', 4)])
    @mock.patch('builtins.input', side_effect=[3])
    def test_taskapproval(self, mock_test, mock_input):
        result = taskapproval()

        self.assertEqual(result, [('asas', 'as', 'Approval Pending', 4)])

# Show Pending wage Approval
    @mock.patch('Admin_login.db_connection')
    @mock.patch('bdo.Bdo.pendingapprovalWage', return_value=[('asas', 'as', 'Approval Pending', 4), ('as', 'sa', 'Approval Pending', 6)])
    @mock.patch('builtins.input', side_effect=[3])
    def test_pendingapprovalWage(self, mock_input, mock_test, mock_db_conn):
        result = wageapproval()

        self.assertEqual(result, [('asas', 'as', 'Approval Pending', 4), ('as', 'sa', 'Approval Pending', 6)])

# Show member
#     @mock.patch('Admin_login.db_connection')
    @mock.patch('bdo.Bdo.showmember', return_value=[('swd', 'dw', 2, 22, 23, 32, 32, 'd', 'we', 2, 'Approved', 'Approved', 2), ('aaaaa', 'ass', 123, 3, 33, 33, 2, 'ddeede', 'sa', 3, 'Approved', 'Approved', 2), ('aaaa', 'sas', 21, 21, 21, 21, 21, 'sqq', 'sq', 5, 'Approved', 'Approved', 2)])
    @mock.patch('builtins.input', side_effect=[2])
    def test_showmember(self, mock_input, mock_test):
        result = membershow()

        self.assertEqual(result, [('swd', 'dw', 2, 22, 23, 32, 32, 'd', 'we', 2, 'Approved', 'Approved', 2), ('aaaaa', 'ass', 123, 3, 33, 33, 2, 'ddeede', 'sa', 3, 'Approved', 'Approved', 2), ('aaaa', 'sas', 21, 21, 21, 21, 21, 'sqq', 'sq', 5, 'Approved', 'Approved', 2)])

# Create GPM
#     @mock.patch('Admin_login.db_connection')
    @mock.patch('bdo.Bdo.create_gpm', return_value=('John', 'Koramangala', 560034))
    @mock.patch('builtins.input', side_effect=("John", "Koramangala", 560034))
    def test_create_gpm(self, mock_input, mock_test):
        result = gpm()

        self.assertEqual(result, ('John', 'Koramangala', 560034))

# # Delete GPM
#
#     @mock.patch('Admin_login.db_connection')
#     @mock.patch('bdo.Bdo.delete_gpm', return_value=('John', 'Koramangala', 560034, 26))
#     @mock.patch('builtins.input', side_effect=('26'))
#     def test_delete_gpm(self, mock_input, mock_test, mock_db_conn):
#         result = deletegpm()
#
#         self.assertEqual(result, ('John', 'Koramangala', 560034, 26))

# Update GPM

    # @mock.patch('Admin_login.db_connection')
    @mock.patch('bdo.Bdo.update_gpm', return_value=('John', 'Koramangala 1st block', 560034, 26))
    @mock.patch('builtins.input', side_effect=("John", "Koramangala 1st block", 560034, 26))
    def test_create_gpm(self, mock_input, mock_test):
        result = gpmupdate()

        self.assertEqual(result, ('John', 'Koramangala 1st block', 560034, 26))

# Create New Project
#   @mock.patch('Admin_login.db_connection')
    @mock.patch('bdo.Bdo.new_project', return_value=('Road Construction', 'Koramangala 1st block', 20, 26000, 22, 29))
    @mock.patch('builtins.input', side_effect=("Road Construction", "Koramangala 1st block", 20, 26000, 22, 29))
    def test_new_project(self, mock_input, mock_test):
        result = newproject()

        self.assertEqual(result, ('Road Construction', 'Koramangala 1st block', 20, 26000, 22, 29))

# Update Pending task Approval  @mock.patch('Admin_login.db_connection')
#     @mock.patch('Admin_login.db_connection')
    @mock.patch('bdo.Bdo.updatetaskapproval', return_value= ('aaaa', 'sas', 21, 21, 21, 21, 21, 'sqq', 'sq', 5, 'Approved', 'Approved', 2))
    @mock.patch('builtins.input', side_effect=[5])
    def test_updatetaskapproval(self, mock_input, mock_test):
        result = taskupdate()

        self.assertEqual(result,  ('aaaa', 'sas', 21, 21, 21, 21, 21, 'sqq', 'sq', 5, 'Approved', 'Approval Pending', 2))

# Update Pending Wage Approval

    # @mock.patch('Admin_login.db_connection')
    @mock.patch('bdo.Bdo.updatetaskapproval', return_value= ('aaaa', 'sas', 21, 21, 21, 21, 21, 'sqq', 'sq', 5, 'Approved', 'Approved', 2))
    @mock.patch('builtins.input', side_effect=[5])
    def test_updatetaskapproval(self, mock_input, mock_test):
        result = taskupdate()

        self.assertEqual(result, ('aaaa', 'sas', 21, 21, 21, 21, 21, 'sqq', 'sq', 5, 'Approved', 'Approved', 2)
)