"""
Console entry point and UI-flow controller for the Movie Recommender
application (KRYOS Movie Project).

This module wires together the storage, service, and logging layers,
and drives the interactive command-line experience: presenting menus,
collecting user input, delegating business logic to `MovieService`,
and translating each resulting `MovieStatus` into a user-facing
message via `ui_helpers`.

Each menu feature (recommend, add, search, delete, show, exit) is
implemented as its own `ui_*` function containing a self-contained
input loop, so a user can repeat an action or return to the main menu
at any point by entering '0' or 'stop'. The `main()` function ties
these features together into a persistent menu loop and provides
top-level exception handling so the application exits gracefully on
both expected (Ctrl+C) and unexpected critical errors.
"""


import sys
from typing import NoReturn
from movie_service import MovieService
from logger_config import get_logger
from storage import MovieStorage
from config import FILE_NAME
from status import MovieStatus
from ui_helpers import (
    print_header,
    print_section,
    print_error,
    print_warning,
    print_info,
    print_back_msg,
    print_separator
)

logger = get_logger()
storage = MovieStorage(FILE_NAME)
movies_service = MovieService(storage)

COMMON_ERRORS = {
    MovieStatus.EMPTY_MOVIE : "❌️ Movie name cannot be empty",
    MovieStatus.DUPLICATE_MOVIE : "⚠️ This movie already exists in the database",
    MovieStatus.EMPTY_GENRE : "❌️ Genre name cannot be empty",
    MovieStatus.DUPLICATE_GENRE : "⚠️ This Genre already exists in the database",
    MovieStatus.INVALID_CHOICE : "❌️ Your choice is out of range. Please choose a number from the list",
    MovieStatus.INVALID_CHOICE_FORMAT : "❌️ Invalid input, Please use digits only",
    MovieStatus.EMPTY_DATA : "⚠️ No movies found in the database"
}

def ui_add_movie() -> None:
    """
    Run the interactive "Add Movie" screen.

    Repeatedly prompts the user to either select an existing genre or
    create a new one, then enter a movie title to add under that
    genre. Delegates the actual add operation to
    `MovieService.add_movie` and prints a status message after each
    attempt. The loop continues until the user enters '0' or 'stop' at
    any prompt.

    Returns:
        None
    """
    
    ACTION_MESSAGES = {
        MovieStatus.SAVE_ERROR : "⚠️ An error occurred while saving new movies to the database",
        MovieStatus.SUCCESS : "✅️ New movie saved successfully"
    }
    
    print_header("ADD MOVIE", "➕️")
    
    while True:
        movies_data = movies_service.get_movies_data()
        genres = list(movies_data.keys() if movies_data else [])
        
        if not genres:
            print_info("There're no genres and movies in the database")
            selected_genre = input("Enter a new genre (or '0'/'stop' to exit): ").strip()
            if selected_genre.lower() in ('stop', '0'):
                print_back_msg()
                break
            
        else:    
            print_section("Available Genres", "🎭")
            for index, genre in enumerate(genres, start=1):
                print(f"  {index} -> {genre.title()}")
            print("  N -> Add a new genre")
            print_separator()
            
            user_choice = input("Select a genre number, (N for new, '0'/'stop' to exit): ").strip()
            if user_choice.lower() in ('stop', '0'):
                print_back_msg()
                break
            
            if user_choice.lower() == 'n':
                selected_genre = input("Enter a new genre (or '0'/'stop' to exit): ").strip()
                if selected_genre.lower() in ('stop', '0'):
                    print_back_msg()
                    break
            
            elif user_choice.isdigit():
                choice = int(user_choice)
            
                if not (1 <= choice <= len(genres)):
                    print_error(f"Invalid choice, Please enter between 1 and {len(genres)}")
                    continue
            
                selected_genre = genres[choice - 1]
            else:
                print_error("Invalid input! Please enter a valid number or 'N'.")
                continue
            
        
        user_movie = input(f"Enter a movie for {selected_genre.title()} genre: ").strip()
        if user_movie.lower() in ('stop', '0'):
            print_back_msg()
            break
        
        status = movies_service.add_movie(selected_genre, user_movie)
        
        message = ACTION_MESSAGES.get(status) or COMMON_ERRORS.get(status, f"Unexpected status {status.name}")
        
        print(f"\n{message}")
    
    
    
