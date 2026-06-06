def validate_name(name):
  """
  Validation functions for Contact Book.
  """
  if not name:
    return False, "Name cannot be empty"
  
  return True, None
    
    
def validate_phone(phone):
  if not phone:
    return False, "Phone number cannot be empty"
  
  if not phone.startswith('+'):
    return False, "Phone number must start with '+'"
    
  if not phone[1:].isdigit():
    return False, "Only digits are allowed after '+'"
    
  if len(phone) <= 8:
    return False, "Phone number must be longer than 8 digits"
    
  return True, None