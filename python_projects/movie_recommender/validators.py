"""
Input validation layer for the Movie Recommender application.

This module defines `MovieValidator`, a collection of static methods
responsible for validating and normalizing raw user input before it
reaches the service or storage layers. Each method follows a
consistent contract: it returns a `(bool, result)` tuple, where the
boolean indicates whether the input was valid, and `result` is either
the cleaned/normalized value (on success) or a `MovieStatus` code
describing the failure reason (on error).

This consistent contract allows calling code in `MovieService` to
handle every validation step uniformly, without needing to catch
exceptions or interpret different return shapes for different checks.
"""

from typing import TypeAlias
from status import MovieStatus
from models import MovieData
ValidateMovieGenre: TypeAlias = tuple[bool, str | MovieStatus]
ValidateChoice: TypeAlias = tuple[bool, int | MovieStatus]

class MovieValidator:
    """
    Stateless collection of validation rules for movie-related input.

    All methods on this class are static, as validation logic here
    depends only on the arguments passed in and requires no instance
    state. This makes `MovieValidator` usable directly via the class
    itself (e.g., `MovieValidator.validate_movie(...)`) without needing
    to instantiate it.
    """

    @staticmethod
    def validate_movie(movie: str) -> ValidateMovieGenre:
        """
        Validate that a movie title is not empty or whitespace-only.

        The input is stripped of leading/trailing whitespace and
        lowercased before the emptiness check, ensuring consistent
        normalization for downstream comparisons (e.g., duplicate
        detection, case-insensitive search).

        Args:
            movie (str): The raw movie title provided by the user.

        Returns:
            tuple[bool, str | MovieStatus]: `(True, cleaned_movie)` if
            the title is valid; `(False, MovieStatus.EMPTY_MOVIE)` if
            the title is empty or contains only whitespace.
        """
          
        cleaned_movie = movie.strip().lower()
        if not cleaned_movie:
            return False, MovieStatus.EMPTY_MOVIE
          
        return True, cleaned_movie
    
    @staticmethod  
    def validate_genre(genre: str) -> ValidateMovieGenre:
        """
        Validate that a genre name is not empty or whitespace-only.

        The input is stripped of leading/trailing whitespace and
        lowercased before the emptiness check, ensuring consistent
        normalization for downstream comparisons (e.g., matching
        against existing genre keys).

        Args:
            genre (str): The raw genre name provided by the user.

        Returns:
            tuple[bool, str | MovieStatus]: `(True, cleaned_genre)` if
            the genre name is valid; `(False, MovieStatus.EMPTY_GENRE)`
            if the name is empty or contains only whitespace.
        """

          
        cleaned_genre = genre.strip().lower()
        if not cleaned_genre:
            return False, MovieStatus.EMPTY_GENRE
          
        return True, cleaned_genre
    
    @staticmethod  
    def duplicate_movie(user_input: str, movies: MovieData) -> ValidateMovieGenre:
        """
        Check whether a movie already exists anywhere in the database.

        The comparison is case-insensitive and searches across every
        genre's movie list, ensuring the same title cannot be added
        twice under different genres.

        Args:
            user_input (str): The movie title to check for duplicates.
            movies (dict): The full movie database, mapping genre
                names (str) to lists of movie titles (list[str]).

        Returns:
            tuple[bool, str | MovieStatus]: `(False, MovieStatus.DUPLICATE_MOVIE)`
            if a case-insensitive match is found in any genre;
            `(True, target_movie)` with the normalized title if the
            movie is unique.
        """

          
        target_movie = user_input.strip().lower()
      
        for movies_list in movies.values():
            if any(m.lower() == target_movie for m in movies_list):
                return False, MovieStatus.DUPLICATE_MOVIE
        
          
        return True, target_movie
    
    @staticmethod  
    def duplicate_genre(user_input: str, movies: MovieData) -> ValidateMovieGenre:
        """
        Check whether a genre already exists in the database.

        The comparison is case-insensitive against the existing genre
        keys of the movie database.

        Args:
            user_input (str): The genre name to check for duplicates.
            movies (dict): The full movie database, whose keys are the
                existing genre names.

        Returns:
            tuple[bool, str | MovieStatus]: `(False, MovieStatus.DUPLICATE_GENRE)`
            if a case-insensitive match already exists;
            `(True, target_genre)` with the normalized genre name if
            it is new.
        """
          
        target_genre = user_input.strip().lower()
        if any(genre.lower() == target_genre for genre in movies.keys()):
            return False, MovieStatus.DUPLICATE_GENRE
          
        return True, target_genre
        
    @staticmethod   
    def validate_choice(list_length: int, user_choice: str) -> ValidateChoice:
        """
        Validate a user's numeric menu selection against a valid range.

        The raw input is first checked to ensure it consists only of
        digits (rejecting empty strings, letters, or negative-sign
        input, since `str.isdigit()` does not accept a leading '-').
        The parsed integer is then checked to fall within the inclusive
        range `[1, list_length]`, matching the 1-based numbering used
        throughout the application's menus.

        Args:
            list_length (int): The number of selectable items
                currently available (e.g., number of genres),
                defining the upper bound of a valid choice.
            user_choice (str): The raw string input entered by the
                user in response to a numbered menu prompt.

        Returns:
            tuple[bool, int | MovieStatus]: `(False, MovieStatus.INVALID_CHOICE_FORMAT)`
            if the input is not a valid digit string;
            `(False, MovieStatus.INVALID_CHOICE)` if the parsed number
            falls outside the valid range; `(True, choice)` with the
            parsed integer if the selection is valid.
        """

        
        if not user_choice.isdigit():
            return False, MovieStatus.INVALID_CHOICE_FORMAT
            
        choice = int(user_choice)
            
        if not (1 <= choice <= list_length):
            return False, MovieStatus.INVALID_CHOICE
            
        return True, choice