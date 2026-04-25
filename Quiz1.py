# You are hired to develop a Student Management System for a university.
# The system should manage student records, courses, and results using Python concepts.
# 1.	Create a Class Called Student.
# Each student should have:
# •	student_id (string)
# •	name (string)
# •	age (integer)
# •	courses (list)
# •	marks (dictionary → course: marks)
# •	grade (initially None)
# Use a constructor to initialize these values.
# 2.	Store available courses as a tuple:
# a.	Math
# b.	English
# c.	Physics
# d.	Computer
# e.	Statistics

# 3.	Create a list called students_list to store multiple student objects. 
# 4.	Store marks in dictionary format:
# { “maths” : 85…….}
# 5.	Create the following functions:
# a.	add_student()
# b.	calculate_grade(student)
# c.	display_student(student)
# d.	search_student(student_id)
# A.	Use for Loop
# •	To calculate total and average marks
# •	To display all students
# B. Grade Rules
# •	Average ≥ 80 → Grade "A"
# •	Average ≥ 70 → Grade "B"
# •	Average ≥ 60 → Grade "C"
# •	Otherwise → Grade "Fail"
# C.	Use while Loop

# Create a menu-driven system:
# 1. Add Student
# 2. Display All Students
# 3. Search Student
# 4. Exit
# The program should continue running until user selects Exit.

student_list = []
class student:
    courses = ('Maths', 'English', 'Physics', 'Computer', 'Statistic')
    def __init__( self, student_id, name, age, courses, marks, grade = None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = courses
        self.marks = marks
        self.grade = grade 
    def add_student(self,student_id,name,age):
        new_student = student(student_id, name, age)
        student_list.append(new_student)
    def display_student(student):
        print("Student ID:", student.student_id)
        print("Name:", student.name)
        print("Age:", student.age)
        print("Courses:", student.courses)
        print("Marks:", student.marks)
        print("Grade:", student.grade)
    
    def calculate_grade(self,marks):
        count = 0
        average = sum(marks)/ len(marks)
        if 	average >= 80:
            print("Grade A")
        elif average >= 70:
            print("Grade B")
        elif average >= 60:
            print("Grade C")
        else:
            print("Fail")
s = student()
s.add_student(1234, "Maira", 22, student.courses,[10,60,80,50,70])


#     def display(add_student):
#         print(f'ID ={student_id} name= {name} age= {age}')
        






