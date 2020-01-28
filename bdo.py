
class Bdo:

    # Create GPM
    @staticmethod
    def create_gpm(conn, Name, Area, PinCode):
        cursor_obj = conn.cursor()
        cursor_obj.execute('''INSERT INTO GPM(Name,Area,PinCode) VALUES(?,?,?)''', (Name, Area, PinCode,))
        cursor_obj.execute("SELECT * FROM GPM WHERE rowid=?", (cursor_obj.lastrowid,))
        newGPM = cursor_obj.fetchone()
        print ("\n\n New GPM created successfully")
        print(newGPM)
        conn.close()
        return newGPM

    # Delete GPM
    @staticmethod
    def delete_gpm(conn, ID):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT * FROM GPM WHERE id=?", (ID, ))
        gpm = cursor_obj.fetchone()
        print(gpm)
        cursor_obj.execute("DELETE from GPM where id=?", (ID, ))
        conn.commit()
        conn.close()
        print("\n\n GPM Deleted successfully")


    # Update GPM
    @staticmethod
    def update_gpm(conn, Name, Area, PinCode, ID):
        cursor_obj = conn.cursor()
        cursor_obj.execute('''UPDATE GPM SET Name=?, Area=?,PinCode=? where ID=?''', (Name, Area, PinCode, ID))
        cursor_obj.execute("SELECT * FROM GPM WHERE id=?", (ID, ))
        conn.commit()
        updateGPM = cursor_obj.fetchone()
        print(updateGPM)
        conn.close()
        print ("\n\n Updated Successfully")
        return updateGPM

    # Shows GPM table
    @staticmethod
    def show_gpm(conn):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT * FROM GPM")
        showGPM = cursor_obj.fetchall()
        cursor_obj.close()
        conn.commit()
        print (showGPM)
        return (showGPM)

    # Create New Project
    @staticmethod
    def new_project(conn, Name, Area, Labour, Cost, Start_date, End_date):
        cursor_obj = conn.cursor()
        cursor_obj.execute('''INSERT INTO PROJECT(Name,Area,Labour,CostEstimated,StartDate,EndDate) VALUES(?,?,?,?,?,?)''',
            (Name, Area, Labour, Cost, Start_date, End_date,))
        cursor_obj.execute("SELECT * FROM PROJECT WHERE rowid=?", (cursor_obj.lastrowid,))
        newproject = cursor_obj.fetchone()
        print(newproject)
        print ("\n\n New Project created successfully")
        cursor_obj.close()
        conn.commit()
        return newproject

     # Pending Task Approvals.
    @staticmethod
    def pendingapprovalTask(conn, TaskApproval, GPMid):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT Name, Area, TaskApproval, ID FROM member WHERE TaskApproval=? AND GPMid=?", (TaskApproval,GPMid))
        approval = cursor_obj.fetchall()
        cursor_obj.close()
        conn.commit()
        print (approval)
        return approval

    # Update Task Approvals
    @staticmethod
    def updatetaskapproval(conn, TaskApproval, ID):
        cursor_obj = conn.cursor()
        cursor_obj.execute('''UPDATE member SET TaskApproval=? where ID=?''', (TaskApproval, ID))
        cursor_obj.execute("SELECT * FROM member WHERE id=?", (ID,))
        conn.commit()
        updatetask = cursor_obj.fetchone()
        print ("\n\n Updated Successfully")
        print(updatetask)
        conn.close()
        return updatetask

    # Show Pending wage Approvals
    @staticmethod
    def pendingapprovalWage(conn, WageApproval, GPMid):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT Name, Area, WageApproval, ID FROM member WHERE WageApproval=? AND GPMid=?", (WageApproval,GPMid))
        approval1 = cursor_obj.fetchall()
        cursor_obj.close()
        conn.commit()
        print (approval1)
        return approval1

    # Update pending wage Approvals
    @staticmethod
    def updatewageapproval(conn, WageApproval, ID):
        cursor_obj = conn.cursor()
        cursor_obj.execute('''UPDATE member SET WageApproval=? where ID=?''', (WageApproval, ID))
        cursor_obj.execute("SELECT * FROM member WHERE id=?", (ID,))
        conn.commit()
        updatewage = cursor_obj.fetchone()
        print(updatewage)
        print ("\n\n Updated Successfully")
        cursor_obj.close()
        conn.commit()
        return updatewage

    # Show members for a Particular GPM ID
    @staticmethod
    def showmember(conn, ID):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT * FROM member WHERE GPMid=?", (ID,))
        approval = cursor_obj.fetchall()
        cursor_obj.close()
        conn.commit()
        print (approval)
        return approval