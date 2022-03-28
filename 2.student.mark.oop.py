student=[]
course=[]
class students():
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
    def display_student(self,s):
        print("Student ID: ",s.id)
        print("Student name:",s.name)
        print("Date of birth: ",s.dob)
def number_student():
    return int(input("Enter the number of students in class: "))
def student_infor():
    studentid=input("Enter ID of student : ")
    studentname=input("Enter the name of student: ")
    DoB=input("Enter the date of birth: ")
    return studentid, studentname, DoB
def list_student():
    n=number_student()
    print("\nInput information of students:\n ")
    for i in range(n):
        print(f"Student {i+1}")
        studentid,studentname,dob=student_infor()
        s=students(studentid,studentname,dob)
        student.append(s)
        print("\n")
    x=1
    print("List of students in class: \n")
    for i in range(student.__len__()):	
        print("Student",x)
        s.display_student(student[i])
        x+=x
        print("\n")
class courses():
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display_course(self,c):
        print("Course ID: ",c.id)
        print("Course name:",c.name)
def number_course():
    return int(input("Enter the number of courses: "))
def course_infor():
    courseid=input("Enter course ID: ")
    coursename=input("Enter course name: ")
    return courseid,coursename
def list_course():
    n=number_course()
    print("\nInput information of course:\n ")
    for i in range(n):
        print(f"Course {i+1}")
        courseid,coursename=course_infor()
        c=courses(courseid,coursename)
        course.append(c)
        print("\n")
    y=1
    print("List of courses: \n")
    for i in range(course.__len__()):	
        print("Course",y)
        c.display_course(course[i])
        y+=y
        print("\n")	    
list_student()
list_course()
