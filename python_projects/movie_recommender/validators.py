def validate_movie(movie):
  """
    Validates the movie name to ensure it is not empty or whitespace-only.

    Args:
        movie (str): The movie title provided by the user.

    Returns:
        tuple: (bool, str) True and the stripped movie name if valid; 
               False and an error message if invalid.
    """
    
  cleaned_movie = movie.strip()
  if not cleaned_movie:
    return False, "❌️ Movie name cannot be empty \nMovie name cannot consist of spaces only"
    
  return True, cleaned_movie
  
def validate_genre(genre):
  """
    Validates the genre name to ensure it is not empty or whitespace-only.

    Args:
        genre (str): The genre name provided by the user.

    Returns:
        tuple: (bool, str) True and the stripped genre name if valid; 
               False and an error message if invalid.
    """
    
  cleaned_genre = genre.strip()
  if not cleaned_genre:
    return False, "❌️ Genre name cannot be empty \nGenre name cannot consist of spaces only"
    
  return True, cleaned_genre
  
def duplicate_movie(user_input, movies):
  """
    Checks if a movie already exists in the database across all genres (case-insensitive).

    Args:
        user_input (str): The movie title to check for duplicates.
        movies (dict): The dictionary containing genres as keys and lists of movies as values.

    Returns:
        tuple: (bool, str) False and an error message if a duplicate is found; 
               True and the original user input if the movie is unique.
    """
    
  target_movie = user_input.strip().lower()

  for movies_list in movies.values():
    for m in movies_list:
      if m.lower() == target_movie:
        return False, "❌️ This movie already exists in database"
    
  return True, user_input
  
def duplicate_genre(user_input, movies):
  """
    Checks if a genre already exists in the database (case-insensitive).

    Args:
        user_input (str): The genre name to check for duplicates.
        movies (dict): The dictionary containing existing genres as keys.

    Returns:
        tuple: (bool, str) False and an error message if the genre exists; 
               True and the original user input if the genre is new.
    """
    
  target_genre = user_input.strip().lower()
  if any(genre.lower() == target_genre for genre in movies.keys()):
    return False, "❌️ This genre already exists \nPlease enter a new genre"
    
  return True, user_input