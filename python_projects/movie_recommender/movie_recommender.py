import random
import sys

def create_movies():
  """Function that collects movies into a dict"""
  movies = {
    "action": ["John Wick", "Extraction", "Mad Max", "The Dark Knight", "Inception"],
    "comedy": ["Mr Bean", "Home Alone", "The Mask", "Rush Hour", "Hangover"],
    "horror" : ["It" , "Conjuring", "Get Out", "Insidious", "A Quiet Place"],
    "drama" : ["The Shawshank Redemption", "Forrest Gump", "The GodFather", "The Pursuit In Happyness", "Interstellar"],
    "sci-fi" : ["Avatar", "The Matrix", "Dune", "Blade Runner 2049", "Tenet"]
  }
  
  return movies

def recommend_movie(movies):
  """Function that recommends a movia depending on a users genre"""
  
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
      chosen_movie = random.choice(movies_list)
      print(f"\n🍿 Recommended movie for you: {chosen_movie.title()} ({selected_genre.title()}) genre!")
      print("Enjoy your view!")
      
    else:
      print("\nInvalid choice, Please choose a valid option!")
      
#all_movies = create_movies()
#recommend_movie(all_movies)

def add_movie(movies):
  """Function that adds movies into the existing dictionary"""
  
  while True:
    print("\nType 'stop' to stop adding movies")
    
    user_input = input("Do you want to add a new film? (yes/no/stop) ").strip()
    
    if user_input.lower() == 'stop' or user_input.lower() == 'no':
      print("\nAdding movies stopped!")
      break
    
    if user_input in ('yes', 'y'):
      
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
          continue
      elif new_genre.lower() in ('no', 'n'):
        selected_genre = input("What genre of movie would you like to add (write the name): ").strip()
        
        if not selected_genre:
          print("\nGenre name cannot be empty!")
          continue
        
        if selected_genre.lower() not in [g.lower() for g in movies.keys()]:
          print("No such genre found, Please select an existing genre!")
          continue
        
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
        continue
  
      if new_genre.lower() in ('yes', 'y'):
        movies[selected_genre] = [movie_name]
    
      else:
        movies[selected_genre].append(movie_name)
      print(f"✅️ Great! The movie '{movie_name.title()}' has been successfully added!")
#new_genres = create_movies()
#add_movie(new_genres)

def search_movie(movies):
  """Function that finds a movie entered by the user"""
  
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
      if found:
        break
    if found:
      print(f"\nYes, This movie was found")
      print(f"Genre: {found_genre.title()}")
      print(f"Movie title: {found_movie.title()}")
    else:
      print(f"\nUnfortuntely, {user_input.title()} movie not found")
      
#search_movies = create_movie()
#search_movie(search_movies)

def delete_movie(movies):
  """Function that deletes movies entered by the user"""
  
  if not movies:
    print("\nThere's no film to delete, Database is empty")
    return
  
  while True:
    print("\nType stop to stop deleting")
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
            
            movie_delete = input(f"\nDelete {movie.title()} (yes/no): ").strip().lower()
        
            if movie_delete in ('yes', 'y'):
              movies_list.remove(movie)
              print(f"\n{movie.title()} has been successfully deleted!")
              break
            
            if movie_delete in ('no', 'n'):
              print(f"\n{found_movie.title()} was not deleted")
              break
            
            else:
              print("\nInvalid choice, Please choose only 'yes' or 'no'")
              
      if movie_found:
        break
              
    if not movie_found:
      print(f"\nNo movie found named {user_input.title()}!")

#remove_movie = create_movies()
#delete_movie(remove_movie)

def show_movies(movies):
  """Function that shows all existing movies"""
  
  if not movies:
    print("\nNo movies found to show")
    return
  
  print("=" * 40)
  print("     🎬   All Existing Movies   🎬")
  print("=" * 40)
  
  for genre, movies_list in movies.items():
    movie_number = len(movies_list)
    plural_suffix = 'movie' if movie_number == 1 else "movies"
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