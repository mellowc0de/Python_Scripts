name = input('Enter student name: ')
grade = int(input('Enter student\'s grade: '))

def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

#print(student_grade("Reed", 80))
#print(student_grade("Paige", 92))
#print(student_grade("Jesse", 85))

print(student_grade(name, grade))