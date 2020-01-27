class Member:

    # File Complaint
    @staticmethod
    def complaints(conn, Name, id, issue):
        cursor_obj = conn.cursor()
        cursor_obj.execute('''INSERT INTO Complaints(MemberName,MemberId,Issue) VALUES(?,?,?)''', (Name, id, issue))
        complaint = cursor_obj.lastrowid
        print ("\n\n Your Complaint is registered")
        cursor_obj.close()
        conn.commit()
        return complaint

    @staticmethod
    def ShowWage(conn, id, GPMid):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT wagecomputation,attendancecalculation FROM member WHERE id=? AND GPMid=?",
                           (id, GPMid))
        wage = cursor_obj.fetchall()
        if wage == []:
            print("Nothing to show for these details")
        else:
            print (wage)
        cursor_obj.close()
        conn.commit()
        return wage