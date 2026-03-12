#creating list in dictionary
students = {"John" : [5,4,3,4],
            "Jason" : [3,2,3,4],
           "David" : [5,4,5,5],
           "Carlos" : [3,2,2,4],
           "Scott" : [5,2,3,4]
}
#calculating the average score for each student with (for)
for student,score in students.items():
#we calculate the average grade for each student
  total_score = sum(score) #Total marks
  number_of_subjects = len(score) #number of subjects
  average_score = total_score / number_of_subjects #average rating
  print(f"{student}'s average score is {average_score}")