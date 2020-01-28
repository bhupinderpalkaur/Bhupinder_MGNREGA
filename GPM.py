class Gpm:
    # Update members in the project.
    @staticmethod
    def update_project(conn, Labour, Name):
        cursor_obj = conn.cursor()
        cursor_obj.execute('''UPDATE PROJECT SET Labour=? where Name=?''', (Labour, Name))
        updateproject = cursor_obj.lastrowid
        cursor_obj.close()
        conn.commit()
        return updateproject

    # Create a new Member
    @staticmethod
    def create_member(conn, Name, Area, PinCode, Age, workingdays, wagecomputation, attendancecalculation,
                      Projectalloted, gender, TaskApproval, WageApproval, GPMid):
        cursor_obj = conn.cursor()
        cursor_obj.execute(
            '''INSERT INTO member(Name,Area,PinCode,Age,workingdays,wagecomputation,attendancecalculation,Projectalloted,gender,TaskApproval,WageApproval,GPMid) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',
            (Name, Area, PinCode, Age, workingdays, wagecomputation, attendancecalculation, Projectalloted, gender,
             TaskApproval, WageApproval, GPMid))
        newmember = cursor_obj.lastrowid
        print ("\n\n New Member created successfully")
        cursor_obj.close()
        conn.commit()
        return newmember

    # Issue Job Card
    @staticmethod
    def jobCard(conn, Name, Projectalloted):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT Name,Area,Age,gender FROM member WHERE Name=? AND Projectalloted=?",
                           (Name, Projectalloted))
        jobcard = cursor_obj.fetchone()
        cursor_obj.close()
        if jobcard == None:
            print("invalid Credentials")
        return jobcard

    # Show GPM id
    @staticmethod
    def gpm_id(conn, Name):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT id FROM GPM WHERE Name=?", (Name,))
        gpmid = cursor_obj.fetchall()
        cursor_obj.close()
        conn.commit()
        print(gpmid)
        return gpmid