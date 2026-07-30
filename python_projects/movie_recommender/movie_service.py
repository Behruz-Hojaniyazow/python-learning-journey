"""
Business logic layer for the Movie Recommender application.

This module defines `MovieService`, the central orchestrator that
coordinates between the persistence layer (`MovieStorage`), the input
validation layer (`MovieValidator`), and the application logger. Every
core feature of the application — recommending, adding, searching for,
and deleting movies — is implemented as a method on this class.

`MovieService` deliberately contains no direct user-interaction code
(no `input()` or `print()` calls); it accepts already-collected raw
input from the UI layer, validates and processes it, and returns a
`MovieStatus` (plus any relevant data) describing the outcome. This
separation keeps the UI layer (`main.py`) free to focus purely on
presentation and menu flow, while all business rules live here.
"""

import random
from models import MovieData
from storage import MovieStorage
from validators import MovieValidator
from logger_config import get_logger
from status import MovieStatus

class MovieService:
    """
    Coordinates movie-related operations between storage, validation,
    and logging.

    `MovieService` acts as the single entry point for all movie
    business logic. It depends on an injected `MovieStorage` instance
    (dependency injection), which decouples this class from any
    specific persistence mechanism — the storage backend could be
    swapped (e.g., from JSON to a database) without requiring changes
    to this class's logic.

    Attributes:
        logger (logging.Logger): Shared application logger used to
            record the outcome of every operation (successes,
            warnings, and errors).
        storage (MovieStorage): The persistence handler used to load
            and save the movie database.
    """
    def __init__(self, storage: MovieStorage) -> None:
        """
        Initialize the service with its required storage dependency.

        Args:
            storage (MovieStorage): The storage handler responsible
                for reading and writing the movie database.
        """
        
        self.logger = get_logger()
        self.storage = storage

    def recommend_movie(self, user_choice_str: str) -> tuple[MovieStatus, dict[str, str]]:
        """
        Recommend a random movie from a user-selected genre.

        Loads the current movie database, validates the user's raw
        genre selection against the number of available genres, and —
        if valid — returns a single randomly chosen movie from that
        genre.

        Args:
            user_choice_str (str): The raw, 1-based genre number
                entered by the user (e.g., "2" to select the second
                genre in the list).

        Returns:
            tuple[MovieStatus, dict]: On success, `(MovieStatus.SUCCESS,
            {genre: movie})` containing the selected genre and the
            recommended movie title. On failure, returns the relevant
            `MovieStatus` (`INVALID_CHOICE_FORMAT`, `INVALID_CHOICE`,
            or `NOT_FOUND` if the genre has no movies) paired with an
            empty dictionary.
        """
        
        
        movies: MovieData = self.storage.load_movies()
        
        genre_names = list(movies.keys())
          
        is_valid, result = MovieValidator.validate_choice(len(genre_names), user_choice_str)
        if not is_valid:
            self.logger.warning(f"Recommending movie failed (Genre error): {result.name}")
            return result, {}
        user_choice = result
            
        selected_genre = genre_names[user_choice -1]
        movies_list = movies.get(selected_genre, [])
        
        if not movies_list:
            self.logger.warning(f"Recommendation failed: No movies found in '{selected_genre}' genre")
            return MovieStatus.NOT_FOUND, {}
            
        chosen_movie = random.choice(movies_list)
            
        self.logger.info(f"Successfully recommended '{chosen_movie}' from '{selected_genre}' genre to user")
        return MovieStatus.SUCCESS, {selected_genre : chosen_movie}
  
    def add_movie(self, user_genre: str, user_movie: str) -> MovieStatus:
        """
        Add a new movie to the database under a given genre.

        Validates both the genre and movie title, checks that the
        movie does not already exist anywhere in the database (case-
        insensitive, across all genres), and then either appends it to
        an existing genre (matched case-insensitively) or creates a
        brand-new genre entry if no match is found. The updated
        database is then persisted to storage.

        Args:
            user_genre (str): The raw genre name entered by the user.
                May refer to an existing genre or introduce a new one.
            user_movie (str): The raw movie title entered by the user.

        Returns:
            MovieStatus: `MovieStatus.SUCCESS` if the movie was added
            and saved successfully; `MovieStatus.EMPTY_GENRE` or
            `MovieStatus.EMPTY_MOVIE` if either input was blank;
            `MovieStatus.DUPLICATE_MOVIE` if the movie already exists;
            `MovieStatus.SAVE_ERROR` if persisting the updated database
            to storage failed.
        """
      
        movies: MovieData = self.storage.load_movies()
                            
        is_valid, result = MovieValidator.validate_genre(user_genre)
        if not is_valid:
            self.logger.warning("Genre name cannot be empty")
            return result
        clean_genre = result
            
        is_valid, result = MovieValidator.validate_movie(user_movie)
        if not is_valid:
            self.logger.warning(f"Movie name cannot be empty")
            return result
        clean_movie = result
      
        is_valid, result = MovieValidator.duplicate_movie(clean_movie, movies)
        if not is_valid:
            self.logger.warning(f"Failed to add movie: '{clean_movie.title()}' already exists in the database")
            return result
            
        existing_genre_key = None
        for g in movies.keys():
            if g.lower() == clean_genre.lower():
                existing_genre_key = g
                break
      
        if existing_genre_key:
            movies[existing_genre_key].append(clean_movie)
      
        else:
            movies[clean_genre] = [clean_movie]
    
        if self.storage.save_movies(movies):
            self.logger.info(f"Successfully added '{clean_movie}' movie")
            return MovieStatus.SUCCESS
      
        return MovieStatus.SAVE_ERROR
  
    def search_movie(self, user_movie: str) -> tuple[MovieStatus, MovieData]:
        """
        Search the database for movies whose titles contain a query string.

        Performs a case-insensitive substring match against every
        movie title across all genres, and groups the matches by the
        genre they belong to.

        Args:
            user_movie (str): The raw search query entered by the
                user (a full or partial movie title).

        Returns:
            tuple[MovieStatus, dict]: `(MovieStatus.SUCCESS, found_movies)`
            where `found_movies` maps each matching genre to a list of
            matching movie titles, if at least one match is found.
            `(MovieStatus.NOT_FOUND, {})` if no movies match the query.
            `(MovieStatus.EMPTY_MOVIE, {})` if the query was blank.
        """
      
        movies: MovieData = self.storage.load_movies()
        
        is_valid, result = MovieValidator.validate_movie(user_movie)
        if not is_valid:
            self.logger.warning("Movie name cannot be empty")
            return result, {}
        clean_movie = result
        
        found_movies: MovieData = {}
        for genre, movies_list in movies.items():
            searching_movies = [
                movie for movie in movies_list
                if clean_movie.lower() in movie.lower()
            ]
            
            if searching_movies:
                found_movies[genre] = searching_movies
            
        if found_movies:
            total_found = sum(len(m_list) for m_list in found_movies.values())
            plural_suffix = "movies" if total_found != 1 else "movie"
            self.logger.info(f"Successfully found {total_found} {plural_suffix} matched to user query")
            return MovieStatus.SUCCESS, found_movies
                  
        self.logger.info(f"Search failed, No movie matched the query {clean_movie.title()}")
        return MovieStatus.NOT_FOUND, {}
        
    def delete_movie(self, user_movie: str) -> MovieStatus:
        """
        Delete the first movie matching the given title from the database.

        Performs a case-insensitive exact match against movie titles
        across all genres. When a match is found, it is removed from
        its genre's list; if that removal empties the genre entirely,
        the genre key itself is also removed from the database. The
        updated database is then persisted to storage.

        Note:
            If the same title were to appear under multiple genres,
            only the first match encountered (in dictionary iteration
            order) is removed per call.

        Args:
            user_movie (str): The raw movie title to delete, as
                entered by the user.

        Returns:
            MovieStatus: `MovieStatus.SUCCESS` if a matching movie was
            found, removed, and the database saved successfully;
            `MovieStatus.EMPTY_MOVIE` if the input was blank;
            `MovieStatus.SAVE_ERROR` if persisting the change failed;
            `MovieStatus.NOT_FOUND` if no matching movie exists.
        """
    
        movies: MovieData = self.storage.load_movies()
      
        is_valid, result = MovieValidator.validate_movie(user_movie)
        if not is_valid:
            self.logger.warning("Movie name cannot be empty")
            return result
        clean_movie = result
          
        for genre, movies_list in list(movies.items()):
            for movie in movies_list:
                if clean_movie.lower() == movie.lower():
                    movies_list.remove(movie)
                    
                    if not movies_list:
                        del movies[genre]
                        
                    if self.storage.save_movies(movies):
                        self.logger.info(f"Successfully deleted {movie.title()}")
                        return MovieStatus.SUCCESS
                    else:
                        self.logger.error("Failed to save changes after deletion")
                        return MovieStatus.SAVE_ERROR
        
        self.logger.warning(f"Delete failed: Movie '{clean_movie.title()}' not found")
        return MovieStatus.NOT_FOUND
  
    def get_movies_data(self) -> MovieData:
        """
        Retrieve the entire movie database as currently stored.

        Returns:
            dict: The full movie database, mapping genre names to
            lists of movie titles.
        """
        
        return self.storage.load_movies()
        
    def is_empty(self) -> bool:
        """
        Check whether the movie database currently contains no genres.

        Returns:
            bool: True if the database has zero genre entries;
            False otherwise. Note that this checks only the number of
            genre keys, not whether individual genres contain movies.
        """
        
        return len(self.get_movies_data()) == 0