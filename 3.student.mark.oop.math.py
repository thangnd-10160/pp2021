import math
import numpy as np
import curses


class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__gpa = None

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_dob(self, dob):
        self.__dob = dob

    def set_gpa(self, gpa):
        self.__gpa = gpa


class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_credits(self, credits):
        self.__credits = credits


class Mark:
    def __init__(self, student, course, mark):
        self.__student = student
        self.__course = course
        self.__mark = mark

    def get_student(self):
        return self.__student

    def get_course(self):
        return self.__course

    def get_mark(self):
        return self.__mark

    def set_student(self, student):
        self.__student = student

    def set_course(self, course):
        self.__course = course

    def set_mark(self, mark):
        self.__mark = mark


if __name__ == '__main__':
    studentList = []
    studentIdList = []
    courseList = []
    courseIdList = []
    markList = []
    courseMarkList = []

    scr = curses.initscr()

    scr.addstr("Enter number of student: ")
    numberStudent = int(scr.getstr().decode())
    scr.addstr(f"Class has: {numberStudent} students")
    scr.clear()


    def input_student(id, name, dob):
        studentList.append(Student(id, name, dob))
        studentIdList.append(id)


    for i in range(numberStudent):
        scr.addstr("Student number #" + str(i + 1))
        scr.addstr("\nId: ")
        id = scr.getstr().decode()
        scr.addstr("Name: ")
        name = scr.getstr().decode()
        scr.addstr("Dob: ")
        dob = scr.getstr().decode()
        scr.addstr("\n")
        input_student(id, name, dob)
    scr.clear()

    scr.addstr("Enter course number: ")
    numberCourse = int(scr.getstr().decode())
    scr.addstr(f"There are {numberCourse} courses")
    scr.clear()


    def input_course(id, name, credits):
        courseList.append(Course(id, name, credits))
        courseIdList.append(id)


    def get_course_by_id(id):
        for course in courseList:
            if course.get_id() == id:
                return course


    for i in range(numberCourse):
        scr.addstr("Course number #" + str(i + 1))
        scr.addstr("\nId: ")
        id = scr.getstr().decode()
        scr.addstr("Name: ")
        name = scr.getstr().decode()
        scr.addstr("Credits: ")
        credits = int(scr.getstr().decode())
        scr.addstr("\n")
        input_course(id, name, credits)
    scr.clear()

    while len(markList) < len(studentList) * len(courseList):
        scr.addstr("Courses that have not inputted marks: \n")
        for course in courseList:
            if course.get_id() not in courseMarkList:
                scr.addstr(course.get_name() + "\n")
        scr.addstr("\nEnter Course Id to input Mark: ")
        idForSum = scr.getstr().decode()
        while True:
            if idForSum not in courseIdList:
                scr.clear()
                scr.addstr("Wrong, enter again course ID: ")
                idForSum = scr.getstr().decode()
            if idForSum in courseMarkList:
                scr.clear()
                scr.addstr("Course mark already inputted, enter again course ID: ")
                idForSum = scr.getstr().decode()
            else:
                scr.clear()
                break

        for student in studentList:
            scr.addstr(f"Enter mark for {student.get_name()}: ")
            markList.append(
                Mark(student, get_course_by_id(idForSum), math.floor((float(scr.getstr().decode())) * 10) / 10.0))
            courseMarkList.append(idForSum)
            scr.clear()


    def calculate_gpa(student_id):
        marks = []
        credits = []
        for mark in markList:
            if mark.get_student().get_id() == student_id:
                marks.append(float(mark.get_mark()))
                credits.append(float(mark.get_course().get_credits()))
        return np.average(np.array(marks), weights=np.array(credits))


    while True:
        scr.clear()
        scr.addstr("Now you are done with input")
        scr.addstr("\nPress 1: Show student list")
        scr.addstr("\nPress 2: Show course list")
        scr.addstr("\nPress 3: Show Mark")
        scr.addstr("\nPress 4: Calculate GPA for a student")
        scr.addstr("\nPress 5: Exit")

        scr.addstr("\nSelect: ")
        choice = int(scr.getstr().decode())
        if choice == 1:
            scr.clear()
            for student in studentList:
                scr.addstr(student.get_id(), student.get_name(), "\n")
            curses.napms(1000 * numberStudent)
        elif choice == 2:
            scr.clear()
            for course in courseList:
                scr.addstr(course.get_id(), course.get_name(), "\n")
            curses.napms(1000 * numberCourse)
        elif choice == 3:
            scr.clear()
            for mark in markList:
                scr.addstr(f"{mark.get_student().get_name()} - {mark.get_course().get_name()} - {mark.get_mark()}\n")
            curses.napms(1000 * len(markList))
        elif choice == 4:
            scr.clear()
            scr.addstr("Enter student id to calculate GPA: ")
            student_id = scr.getstr().decode()
            if student_id not in studentIdList:
                scr.clear()
                scr.addstr("\nStudent does not exist")
            else:
                scr.clear()
                for student in studentList:
                    if student.get_id() == student_id:
                        scr.addstr(f"\nGPA of {student.get_name()}:", calculate_gpa(student_id))
                curses.napms(1000)
        elif choice == 5:
            exit()
        else:
            scr.clear()
            scr.addstr("Wrong choice. Choose again: ")