def ui_recommend_movie() -> None:
    """
    Run the interactive "Recommend Movie" screen.

    Guards against an empty database up front, then repeatedly
    displays the list of available genres and asks the user to pick
    one by number. For each selection, delegates to
    `MovieService.recommend_movie` and prints either the randomly
    chosen movie or an appropriate status message. The loop continues
    until the user enters '0' or 'stop'.

    Returns:
        None
    """
    
    if movies_service.is_empty():
        logger.info("No movies found in the database to recommend")
        print_info("\nNo movies found to recommend, first add movies")
        return
        
    ACTION_MESSAGES = {
        MovieStatus.SUCCESS : "✅️ Movie Recommended successfully",
        MovieStatus.NOT_FOUND : "⚠️, No movies left in this genre, first add movies for this genre"
    }
    
    movies = movies_service.get_movies_data()
    genres = list(movies.keys() if movies else [])
    
    print_header("RECOMMEND MOVIE", "🎯")
        
    while True:
        print_section("Choose a genre", "🎭")
        for index, genre in enumerate(genres, start=1):
            print(f"  {index} -> {genre.title()}")
        print_separator()
        user_choice = input("\nSelect a genre number (or '0'/'stop' to exit): ").strip()
        
        if user_choice.lower() in ('stop', '0'):
            print_back_msg()
            break
        
        status, result = movies_service.recommend_movie(user_choice)
        message = ACTION_MESSAGES.get(status) or COMMON_ERRORS.get(status, f"Unexpected status: {status.name}")
        
        if status == MovieStatus.SUCCESS:
            print(f"\n{message}")
            for genre, movie in result.items():
                print_section("Recommended movie for you" "🍿")
                print(
                    f"  Genre: {genre.upper()}\n"
                    f"  Movie: {movie.title()}"
                )
            print_separator()
        else:
            print(message)
    
def ui_search_movie() -> None:
    """
    Run the interactive "Search Movies" screen.

    Guards against an empty database up front, then repeatedly prompts
    the user for a search query, delegates to
    `MovieService.search_movie`, and prints all matching movies
    grouped by genre. The loop continues until the user enters '0' or
    'stop'.

    Returns:
        None
    """
    
    if movies_service.is_empty():
        logger.info("No movies found from the database")
        print_info("No movies found to search, first add movies")
        return
    
    ACTION_MESSAGES = {
        MovieStatus.SUCCESS : "✅️ Movie found successfully",
        MovieStatus.NOT_FOUND : "⚠️ Entered movie not found from the database"
    }
    
    print_header("SEARCH MOVIES", "🔍")
    while True:
        user_movie = input("\nEnter a movie to search (or '0'/'stop' to exit): ").strip()
        if user_movie.lower() in ('stop', '0'):
            print_back_msg()
            break
        
        status, results = movies_service.search_movie(user_movie)
        message = ACTION_MESSAGES.get(status) or COMMON_ERRORS.get(status, f"Unexpected status: {status.name}")
        
        if results:
            print(message)
            total_found = sum(len(m_list) for m_list in results.values())
            plural_suffix = "movies" if total_found != 1 else "movie"
            print_section(f"{total_found} {plural_suffix} matched your query")
            flat_movies = [(genre, movie) for genre, movies_list in results.items() for movie in movies_list]
            for ind, (genre, movie) in enumerate(flat_movies, start=1):
                print(f"  {ind:02d}. 🎬{movie.title()} [{genre.upper()}]")
            print_separator()
        else:
            print(f"{message}")
    
def ui_show_movies() -> None:
    """
    Run the "Show Movies" screen.

    Guards against an empty database up front, then displays the
    entire movie library grouped by genre, including a per-genre movie
    count and a numbered listing of each movie. Unlike the other
    `ui_*` functions, this is a single-pass display screen rather than
    an input loop.

    Returns:
        None
    """
    
    if movies_service.is_empty():
        logger.info("No movies found from the database")
        print_info("No movies found to show, first add movies")
        return
    
    movies = movies_service.get_movies_data()
    
    print_header("MOVIE LIBRARY", "🍿")
    
    for genre, movies_list in movies.items():
        movie_number = len(movies_list)
        plural_suffix = "movies" if movie_number != 1 else "movie"
        
        print_section(f"{genre.upper()} ({movie_number} {plural_suffix})", "🎭")
        
        if movie_number == 0:
            print_info("    (There are no movies in this genre yet!)")
            
        else:
            for ind, movie in enumerate(movies_list, start=1):
                print(f"    {ind:02d}. 🎬{movie.title()}")
        
        print_separator()
    
