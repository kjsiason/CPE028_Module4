import Student
import Grades

p1=Student.Student("Karl Siason", 22)
p2=Grades.Grades("CPE 028", 3, 1)
print(p1)
print(p2)
print("Name:", p1.name)
print("Age:", p1.age)
print("Course Code:", p2.code)
print("Course Units:", p2.unit)
print("Course Grade:", p2.grade)