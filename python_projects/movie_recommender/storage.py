"""
Persistence layer for the Movie Recommender application.

This module defines `MovieStorage`, the sole component responsible for
reading and writing the movie database to disk as JSON. It abstracts
away all file I/O and error handling so that the rest of the
application (the service and UI layers) can work with a plain Python
dictionary without needing to know anything about file paths, JSON
serialization, or disk-related failure modes.

The class also provides a built-in default dataset, ensuring the
application has meaningful sample data available on first run, before
the user has added anything of their own.
"""

import json
from logger_config import get_logger
from models import MovieData

class MovieStorage:
    """
    Handles all disk persistence for the movie database.

    `MovieStorage` is a thin data-access layer around a single JSON
    file. It is responsible for loading the movie database into
    memory, saving it back to disk, and providing a default dataset
    when no database file yet exists. All I/O errors are caught and
    logged internally so that calling code can rely on simple return
    values (`dict` or `bool`) instead of handling exceptions directly.

    Attributes:
        file_name (str): Path to the JSON file used for persistence.
        logger (logging.Logger): Shared application logger used to
            record warnings and errors encountered during file I/O.
    """
    
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.logger = get_logger()
        
    @staticmethod
    def get_default_movies() -> MovieData:
        """
        Build and return the default (seed) movie database.

        This dataset is used to populate the application the first
        time it runs — that is, whenever the underlying JSON file
        does not yet exist on disk. It provides a small, ready-to-use
        library so the user can immediately explore features like
        recommending, searching, and browsing movies.

        Returns:
            dict: A dictionary mapping genre names (str) to lists of
            movie titles (list[str]).
        """
      
        movies = {
          "action": ["John Wick", "Extraction", "Mad Max", "The Dark Knight", "Inception"],
          "comedy": ["Mr Bean", "Home Alone", "The Mask", "Rush Hour", "Hangover"],
          "horror" : ["It" , "Conjuring", "Get Out", "Insidious", "A Quiet Place"],
          "drama" : ["The Shawshank Redemption", "Forrest Gump", "The GodFather", "The Pursuit of Happyness", "Interstellar"],
          "sci-fi" : ["Avatar", "The Matrix", "Dune", "Blade Runner 2049", "Tenet"]
        }
        
        return movies
    
    def load_movies(self) -> MovieData:
        """
        Load the movie database from the JSON storage file.

        If the target file does not yet exist, this method transparently
        bootstraps the application by generating the default movie
        database (via `get_default_movies`) and immediately persisting
        it to disk, so subsequent calls will find the file in place.

        All failure modes — a missing file, a corrupted/invalid JSON
        structure, or any other unexpected I/O error — are caught and
        logged internally rather than propagated, so callers can always
        expect a `dict` return value without needing to wrap this call
        in a try/except block.

        Returns:
            dict: The loaded movie database, mapping genre names to
            lists of movie titles. Returns an empty dictionary if the
            file is corrupted, cannot be created, or an unexpected
            error occurs.
        """
        
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                movies: MovieData = json.load(file)
              
                return movies
            
        except FileNotFoundError:
            # It is normal for file not to exist (when opened for the first time) this can be done with a small warning (DEBUG)
            self.logger.debug(f"'{self.file_name}' not found, Initializing with default movies")
            default_movies = self.get_default_movies()
            if self.save_movies(default_movies):
                return default_movies
                
            return {}
          
        except json.JSONDecodeError as e:
            # JSON STRUCTURE is corrupted - this is a serious error!
            self.logger.exception(f"Invalid JSON format - {e}")
            
            return {}
          
        except Exception:
            self.logger.exception(f"Unexpected error occured in (load_movies)")
            
            return {}
          
    def save_movies(self, movies: MovieData) -> bool:
        """
        Persist the movie database to the JSON storage file.

        The dictionary is written to disk as pretty-printed JSON
        (4-space indentation) with `ensure_ascii=False` so that
        non-ASCII movie or genre titles are stored in a
        human-readable form rather than as escape sequences.

        Args:
            movies (dict): The movie database to persist, mapping
                genre names (str) to lists of movie titles (list[str]).

        Returns:
            bool: True if the data was written to disk successfully;
            False if an `IOError` or any other unexpected error
            occurred while saving (the error is logged internally).
        """
          
        try:
            
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(
                    movies,
                    file,
                    indent=4,
                    ensure_ascii=False
                )
            return True
              
        except IOError as e:
            self.logger.exception(f"File error - {e}")
            return False
            
        except Exception:
            self.logger.exception(f"An error occured while saving movies")
            return False