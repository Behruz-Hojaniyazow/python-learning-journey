import sys
from movie_service import (
  recommend_movie,
  add_movie,
  search_movie,
  delete_movie,
  show_movies,
  exit_app
) 
from logger_config import get_logger

logger = get_logger()

def main():
  
  menu_actions = {
    '1' : {'text' : 'recommend movie', 'func' : recommend_movie},
    '2' : {'text' : 'add movie', 'func' : add_movie},
    '3' : {'text' : 'search movie', 'func' : search_movie},
    '4' : {'text' : 'delete movie', 'func' : delete_movie},
    '5' : {'text' : 'show movies', 'func' : show_movies},
    '6' : {'text' : 'exit app', 'func' : exit_app}
  }
  
  try:
    while True:
      print("\n" + "=" * 35)
      print("Welcome to Kryos Movie Program")
      print("=" * 35)
      for key, value in menu_actions.items():
        print(f"{key} -> {value['text'].title()}")
      
      user_choice = input("\nChoose an action: ").strip()
    
      if user_choice in menu_actions:
        menu_actions[user_choice]['func']()
      
      else:
        print("\nInvalid choice, Please choose only (1 to 6)")
      
  except KeyboardInterrupt:
    # close gracefully without throwing an error when the user presses Ctrl+C
    print("\n\nProject was stopped by the user")
    sys.exit(0)
    
  except Exception as e:
    # Any unexpected critical error in the program goes here
    logger.critical(f"A critical system error has occured and the program has stopped! Global Error - {e}", exc_info=True)
    print("A critical error occurred")
    sys.exit(1)
      
if __name__ == '__main__':
  main()