def validate_letter(letter):
  """
  Validate user input
  
  Returns True if input contains exactly one alphabetic character.
  """
  
  if not letter.strip():
    return False, "Not allowed empty space, Enter a letter"
    
  if len(letter) != 1:
    return False, "Enter exactly one letter"
    
  if not letter.isalpha():
    return False, "Please enter only letters!"
    
  return True, None