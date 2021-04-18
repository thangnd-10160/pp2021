Students = []
StudentID = []
Courses = []
CoursesID = []
Mark = []

def numstudent():
    stu = int(input("Let's enter the numbers of Student:"))
    if stu > 0:
        return stu
    else:
        print("Should stop!!!")
        return 0

def infStudent():
    print("Enter the information of student")
    inf = {
        'ID ': '',
        'Name': '',
        'DOB': ''
    }
    print("Enter the ID of Student:")
    inf['s_ID'] = s_Id = input()
    print("Enter the name of Student:")
    inf['Name'] = input()
    print("Enter date of brith of Student:")
    inf['DOB'] = input()
    Students.append(inf)
    StudentID.append(s_Id)

def numcourses():
    cou = int(input("Let's enter the numbers of course:"))
    if cou > 0:
        return cou
    else:
        print("Should stop!!!")
        return 0

def infCourses():
    print("Enter the information of courses")
    inf_C = {
        'cID': '',
        'Name': ''
    }
    print("Enter the ID of Courses:")
    inf_C['c_ID'] = c_Id = input()
    print("Enter the name of Courses:")
    inf_C['Name'] = input()
    Courses.append(inf_C)
    CoursesID.append(c_Id)

def infmark():
    print("Enter the point mark")
    inf_M = {
        'c_ID': '',
        's_ID': '',
        'Mark': ''
    }
    print("Enter the ID of Courses: ")
    inf_M['c_ID'] = c = input()
    if c in CoursesID:
        print("Enter the ID of Student:")
        inf_M['s_ID'] = c1 = input()
        if c1 in StudentID:
            print("Enter marks of that Student:")
            inf_M['Mark'] = float(input())
        else:
            return -1
    else:
        return -1
    Mark.append(inf_M)

def ShowCourse():
    print("Show the lists of courses:")
    for a in range(0, len(Courses)):
        print("[", Courses[a]['c_ID'], "]", "[", Courses[a]['Name'], "]", )


def ShowStudent():
    print("Show the lists of Student:")
    for a in range(0, len(Students)):
        print("[", Students[a]['s_ID'], "]", "[", Students[a]['Name'], "]", "[", Students[a]['DOB'], "]", )


def ShowMark():
    print("Show marks of Student in courses:")
    for a in range(len(Students)):
        print("[", Mark[a]['c_ID'], "]", "[", Mark[a]['s_ID'], "]", "[", Mark[a]['Mark'], "]", )

def Student_Management():
    cou = numcourses()
    stu = numstudent()
    for i in range(cou):
        infCourses()
        for i in range(stu):
            infStudent()
            infmark()
            ShowCourse()
            ShowStudent()
            ShowMark()
    print("Done")

Student_Management()