import random
import sys
import json
import logging

FILE_NAME = 'movies.json'
LOG_FILE = 'movies_app.log'

# creating a log
logger = logging.getLogger('MovieRecommender')
logger.setLevel(logging.DEBUG) # Accepts logs of all level

# 1.Handler for writing to a file(ALL ERROR and CRITICAL ERRORS are written to a file for analysis)
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter(
  '[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d] - %(message)s'
)
file_handler.setFormatter(file_formatter)

# 2.Handler for output to the console (Only for the user or programmer can see on the screen)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)

if not logger.handlers:
  # Add handlers to the logger
  logger.addHandler(file_handler)
  logger.addHandler(console_handler)

def load_movies():
  """
  Reads movies from a JSON file.
  
  If the file does not exist:
  - returns an empty dict
  
  If the file exists:
  - returns the data in the JSON file
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
    
  except Exception as e:
    logger.exception(f"Unexpected error occured (load_movies) - {e}")
    
    return {}
    
def save_movies(movies):
  """Save movies to a JSON file"""
  
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
    
  except Exception as e:
    logger.exception(f"An error occured while saving movies - {e}")
    
def create_movies():
  """Function that collects movies into a dict"""
  movies = {
    "action": ["John Wick", "Extraction", "Mad Max", "The Dark Knight", "Inception"],
    "comedy": ["Mr Bean", "Home Alone", "The Mask", "Rush Hour", "Hangover"],
    "horror" : ["It" , "Conjuring", "Get Out", "Insidious", "A Quiet Place"],
    "drama" : ["The Shawshank Redemption", "Forrest Gump", "The GodFather", "The Pursuit of Happyness", "Interstellar"],
    "sci-fi" : ["Avatar", "The Matrix", "Dune", "Blade Runner 2049", "Tenet"]
  }
  
  return movies

def recommend_movie():
  """Function that recommends a movie depending on a users genre"""
  
  movies = load_movies()
  
  if not movies:
    print("\nNo new movies to watch!")
    return
  
  genre_names = list(movies.keys())
  
  while True:
    print("\nType (stop) or 0 to stop watching movies")
    
    print("\n" + "=" * 35)
    print("What genre of movie would you like to see?")
    print("-" * 35)
    for ind, genre in enumerate(genre_names, start=1):
      print(f"{ind} -> {genre.title()}")
      print("-" * 35)
    
    user_choice = input("\nChoose a genre you want to watch: ").strip()
      
    if user_choice == "0" or user_choice.lower() == "stop":
      print("\nRecommending movies stopped!")
      break
    
    if user_choice.isdigit() and 1 <= int(user_choice) <= len(genre_names):
      selected_genre = genre_names[int(user_choice) -1]
      movies_list = movies[selected_genre]
      
      if not movies_list:
        print(f"\nNo movies left in {selected_genre.title()} genre!")
        continue
      
      chosen_movie = random.choice(movies_list)
      print(f"\n🍿 Recommended movie for you: {chosen_movie.title()} ({selected_genre.title()}) genre!")
      print("Enjoy your view!")
      
      logger.info(f"Successfully recommended '{chosen_movie}' from '{selected_genre}' genre to user")
      
    else:
      print("\nInvalid choice, Please choose a valid option!")

def add_movie():
  """Function that adds movies into the existing dictionary"""
  
  movies = load_movies()
  
  while True:
    print("\nType 'stop' to stop adding movies")
    
    user_input = input("Do you want to add a new film? (yes/no/stop) ").strip()
    
    if user_input.lower() == 'stop' or user_input.lower() == 'no':
      print("\nAdding movies stopped!")
      break
    
    if user_input.lower() in ('yes', 'y'):
      
      print("\n --- Existing Genres---\n")
      
      for ind, genre in enumerate(movies.keys(), start = 1):
        print(f"{ind} -> {genre.title()}")
        print("-" * 35)
      
      new_genre = input("Would you like to add a new genre (yes/no)? ").strip()
      
      if not new_genre:
        print("\nAnswer name cannot be empty")
        continue
      
      if new_genre.lower() in ('yes', 'y'):
        selected_genre = input(f"Enter a new genre: ").strip()
        if not selected_genre:
          print("\nGenre name cannot be empty")
          continue
        
        if selected_genre.lower() in [g.lower() for g in movies.keys()]:
          print("\nThis genre already exists")
          print("Please enter a new genre!")
          logger.warning(f"Failed to add genre: '{selected_genre.title()}' already exists")
          continue
        selected_genre = selected_genre.lower()
      elif new_genre.lower() in ('no', 'n'):
        selected_genre = input("What genre of movie would you like to add (write the name): ").strip()
        
        if not selected_genre:
          print("\nGenre name cannot be empty!")
          continue
        
        if selected_genre.lower() not in [g.lower() for g in movies.keys()]:
          print("No such genre found, Please select an existing genre!")
          continue
        selected_genre = selected_genre.lower()
        
      else:
        print("Wrong Command")
        continue
      
      movie_name = input(f"What movie would you like to add for {selected_genre.title()} genre? ").strip()
  
      if not movie_name:
        print("\nMovie name cannot be empty")
        continue
  
      all_existing_movies = []
      for movies_list in movies.values():
        for m in movies_list:
          all_existing_movies.append(m.lower())
      
      if movie_name.lower() in all_existing_movies:
        print("\nThis movie is already in the database!")
        logger.warning(f"Failed to add movie: '{movie_name.title()}' already exists in database")
        continue
  
      if new_genre.lower() in ('yes', 'y'):
        movies[selected_genre] = [movie_name]
        save_movies(movies)
    
      else:
        movies[selected_genre].append(movie_name)
        save_movies(movies)
      print(f"✅️ Great! The movie '{movie_name.title()}' has been successfully added!")
      logger.info(f"Successfully added '{movie_name}' movie")

def search_movie():
  """Function that finds a movie entered by the user"""
  
  movies = load_movies()
  
  if not movies:
    print("\nNo movie found, Database is empty!")
    return
  
  while True:
    print("\nType 'stop' to stop searching!")
    user_input = input("Enter a movie that you need: ").strip()
    
    if user_input.lower() == 'stop':
      print("\nSearching movie stopped")
      break
    
    if not user_input:
      print("\nMovie name cannot be empty!")
      continue
    
    found_genre = ""
    found_movie = ""
    found = False
    
    for genre, movies_list in movies.items():
      for movie in movies_list:
        if user_input.lower() == movie.lower():
          found_genre = genre
          found_movie = movie
          found = True
          break
      if found:
        break
    if found:
      print(f"\nYes, This movie was found")
      print(f"Genre: {found_genre.title()}")
      print(f"Movie title: {found_movie.title()}")
      logger.info(f"Successfully found movie: {found_movie.title()} from {found_genre.title()} genre")
    else:
      print(f"\nUnfortunately, {user_input.title()} movie not found")
      logger.info(f"Search failed, No movie found named {user_input.title()}")
      
def delete_movie():
  """Function that deletes movies entered by the user"""
  
  movies = load_movies()
  
  if not movies:
    print("\nThere's no film to delete, Database is empty")
    return
  
  while True:
    print("\nType 'stop' to stop deleting")
    user_input = input("\nWhich movie would you like to delete: ").strip()
    
    if not user_input:
      print("\nMovie name cannot be empty")
      continue
    
    if user_input.lower() == 'stop':
      print("\nDeleting movies stopped!")
      break
    
    movie_found = False
    
    for genre, movies_list in movies.items():
      for movie in movies_list:
        if user_input.lower() == movie.lower():
          movie_found = True
          
          while True:
            print("\nYes, this movie was found")
            print(f"Genre: {genre.title()}")
            print(f"Movie title: {movie.title()}")
            
            movie_delete = input(f"\nDelete {movie.title()} (yes/no): ").strip()
        
            if movie_delete.lower() in ('yes', 'y'):
              movies_list.remove(movie)
              save_movies(movies)
              print(f"\n{movie.title()} has been successfully deleted!")
              logger.info(f"Successfully deleted {movie.title()}")
              break
            
            elif movie_delete.lower() in ('no', 'n'):
              print(f"\n{movie.title()} was not deleted")
              break
            
            else:
              print("\nInvalid choice, Please choose only 'yes' or 'no'")
              
          break
        
      if movie_found:
        break
              
    if not movie_found:
      print(f"\nNo movie found named {user_input.title()}!")
      logger.warning(f"Delete failed: Movie '{user_input.title()}' not found")

def show_movies():
  """Function that shows all existing movies"""
  
  movies = load_movies()
  
  if not movies:
    print("\nNo movies found to show")
    return
  
  print("=" * 40)
  print("     🎬   All Existing Movies   🎬")
  print("=" * 40)
  
  for genre, movies_list in movies.items():
    movie_number = len(movies_list)
    plural_suffix = ('movie' if movie_number == 1 else "movies")
    print(f"\n📌 {genre.upper()} ({movie_number} {plural_suffix}):")
    print("-" * 40)
    
    if movie_number == 0:
      print("   (There are no movies in this genre yet!)")
      
    else:
      for ind, movie in enumerate(movies_list, start=1):
        print(f"   {ind}. {movie.title()}")
  print("\n" + "=" * 40)
      
#all_movies = create_movies()
#show_movies(all_movies)

def exit_app():
  """Exit the application gracefully"""
  
  print("\nThank you for using Kryos Movie program, GoodBye!")
  
  sys.exit()
  
def main():
  
  menu_actions = {
    '1' : 'recommend movie',
    '2' : 'add movie',
    '3' : 'search movie',
    '4' : 'delete movie',
    '5' : 'show movies',
    '6' : 'exit app'
  }
  
  try:
    while True:
      print("\n" + "=" * 35)
      print("Welcome to Kryos Movie Program")
      print("=" * 35)
      for key, value in menu_actions.items():
        print(f"{key} -> {value.title()}")
      
      user_choice = input("Choose an action: ").strip()
    
      if user_choice == '1':
        recommend_movie()
      
      elif user_choice == '2':
        add_movie()
      
      elif user_choice == '3':
        search_movie()
      
      elif user_choice == '4':
        delete_movie()
    
      elif user_choice == '5':
        show_movies()
      
      elif user_choice == '6':
        exit_app()
      
      else:
        print("\nInvalid choice, Please choose only (1 to 6)")
      
  except KeyboardInterrupt:
    # close gracefully without throwing an error when the user presses Ctrl+C
    print("\n\nProject was stopped by the user")
    sys.exit(0)
    
  except Exception as e:
    # Any unexpected critical error in the program goes here
    logger.critical(f"A critical system error has occured and the program has stopped! Global Error - {e}", exc_info=True)
    sys.exit(1)
      
if __name__ == '__main__':
  main()