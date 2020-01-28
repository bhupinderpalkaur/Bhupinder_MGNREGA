import sqlite3
from MGNREGA.GPM import Gpm
from MGNREGA.Members import Member
from MGNREGA.bdo import Bdo


def db_connection():
    conn = sqlite3.connect('my_database.sqlite')
    return conn


class login:

    def __init__(self):
        pass

    # Login for BDO.
    @staticmethod
    def test(conn, LOGIN_ID, PASSWORD):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT LOGIN_ID, PASSWORD FROM Admin WHERE LOGIN_ID=? AND PASSWORD=?", (LOGIN_ID, PASSWORD))
        logged_in_admin = cursor_obj.fetchone()
        cursor_obj.close()
        if logged_in_admin is None:
            print("invalid Credentials")
        else:
            print("You logged in as BDO")
        return logged_in_admin

    # Login for GPM
    @staticmethod
    def testgpm(conn, LOGIN, PASSWORD):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT LOGIN_ID, PASSWORD FROM GPM1 WHERE LOGIN_ID=? AND PASSWORD=?", (LOGIN, PASSWORD))
        logged_in_user = cursor_obj.fetchone()
        cursor_obj.close()
        if logged_in_user is None:
            print("invalid Credentials")
        else:
            print("You logged in as GPM")
        return logged_in_user

    # Show Complaints to GPM and BDO
    @staticmethod
    def show_complaint(conn):
        cursor_obj = conn.cursor()
        cursor_obj.execute("SELECT * FROM Complaints")
        showcomplaint = cursor_obj.fetchall()
        cursor_obj.close()
        conn.commit()
        print(showcomplaint)
        return showcomplaint


def bdo():
    conn = db_connection()
    username = take_input()
    password = take_pass()
    user = login.test(conn, username, password)
    return user


def GPM():
    conn = db_connection()
    username = take_input()
    password = take_pass()
    user = login.testgpm(conn, username, password)
    return user


def take_input():
    username = input("Enter Login ID:")
    if not isinstance(username, str) or username == '':
        return take_input()
    else:
        return username


def take_pass():
    password = input("Enter password: ")
    if not isinstance(password, str) or password == '':
        return take_pass()
    else:
        return password


def show_complain():
    conn = db_connection()
    showcomplain = login.show_complaint(conn)
    return showcomplain


def take_id():
    try:
        id = int(input("Enter your ID: "))
        if not isinstance(id, int):
            return take_id()
        else:
            return id
    except ValueError:
        print("Please Input id as number")
        return take_id()

def take_pincode():
    try:
        Pincode = int(input("Enter Your Pincode: "))
        if not isinstance(Pincode, int):
            return take_pincode()
        else:
            return Pincode
    except ValueError:
        print("Please Input Pincode as number")
        return take_pincode()

def take_gpmid():
    try:
        gpmid = int(input("Enter GPM id: "))
        if not isinstance(gpmid, int):
            return take_gpmid()
        else:
            return gpmid
    except ValueError:
        print("Please Input GPM id as number")
        return take_gpmid()

def take_labour():
    try:
        labour = int(input("Enter the labour needed: "))
        if not isinstance(labour, int):
            return take_labour()
        else:
            return labour
    except ValueError:
        print("Please Input number of labour as number")
        return take_labour()

def cost_estimation():
    try:
        cost = int(input("Enter the Cost Estimation: "))
        if not isinstance(cost, int):
            return cost_estimation()
        else:
            return cost
    except ValueError:
        print("Please Input Cost estimation as number")
        return cost_estimation()

def age_member():
    try:
        age = int(input("Enter Age: "))
        if not isinstance(age, int):
            return age_member()
        else:
            return age
    except:
        print("Please Input Age in number")
        return age_member()

def working_days():
    try:
        days = int(input("Enter Working days: "))
        if not isinstance(days, int):
            return working_days()
        else:
            return days
    except:
        print("Please Input Working days in number")
        return working_days()

def take_wage():
    try:
        wage = int(input("Enter Working days: "))
        if not isinstance(wage, int):
            return take_wage()
        else:
            return wage
    except:
        print("Please Input Wage in number")
        return take_wage()

def attendance_member():
    try:
        attendance = int(input("Enter Attendance: "))
        if not isinstance(attendance, int):
            return attendance_member()
        else:
            return attendance
    except:
        print("Please Input Attendance in number")
        return attendance_member()

# Bdo Class functions

def gpm():
    conn = db_connection()
    name = input("Enter the name of GPM: ")
    area = input("Enter the District/State: ")
    pincode = take_pincode()
    bdo = Bdo()
    newgpm = bdo.create_gpm(conn, name, area, pincode)
    return newgpm


def deletegpm():
    conn = db_connection()
    id = take_id()
    Deletegpm = Bdo.delete_gpm(conn, id)
    return Deletegpm


def gpmupdate():
    conn = db_connection()
    name = input("Enter the name of GPM: ")
    area = input("Enter the District/State: ")
    pincode = take_pincode()
    id = take_id()
    bdo = Bdo()
    updategpm = bdo.update_gpm(conn, name, area, pincode, id)
    return updategpm


def gpmshow():
    conn = db_connection()
    showgpm = Bdo.show_gpm(conn)
    return showgpm


def newproject():
    conn = db_connection()
    name = input("Enter the name of Project: ")
    area = input("Enter the area of project: ")
    labour = take_labour()
    cost = cost_estimation()
    start_date = input("Enter the start date: ")
    end_date = input("Enter the end date: ")
    newProject = Bdo.new_project(conn, name, area, labour, cost, start_date, end_date)
    return newProject


