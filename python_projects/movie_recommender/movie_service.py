import random
from storage import (
  load_movies,
  save_movies
)
from validators import (
  validate_movie,
  validate_genre,
  duplicate_movie,
  duplicate_genre
)
from logger_config import get_logger

logger = get_logger()

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
        is_valid, result = validate_genre(selected_genre)
        if not is_valid:
          print(f"\n{result}")
          continue
        
        is_valid, result = duplicate_genre(selected_genre, movies)
        if not is_valid:
          print(f"\n{result}")
          logger.warning(f"Failed to add genre: '{selected_genre.title()}' already exists")
          continue
        selected_genre = selected_genre.lower()
      elif new_genre.lower() in ('no', 'n'):
        selected_genre = input("What genre of movie would you like to add (write the name): ").strip()
        
        is_valid, result = validate_genre(selected_genre)
        if not is_valid:
          print(f"\n{result}")
          continue
        
        if selected_genre.lower() not in [g.lower() for g in movies.keys()]:
          print(f"\nNo such genre found, Please select an existing genre")
          logger.warning(f"Failed to find genre: '{selected_genre}' during movie addition")
          continue
        selected_genre = selected_genre.lower()
        
      else:
        print("Wrong Command")
        continue
      
      movie_name = input(f"What movie would you like to add for {selected_genre.title()} genre? ").strip()
      
      is_valid, result = validate_movie(movie_name)
      if not is_valid:
        print(f"\n{result}")
        continue
      
      is_valid, result = duplicate_movie(movie_name, movies)
      if not is_valid:
        print(f"\n{result}")
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
  """
  Search for a movie in the database.

  Returns:
    None
  """
  
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
    
    is_valid, result = validate_movie(user_input)
    if not is_valid:
      print(f"\n{result}")
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
    
    if user_input.lower() == 'stop':
      print("\nDeleting movies stopped!")
      break
    
    is_valid, result = validate_movie(user_input)
    if not is_valid:
      print(f"\n{result}")
      continue
    
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
  
  logger.info("Application closed")
  print("\nThank you for using Kryos Movie program, GoodBye!")
  
  sys.exit()