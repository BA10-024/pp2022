import math
import numpy as np
import curses
student=[]
course=[]
mark=[]
checkcredit=[]
checkmark=[]
GPA=[]
class students():
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        student.append(self)
    def student_infor():
        studentid=input("Enter ID of student : ")
        studentname=input("Enter the name of student: ")
        DoB=input("Enter the date of birth: ")
        students(studentid,studentname,DoB)
    def display_student(self):
        print("Student ID: ",self.id)
        print("Student name:",self.name)
        print("Date of birth: ",self.dob)
def number_student():
    return int(input("Enter the number of students in class: "))
def list_student():
    n=number_student()
    print("\nInput information of students:\n ")
    for i in range (n):
        print(f"Student {i+1}")
        s1=students.student_infor()
    x=1
    print("\nList of students in class: \n")
    for i in range(student.__len__()):	
        print("Student",x)
        s2=students.display_student(student[i])
        x+=x
        print("\n")
class courses():
    def __init__(self,id,name,credit):
        self.id=id
        self.name=name
        self.credit=credit
        course.append(self)
        checkcredit.append(self.credit)
    def course_infor():
        courseid=input("Enter course ID: ")
        coursename=input("Enter course name: ")
        credit=input("Enter credits of course: ")
        courses(courseid,coursename,credit)
    def display_course(self):
        print("Course ID: ",self.id)
        print("Course name:",self.name)
        print("Credits of course: ",self.credit)
def number_course():
    return int(input("Enter the number of courses: "))
def list_course():
    n=number_course()
    print("\nInput information of course:\n ")
    for i in range(n):
        print(f"Course {i+1}")
        c1=courses.course_infor()
    y=1
    print("\nList of courses: \n")
    for i in range(course.__len__()):	
        print("Course",y)
        c2=courses.display_course(course[i])
        y+=y
        print("\n")

class marks():
    def __init__(self,studentid,courseid,point):
        self.studentid=studentid
        self.courseid=courseid
        self.point=point
        mark.append(self)
        checkmark.append(self.point)
    def input_mark(courseid):
        studentid=("Enter student ID: ")
        if studentid in [i[0] for i in student]:
            point=math.floor(float(input("Enter mark: ")))
        else:
            print("Invalid ID.")
        marks(studentid,courseid,point)    
    def select_course(courseid):
        if courseid in [i[0] for i in course]:
            input_mark(courseid)
        else:
            print("Invalid ID.")
    def display_mark(self):
        print("Student ID: ",self.studentid)
        print("Course ID:",self.courseid)
        print("Mark: ",self.point)
def Cal_averageGPA(studentid):
    credit=np.array([checkcredit])
    mark=np.array([checkmark])
    if studentid in [i[0] for i in student]:
        for i in range(student.__len__()):
            sum_credits=np.sum(credit)
            sum_mark=np.sum(np.multiply(sum_credits,sum_mark))
            gpa=sum_mark/sum_credits
        GPA.append(gpa)
def sort_GPA():
    sorted=np.flip(np.sort(GPA))
    print("List students by GPA descending:  ",sorted)

list_student()
list_course()
n=int(input("Enter the number of courses you want to mark: "))
for i in range (n):
    courseid=input("Enter course ID: ")
    m1=marks.select_course(courseid)
print("\nList of courses: \n")
for i in range(mark.__len__()):	
    m2=marks.display_mark(mark[i])
    print("\n")
studentid=input("Enter the student ID you want to calculate average GPA: ")
Cal_averageGPA(studentid)
