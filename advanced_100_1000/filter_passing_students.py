info_students = {
  'behruz' : 45,
  'anvar' : 89,
  'mahmut' : 78,
  'nuriya' : 49,
  'zamira' : 89
}
passed_students = dict(filter(lambda student: student[1] > 50, info_students.items()))
for student, score in passed_students.items():
  print(f" -  {student.title()} scored {score} points!")