def ui_delete_movie() -> None:
    """
    Run the interactive "Delete Movie" screen.

    Guards against an empty database up front, then repeatedly prompts
    the user for a movie title to delete. Reuses
    `MovieService.search_movie` to find all matches for the entered
    title: if exactly one match is found, it is proposed directly for
    deletion; if multiple matches exist (e.g., the same or similar
    title across different genres), the user is shown a numbered list
    and asked to pick one. Deletion requires an explicit yes/no
    confirmation before `MovieService.delete_movie` is called. If the
    database becomes completely empty after a deletion, the function
    prints a warning and returns immediately. The loop otherwise
    continues until the user enters '0' or 'stop'.

    Returns:
        None
    """
    
    if movies_service.is_empty():
        logger.info("No movies found from the database")
        print_info("No movies found to delete, first add movies")
        return
    
    ACTION_MESSAGES = {
        MovieStatus.SAVE_ERROR : "⚠️ An error occurred while deleting movies from the database",
        MovieStatus.SUCCESS : "✅️ Movie deleted successfully",
        MovieStatus.NOT_FOUND : "⚠️ Entered movie not found from the database"
    }
    
    print_header("DELETE MOVIES", "🗑")
    
    while True:
        user_movie = input("\nEnter a movie to delete (or '0'/'stop' to exit): ").strip()
        if user_movie.lower() in ("stop", "0"):
            print_back_msg()
            break
        
        status, result = movies_service.search_movie(user_movie)
        message = ACTION_MESSAGES.get(status) or COMMON_ERRORS.get(status, f"Unexpected status: {status.name}")
        if result:
            flat_movies = [(genre, movie) for genre, movies_list in result.items() for movie in movies_list]
            total_found = len(flat_movies)
            plural_suffix = "movies" if total_found != 1 else "movie"
            print_section(
                    f"{total_found} {plural_suffix} matched your query.", "🎯"
                )
            if total_found == 1:
                selected_genre, selected_movie = flat_movies[0]
                
                print(f"   🎬 Movie : {selected_movie.title()}")
                print(f"   🎭 Genre : {selected_genre.title()}")
                print_separator()
                
            else:
                for ind, (genre, movie) in enumerate(flat_movies, start=1):
                    print(f"  {ind:02d}. 🎬{movie.title()} [{genre.upper()}]")
                print_separator()
                    
                selected_genre, selected_movie = None, None
                while True:   
                    user_choice = input("Select the number of movie to delete (or '0'/'stop' to exit): ").strip()
                    if user_choice.lower() in ('stop', '0'):
                        print_back_msg()
                        break
                    
                    elif user_choice.isdigit():
                        choice = int(user_choice)
                        
                        if (1 <= choice <= total_found):
                            selected_genre, selected_movie = flat_movies[choice - 1]
                            break
                        
                        else:
                            print_error(f"Invalid choice, Please choose between 1 and {total_found}")
                        
                    else:
                        print_error("Invalid choice, Please enter a valid number")
                    
                if not selected_movie:
                    break
            
            print(f"\n📌 Target: {selected_movie.title()}")
            is_delete = input(f"\nDelete: '{selected_movie.title()}'?  [yes/no]: ").strip()
            
            if is_delete.lower() in ('yes', 'y'):
                status = movies_service.delete_movie(selected_movie)
                final_message = ACTION_MESSAGES.get(status) or COMMON_ERRORS.get(status, f"Unexpected status: {status.name}")
                
                print(f"\n{final_message}")
                
                if movies_service.is_empty():
                    print_warning("No genres and movies left in the database")
                    return
                
            else:
                print("\n🛑 Deleting cancelled")
        
        else:
            print(f"\n{message}")
            
def ui_exit_app() -> NoReturn:
    """
    Display a goodbye screen and terminate the application.

    Prints a farewell header and message, then exits the process
    immediately via `sys.exit()`. Called when the user selects the
    "exit app" option from the main menu.

    Returns:
        None

    Raises:
        SystemExit: Always raised by `sys.exit()` to terminate the
            program.
    """
    
    print_header("GOODBYE", "👋🏼")
    print_info(f"Thank you for using KRYOS Movie Project, Goodbye 👋🏼")
    sys.exit()
 
    

def main() -> None:
    """
    Run the application's main menu loop.

    Builds a mapping of menu keys ('1'-'6') to their display text and
    corresponding `ui_*` handler function, then repeatedly renders the
    main menu and dispatches the user's selection to the appropriate
    handler. Invalid menu selections are reported without interrupting
    the loop.

    Top-level exception handling ensures the application shuts down
    gracefully:
        - A `KeyboardInterrupt` (Ctrl+C) results in a clean exit with
          status code 0.
        - Any other unhandled exception is logged as a critical error
          (with full traceback) and results in exit with status code 1,
          preventing the raw traceback from being shown to the user.

    Returns:
        None
    """
  
    menu_actions = {
      '1' : {'text' : '🎯 recommend movie', 'func' : ui_recommend_movie},
      '2' : {'text' : '➕️ add movie', 'func' : ui_add_movie},
      '3' : {'text' : '🔍 search movie', 'func' : ui_search_movie},
      '4' : {'text' : '🗑 delete movie', 'func' : ui_delete_movie},
      '5' : {'text' : '🍿 show movies', 'func' : ui_show_movies},
      '6' : {'text' : '🚪 exit app', 'func' : ui_exit_app}
    }
    
    try:
        while True:
            print_header("KRYOS MOVIE PROGRAM")
            print_section("MAIN MENU", "📋")
            for key, value in menu_actions.items():
                print(f"   {key} -> {value['text'].title()}")
            print_separator()
            
            user_choice = input("\n➡️ Choose an action: ").strip()
          
            if user_choice in menu_actions:
                menu_actions[user_choice]['func']()
            
            else:
                print_error("Invalid choice, Please choose only (1 to 6)")
        
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