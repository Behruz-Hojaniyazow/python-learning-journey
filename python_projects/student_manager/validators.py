def validate_name(name):
  """
  Validation functions for Student Manager.
  """
  if not name:
    return False, "❌️ Name cannot be empty"
  
  cleaned_name = name.strip()
  if not cleaned_name:
    return False, "❌️ Name cannot consist of spaces only"
    
  allowed = cleaned_name.replace(" ", "").replace("-", "").replace("'", "")
  if not allowed.isalpha():
    return False, "❌️ Invalid name format!"
  return True, cleaned_name
  
def validate_age(age_str):
  """
  Checking the student's age (Positive integer only)
  """
  if not age_str or not age_str.strip():
    return False, "❌️ Age cannot be empty"
    
  try:
    age = int(age_str)
  
    if age <= 0:
      return False, "❌️ Age must be greater than 0!"
  
    if age > 120:
      return False, "❌ The entered age is too high!"
    return True, age
  except ValueError:
    return False, "❌️ Age must be integers only"
    
def validate_score(score_str):
  """
  Checking a student's exam score (a number from 0 to 100)
  """
  if not score_str or not score_str.strip():
    return False, "❌️ Score cannot be empty"
      
  try:
    score = float(score_str)
    
    if score < 0 or score > 100:
      return False, "❌️ The score must be between 0 and 100"
      
    final_score = int(score) if score.is_integer() else score
    return True, final_score
  except ValueError:
    return False, "❌️ The score must consist of numbers"