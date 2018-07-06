from collections import namedtuple

num = int(input())
fields = input()

Student = namedtuple('Student', fields)
students = []
for i in range(num):
    students.append(Student(*input().split()))
    
s = sum([int(student.MARKS) for student in students])

print('{:2f}'.format(s / len(students)))
