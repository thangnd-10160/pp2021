Students = []
StudentID = []
Courses = []
CoursesID = []
Mark = []

class Student_s:
    def __init__(self, s_id, name, dob):
        self.a=s_id
        self.b=name
        self.c=dob
        Students.append(self)
        StudentID.append(self.a)
    def get_id(self):
        return self.a
    def get_name(self):
        return self.b
    def get_dob(self):
        return self.c

class Course_s:
    def __init__(self, c_id, name):
        self.d=c_id
        self.e=name
        Courses.append(self)
        Courses.append(self.d)
    def get_id(self):
        return self.d
    def get_name(self):
        return self.e

class Marks:
    def __init__(self, s_id, c_id, mark):
        self.f=s_id
        self.g=c_id
        self.h=mark
        Mark.append(self)
    def get_a(self):
        return self.f
    def get_b(self):
        return self.g
    def get_mark(self):
        return self.h

def numstudent():
    stu = int(input("Let's enter the numbers of Student:"))
    if stu > 0:
        return stu
    else:
        print("Should stop!!!")
        return 0

def infStudent():
    print("Enter the information of student")
    s_id = input("Enter the ID of Student:")
    name = input("Enter the name of Student:")
    dob = input("Enter date of birth of Student:")
    inf_s = {
        's_id': s_id,
        'name': name,
        'dob': dob
    }

    Students.append(inf_s)
    StudentID.append(s_id)

def numcourses():
    cou = int(input("Let's enter the numbers of course:"))
    if cou > 0:
        return cou
    else:
        print("Should stop!!!")
        return 0

def infCourses():
    print("Enter the information of courses")
    c_id = input("Enter the ID of Courses:")
    name = input("Enter the name of Courses:")
    inf_c = {
        'c_id': c_id,
        'name': name
    }

    Courses.append(inf_c)
    CoursesID.append(c_id)

def marks():
    i = 1
    mk = len(Students)
    while i <= mk:
        i += 1
        s_id = input("Enter the ID of Student:")
        if s_id in StudentID:
            for i in range(0, len(Courses)):
                c_id = input("Enter the ID of Courses")
                if c_id in CoursesID:
                    mark = float(input("Enter marks of that Student:"))
                    inf_m = {
                        's_id': s_id,
                        'c_id': c_id,
                        'mark': mark
                    }
                else:
                    print("should stop")
                    break
                Mark.append(inf_m)
        else:
            print("should stop")
            break

def ShowCourse():
    print("Show the lists of courses:")
    for a in range(0, len(Courses)):
        print("[", Courses[a]['c_id'], "]", "[", Courses[a]['name'], "]", )

def ShowStudent():
    print("Show the lists of Student:")
    for a in range(0, len(Students)):
        print("[", Students[a]['s_id'], "]", "[", Students[a]['name'], "]", "[", Students[a]['dob'], "]", )

def ShowMark():
    print("Show marks of Student in courses:")
    for a in range(0, len(Students)):
        print("[", Mark[a]['c_id'], "]", "[", Mark[a]['s_id'], "]", "[", Mark[a]['mark'], "]", )

stud = int(numstudent())
for a in range(0, len(stud)):
    a += 1
    infStudent()
ShowStudent()

cour = int(numcourses())
for a in range(0, len(cour)):
    a+= 1
    infCourses()
ShowCourse()

marks()

for a in range(0, len(Courses)):
    ShowMark()