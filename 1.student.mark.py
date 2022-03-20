#!/usr/bin/env python
students=[]
courses=[]
marks={}
def no_student():
     x=int(input("Enter the number of students in the class: "))
     return x
def no_courses():
     y=int(input("Enter the number of courses: "))
     return y
def student_infor():
    print("Information of students: ")
    studentid=input("Enter ID of student : ")
    studentname=input("Enter the name of student: ")
    DoB=input("Enter the date of birth: ")
    return studentid, studentname, DoB
def courses_infor():
    print("Information of the courses: ")
    courseid=input("Enter the course id: ")
    coursename=input("Enter the name of course: ")
    return courseid, coursename
def input_mark(coursesid,n):
    for i in range (n):
        print(f"Student {i+1}")
        studentid=input("Enter student id: ")
        if studentid not in [i[0] for i in students]:
            print("Invalid id.")
        point=float(input(f"Enter mark of course: "))
        if coursesid in marks:
            marks[coursesid].append((studentid,point))
def select_courses(n,coursesid):
    if coursesid in [i[0] for i in courses]:
    	input_mark(coursesid,n)  
    else:
    	print("Invalid id.")

def list_student(students):
    n=no_student()
    for i in range (n):
        studentid,studentname,DoB=student_infor()
        students.append((studentid,studentname,DoB))
    print ("List of students in the class: ")
    for i in students:
        print (f"\nStudent id: {i[0]}")
        print (f"Student name: {i[1]}")
        print (f"Date of birth: {i[2]}\n")
def list_courses(courses):
    n=no_courses()
    for i in range (n):
        coursetid,coursename=courses_infor()
        courses.append((coursetid,coursename))
    print ("List of courses: ")
    for i in courses:
        print (f"\nCourses id: {i[0]}")
        print (f"Courses name: {i[1]}\n")
def showMark(coursesid):     
	coursesid=int(input("Enter the course id you want to see marks:     "))
	if coursesid in marks:
	    for i in marks[coursesid]:
	        print(f"Student {i[0]} :{i[1]}")
list_student(students)
list_courses(courses)
n=int(input("Enter the number of courses you want to mark: "))
for i in range (n):
    coursesid=input("Enter course id: ")
    select_courses(n, coursesid)
showMark(coursesid)


