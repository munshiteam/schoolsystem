import pickle
from Teacher import *
from Student import *
from SchoolClass import *
import os

teachers = []
students = []
schoolClasses = []

os.system('cls')


def initialize():
    try:
        if os.path.exists("teacher_dict.pickle"):
            with open("teacher_dict.pickle", "rb") as f:
                global teachers
                teachers = pickle.load(f)
                print(teachers, " \n")
    except EOFError:
        print("Sorry you have no Teachers saved")

    try:
        if os.path.exists("student_dict.pickle"):
            with open("student_dict.pickle", "rb") as f:
                global students
                students = pickle.load(f)
                print(students, " \n")
    except EOFError:
        print("Sorry you have no Student saved")

    try:
        if os.path.exists("schoolClass_dict.pickle"):
            with open("schoolClass_dict.pickle", "rb") as f:
                global schoolClasses
                schoolClasses = pickle.load(f)
                print(schoolClasses, " \n")
    except EOFError:
        print("Sorry you have no School Class saved")
    input("Press any key to continue..")
    os.system('cls')


def persist():
    with open("teacher_dict.pickle", "wb") as t:
        pickle.dump(teachers, t)
        t.close()
    with open("student_dict.pickle", "wb") as t:
        pickle.dump(students, t)
        t.close()
    with open("schoolClass_dict.pickle", "wb") as t:
        pickle.dump(schoolClasses, t)
        t.close()


def main():
    initialize()
    while True:
        os.system('cls')
        print("-" + "=" * 8 + "|  WELCOME TO SAIM AND ANAS'S SCHOOL SYSTEM  |" + "=" * 8 + "-")
        print(" \n")
        print("1. Teacher...")
        print("2. Student...")
        print("3. Class...")
        print("4. Leave\n")
        opt = input(" Please Choose one of the above (ex. 1,2,3,4 or 5)")
        if opt == "1":
            TeacherMenu()
        elif opt == "2":
            StudentMenu()
        elif opt == "3":
            ClassMenu()
        elif opt == "4":
            persist()
            break


def TeacherMenu():
    while True:
        os.system('cls')
        print("-" + "=" * 8 + "|  TEACHER MENU  |" + "=" * 8 + "-")
        print(" ")
        print("What would you like to do? \n")
        print("1. Add A Teacher")
        print("2. Edit Teachers")
        print("3. Delete A Teacher")
        print("4. See Previous/Saved Teachers")
        print("5. Back\n")
        opt = input(" Please Choose one of the above (ex. 1,2,3,4 or 5)")
        if opt == "1":
            AddTeacher()
        elif opt == "2":
            print("EditTeacher() work in progress")
        elif opt == "3":
            DeleteTeacher()
        elif opt == "4":
            SeeTeachers()
        elif opt == "5":
            break
        else:
            input("Not a valid selection. Press any key to continue...")


def AddTeacher():
    os.system('cls')
    print("-" + "=" * 8 + "|  ADD A TEACHER  |" + "=" * 8 + "-")

    teachervalue = Teacher(input("Enter Teacher Name: ").title(),
                           input("Enter Teacher age: "),
                           input("Any Qualifications? ").upper(),
                           )
    teachers.append(teachervalue)
    print(teachervalue)
    input("Press any key to continue..")


def DeleteTeacher():
    os.system('cls')
    print("-" + "=" * 8 + "|  DELETE A TEACHER  |" + "=" * 8 + "-")

    print('Which Teacher will you be deleting?')
    print("No.\tNAME\t\tAGE\t\tQUALIFICATION")
    counter = 1
    for teacher in teachers:
        print(str(counter) + "\t" + teacher.name + "\t\t" + teacher.age + "\t\t" + teacher.qualification)
        counter += 1
    teacherIndexToAdd = int(input("Select number"))
    teachers.pop(teacherIndexToAdd - 1)


def SeeTeachers():
    os.system('cls')
    print("-" + "=" * 8 + "|  SAVED TEACHERS  |" + "=" * 8 + "-")
    if len(teachers) == 0:
        print("There is not Teacher register with school")
    else:
        print(teachers, "\n")


