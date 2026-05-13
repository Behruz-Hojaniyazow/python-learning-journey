students = {
  'anvar' : 90,
  'zamira' : 90,
  'behruz' : 76,
  'mahmut' : 69,
  'nuriya' : 50
}
passed_students = dict(
  filter(lambda student: student[1] > 70, students.items())
)
for student, score in passed_students.items():
  print(f"{student.title()} passed with {score}")