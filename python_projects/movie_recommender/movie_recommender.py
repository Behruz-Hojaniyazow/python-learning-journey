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