def taskapproval():
    conn = db_connection()
    task_approval = "Approval Pending"
    GPMid = take_gpmid()
    approve = Bdo.pendingapprovalTask(conn, task_approval, GPMid)
    return approve


def taskupdate():
    conn = db_connection()
    task_approval = "Approved"
    ID = take_id()
    approved = Bdo.updatetaskapproval(conn, task_approval, ID)
    return approved


def wageapproval():
    conn = db_connection()
    wage_approval = "Approval Pending"
    GPMid = take_gpmid()
    approve1 = Bdo.pendingapprovalWage(conn, wage_approval, GPMid)
    return approve1


def wageupdate():
    conn = db_connection()
    wage_approval = "Approved"
    ID = take_id()
    approval = Bdo.updatewageapproval(conn, wage_approval, ID)
    return approval


def membershow():
    conn = db_connection()
    ID = take_id()
    show = Bdo.showmember(conn, ID)
    return show


# GPM Class Functions

def updateproject():
    conn = db_connection()
    labour = take_labour()
    name = input("Enter the name of Project: ")
    update_project = Gpm.update_project(conn, labour, name)
    return update_project


def createmember():
    conn = db_connection()
    name = input("Enter the name of Member: ")
    area = input("Enter the District/State: ")
    pincode = take_pincode()
    age = age_member()
    workingdays = working_days()
    wage = take_wage()
    attendance = attendance_member()
    Projectalloted = input("Enter name of the project: ")
    gender = input("Enter the gender: ")
    TaskApproval = "Approval Pending"
    WageApproval = "Approval Pending"
    gpmid = take_gpmid()
    newmember = Gpm.create_member(conn, name, area, pincode, age, workingdays, wage, attendance, Projectalloted,
                                  gender, TaskApproval, WageApproval, gpmid)
    return newmember


def jobcard():
    conn = db_connection()
    name = input("Enter the name of Member: ")
    Projectalloted = input("Enter name of the project: ")
    jobdetails = Gpm.jobCard(conn, name, Projectalloted)
    return jobdetails


def gpmid():
    conn = db_connection()
    Name = input("Enter Your Name: ")
    showid = Gpm.gpm_id(conn, Name)
    return showid


# Member Class Functions

def issuecomp():
    conn = db_connection()
    Name = input("Enter Your Name: ")
    id = take_id()
    issue = input("Write your complaint: ")
    com = Member.complaints(conn, Name, id, issue)
    return com


def wage():
    conn = db_connection()
    id = take_id()
    gpmid = take_gpmid()
    wage = Member.ShowWage(conn, id, gpmid)
    return wage


if __name__ == "__main__":
    s = ''
    while 1:
        print("\t1. Login as BDO")
        print("\t2. Login as GPM")
        print("\t3. Login as Member")
        s = input()
        if s == "1":
            bdo = bdo()
            ch = bdo
            while ch != None:
            # system("cls");
                print("\tMAIN MENU")
                print("\t1. Create GPM")
                print("\t2. Delete GPM")
                print("\t3. Update GPM")
                print("\t4. Show GPM")
                print("\t5. Create new Project")
                print("\t6. Pending Task Approvals")
                print("\t7. Pending Wage Approvals")
                print("\t8. Show members")
                print("\t9. Show complaints")
                print("\t10. Exit")
                print("\tSelect Your Option (1-10) ")
                ch = input()
                if ch == "1":
                    gpm = gpm()
                elif ch == "2":
                    delete = deletegpm()
                elif ch == "3":
                    update = gpmupdate()
                elif ch == "4":
                    show = gpmshow()
                elif ch == "5":
                    project = newproject()
                elif ch == "6":
                    pendingtask = taskapproval()
                    if not pendingtask:
                        print("All the tasks are approved")
                    i = pendingtask
                    while i != []:
                        print("\t1. To approve the task assigned click 1")
                        print("\t2. Exit")
                        i = input()
                        if i == "1":
                            updatetask = taskupdate()
                            break
                        else:
                            break
                elif ch == "7":
                    wageapproval = wageapproval()
                    if wageapproval == []:
                        print("wage for all members are approved")
                    i = wageapproval
                    while i != []:
                        print("\t1. To approve the Wage click 1")
                        print("\t2. Exit")
                        i = input()
                        if i == "1":
                            updatewage = wageupdate()
                            break
                        else:
                            break
                elif ch == "8":
                    member = membershow()
                elif ch == "9":
                    comp = show_complain()
                elif ch == "10":
                    break
                else:
                    print ("INVALID")
            break
        elif s == "2":
            gpm1 = GPM()
            n = gpm1
            while n != None:
                # system("cls");
                print("\t\n\n MAIN MENU")
                print("\t1. Update Project")
                print("\t2. Create Member")
                print("\t3. Job Card")
                print("\t4. Show members")
                print("\t5. Show GPM ID")
                print("\t6. Show complaints")
                print("\t7. Exit")
                n = input()
                if n == "1":
                    update = updateproject()
                    break
                elif n == "2":
                    membercreate = createmember()
                    break
                elif n == "3":
                    member = jobcard()
                    print("Job card")
                    print(member)
                    break
                elif n == "4":
                    member = membershow()
                elif n == "5":
                    id = gpmid()
                elif n == "6":
                    comp = show_complain()
                elif n == "7":
                    break
            break
        elif s == "3":
            member = jobcard()
            print(member)
            c = member
            while c != None:
                print("\tMAIN MENU")
                print("\t1. Show wage")
                print("\t2. File complaint")
                c = input()
                if c == "1":
                    wage()
                    break
                elif c == "2":
                    complaint = issuecomp()
            break
        else:
            print("INVALID")
