import json
from config import FILE_NAME
from logger_config import get_logger

logger = get_logger()

def create_movies():
  """
  Creates and returns the default movie database.

  The database contains predefined movie categories
  and a collection of movies for each category.

  Returns:
    dict: Dictionary where keys are genres and
    values are lists of movie titles.
  """

  movies = {
    "action": ["John Wick", "Extraction", "Mad Max", "The Dark Knight", "Inception"],
    "comedy": ["Mr Bean", "Home Alone", "The Mask", "Rush Hour", "Hangover"],
    "horror" : ["It" , "Conjuring", "Get Out", "Insidious", "A Quiet Place"],
    "drama" : ["The Shawshank Redemption", "Forrest Gump", "The GodFather", "The Pursuit of Happyness", "Interstellar"],
    "sci-fi" : ["Avatar", "The Matrix", "Dune", "Blade Runner 2049", "Tenet"]
  }
  
  return movies

def load_movies():
  """
  Loads movies from the JSON storage file.

  If the file does not exist, a default movie
  database is created and saved automatically.

  Returns:
    dict: Dictionary containing movie data.

  Raises:
    No exception is propagated because all
    exceptions are handled internally and logged.
  """
  
  try:
    with open (FILE_NAME, 'r', encoding='utf-8') as file:
      movies = json.load(file)
      
      return movies
      
  except FileNotFoundError:
    # It is normal for file not to exist (when opened for the first time) this can be done with a small warning (DEBUG)
    logger.debug(f"'{FILE_NAME}' not found, Initializing with default movies")
    default_movies = create_movies()
    save_movies(default_movies)
    return default_movies
    
  except json.JSONDecodeError as e:
    # JSON STRUCTURE is corrupted - this is a serious error!
    logger.exception(f"Invalid JSON format - {e}")
    
    return {}
    
  except Exception:
    logger.exception(f"Unexpected error occured in (load_movies)")
    
    return {}
    
def save_movies(movies):
  """
  Saves the movie database to a JSON file.

  Args:
    movies (dict): Dictionary containing
        movie categories and movie titles.

  Returns:
    None
  """
  
  try:
    
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
      json.dump(
        movies,
        file,
        indent=4,
        ensure_ascii=False
      )
      
  except IOError as e:
    logger.exception(f"File error - {e}")
    
  except Exception:
    logger.exception(f"An error occured while saving movies")