def StudentMenu():
    while True:
        os.system('cls')
        print("-" + "=" * 8 + "|  STUDENT MENU  |" + "=" * 8 + "-")
        print("What would you like to do \n")
        print("1. Add Student")
        print("2. Edit Student")
        print("3. Delete Student")
        print("4. See Previously Saved Students")
        print("5. Return\n")
        opt = input(" Please Choose one of the above (ex. 1,2,3 or 4)")
        if opt == "1":
            AddStudent()
        elif opt == "2":
            EditStudent()
        elif opt == "3":
            DeleteStudent()
        elif opt == "4":
            SeeStudent()
        elif opt == "5":
            break
        else:
            input("Not a valid selection. Press any key to continue...")

def EditStudent():
    print("Work in progess")

def AddStudent():
    os.system('cls')
    print("-" + "=" * 8 + "|  ADD A STUDENT  |" + "=" * 8 + "-")
    studentvalue = Student(input("Enter Student Name").title(),
                           input("Enter Student Age"),
                           )
    students.append(studentvalue)
    print(studentvalue)
    input("Press any key to continue..")

def DeleteStudent():
    os.system('cls')
    print("-" + "=" * 8 + "|  DELETE A STUDENT  |" + "=" * 8 + "-")

    print('Which Student will you be deleting?')
    print("No.\tNAME\t\tAGE")
    counter = 1
    for student in students:
        print(str(counter) + "\t" + student.name + "\t\t" + student.age )
        counter += 1
    studentIndexToAdd = int(input("Select number"))
    students.pop(studentIndexToAdd - 1)

def SeeStudent():
    os.system('cls')
    print("-" + "=" * 8 + "|  SAVED STUDENTS  |" + "=" * 8 + "-")
    if len(students) == 0:
        print("There is not Teacher register with school")
    else:
        print(students, "\n")


def ClassMenu():
    os.system('cls')
    while True:
        print("-" + "=" * 8 + "|  CLASS MENU  |" + "=" * 8 + "-")
        print("What would you like to do \n")
        print("1. Add Class")
        print("2. Edit Class")
        print("3. Remove Class")
        print("4. Print Class")
        print("5. Return\n")
        opt = input(" Please Choose one of the above (ex. 1,2,3 or 4)")
        if opt == "1":
            AddClass()
        elif opt == "2":
            print("")
        elif opt == "3":
            DeleteClass()
        elif opt == "4":
            PrintSchoolClass()
        elif opt == "5":
            break
        else:
            input("Not a valid selection. Press any key to continue...")


def AddClass():
    if len(teachers) != 0 or len(students) != 0:
        classGrade = input("Enter class grade ")
        print('Which Teacher will be teaching this class?')
        print("No.\tNAME\t\tAGE\t\tQUALIFICATION")
        counter = 1
        for teacher in teachers:
            print(str(counter) + "\t" + teacher.name + "\t\t" + teacher.age + "\t\t" + teacher.qualification)
            counter += 1
        teacherIndexToAdd = int(input("Which Teacher do you want to add.  Select number"))
        studentsListToAdd = []
        while True:
            print('Which Student will be studying in this class?')
            print("No.\tNAME\t\tAGE\t\t")
            counter = 1
            for student in students:
                print(str(counter) + "\t" + student.name + "\t\t" + student.age)
                counter += 1
            studentIndexToAdd = int(input("Which Student do you want to register.  Select number"))
            if counter == -1 or len(students) == 0:
                break
            studentToAdd = students.pop(studentIndexToAdd - 1)
            studentsListToAdd.append(studentToAdd)
            ipt = input("Would you like to register more students")
            if ipt != "y" or ipt != "Y" or ipt != "yes" or ipt != "Yes":
                break
        schoolClasses.append(SchoolClass(teachers.pop(teacherIndexToAdd - 1), classGrade, studentsListToAdd))
    else:
        input("No Teachers or Student are available. Kindly use their menu to register them \nPress any key...")

def DeleteClass():
    print("Work in progress ")

def PrintSchoolClass():
    print("No.\tGrade\t\t\t\tTeacher\t\t\t\t\t\t\t\t\t\tStudents")
    counter = 1
    for schoolClass in schoolClasses:
        print(str(counter) + "\t" + str(schoolClass.grade) + "\t\t\t\t" + str(
            schoolClass.teacher) + "\t\t\t\t" + str(schoolClass.students))
        counter += 1
    print(" \n" * 5)
    input("Press any key to continue..")


main()
