"""
Unit tests for the MovieValidator class.

This module contains the unit test suite for the validation and
normalization logic implemented by MovieValidator.

The tests verify that movie titles, genres, duplicate entries, and
menu selections are correctly validated, normalized, and rejected
when invalid input is provided. Both successful and unsuccessful
validation paths are covered, including case-insensitive comparisons,
whitespace normalization, empty input, boundary values, and invalid
menu selections.

Each test follows the Arrange-Act-Assert pattern where appropriate
and uses unittest.subTest() when multiple related inputs exercise the
same behavior. This keeps individual test cases isolated while
providing clear failure information for each input.

The test suite is designed to protect the public behavior and return
contracts of MovieValidator without depending on its internal
implementation details.
"""


import unittest
from validators import MovieValidator
from status import MovieStatus

class TestMovieValidator(unittest.TestCase):
    """
    Test suite for the MovieValidator class.

    This test case verifies the complete externally observable behavior
    of MovieValidator, including input normalization, empty-value
    validation, duplicate detection, case-insensitive comparisons,
    numeric menu validation, and boundary conditions.

    Each test method focuses on one specific behavior or validation
    rule and asserts both the validity flag and the returned value or
    MovieStatus error code.
    """
    
    def test_validate_movie_success(self):
        """
        Verify that a valid movie title is accepted and normalized.

        The validator should remove leading and trailing whitespace,
        convert the movie title to lowercase, return True as the
        validation status, and return the normalized title as the
        result.
        """
        
        #Arrange
        movie_name = " John Wick "
        
        expected_result = movie_name.strip().lower()
        
        #Act
        is_valid, result = MovieValidator.validate_movie(movie_name)
        
        #Assert
        self.assertTrue(is_valid)
        self.assertEqual(result, expected_result)
        
    def test_validate_movie_empty_name(self):
        """
        Verify that whitespace-only movie titles are rejected.

        The validator should reject input containing only whitespace
        characters, including spaces, newlines, tabs, and combinations
        of newline and tab characters, and return MovieStatus.EMPTY_MOVIE.
        """
        
        # Arrange
        movie_names = [" ", "\n", "\t", "\n\t", "\t\n"]
        
        # Act & Assert
        for movie in movie_names:
            with self.subTest(movie=movie):
        
                is_valid, result = MovieValidator.validate_movie(movie)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, MovieStatus.EMPTY_MOVIE)
        
    def test_validate_genre_success(self):
        """
        Verify that a valid genre name is accepted and normalized.

        The validator should remove leading and trailing whitespace,
        convert the genre name to lowercase, return True as the
        validation status, and return the normalized genre name.
        """
        
        # Arrange
        genre_name = "  Action "
        
        expected_result = genre_name.strip().lower()
        
        # Act
        is_valid, result = MovieValidator.validate_genre(genre_name)
        
        # Assert
        self.assertTrue(is_valid)
        self.assertEqual(result, expected_result)
        
    def test_validate_genre_empty_genre(self):
        """
        Verify that whitespace-only genre names are rejected.

        The validator should reject genre input containing no
        non-whitespace characters and return MovieStatus.EMPTY_GENRE.
        """
        
        # Arrange
        genre_names = ["  ", "\n", "\t",  "\n\t", "\t\n"]
        
        # Act & Assert
        for genre in genre_names:
            with self.subTest(genre=genre):
                
                is_valid, result = MovieValidator.validate_genre(genre)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, MovieStatus.EMPTY_GENRE)
                
    def test_duplicate_movie_exists(self):
        """
        Verify that existing movie titles are detected case-insensitively.

        The validator should identify a movie as a duplicate when the
        normalized input matches an existing movie title, regardless of
        differences in capitalization or surrounding whitespace.

        A duplicate movie should result in False and
        MovieStatus.DUPLICATE_MOVIE.
        """
        
        # Arrange
        movies_data = {
            "Action" : ["The Matrix", "John Wick"],
            "Comedy" : ["Rush Hour"]
        }
        duplicate_inputs = ["  JOhN wiCK  ", "the matrix ", " RUSH hour"]
        
        # Act & Assert
        for movie in duplicate_inputs:
            with self.subTest(movie=movie):
        
                is_valid, result = MovieValidator.duplicate_movie(movie, movies_data)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, MovieStatus.DUPLICATE_MOVIE)
        
    def test_duplicate_movie_unique(self):
        """
        Verify that new movie titles are accepted and normalized.

        Movie titles that do not exist anywhere in the movie database
        should be considered unique. The validator should return True
        together with the title normalized by stripping surrounding
        whitespace and converting it to lowercase.
        """
        
        # Arrange
        movies_data = {
            "Action" : ["The Matrix", "John Wick"],
            "Comedy" : ["Rush Hour"]
        }
        
        unique_movies = ["  Interstellar ", "  INception", "AGENT 007"]
        
        # Act & Assert
        for movie in unique_movies:
            with self.subTest(movie=movie):
        
                is_valid, result = MovieValidator.duplicate_movie(movie, movies_data)
                
                self.assertTrue(is_valid)
                self.assertEqual(result, movie.strip().lower())
                
    def test_duplicate_movie_empty_database(self):
        """
        Verify that a movie is accepted when the database is empty.

        When no movies exist in the database, any non-empty movie title
        should be considered unique. The validator should return True
        and provide the normalized movie title.
        """
        
        # Arrange
        movies = {}
        new_movie = "Interstellar"
        expected_result = new_movie.strip().lower()
        
        # Act
        is_valid, result = MovieValidator.duplicate_movie(new_movie, movies)
        
        # Assert
        self.assertTrue(is_valid)
        self.assertEqual(result, expected_result)
        
        
    def test_duplicate_genre_exists(self):
        """
        Verify that existing genres are detected case-insensitively.

        The validator should identify a genre as a duplicate when its
        normalized name matches an existing genre key, regardless of
        capitalization or surrounding whitespace.

        A duplicate genre should result in False and
        MovieStatus.DUPLICATE_GENRE.
        """
        
        # Arrange
        genres = {
            "Action" : ["The Matrix", "John Wick"],
            "Drama" : ["The Godfather", "The Shawshank Redemption"],
            "Sci-Fi" : ["Interstellar", "Inception"]
        }
        
        duplicate_genres = ["  Sci-Fi ", "  DRAMA", "  AcTIon"]
        
        # Act & Assert
        for genre in duplicate_genres:
            with self.subTest(genre=genre):
        
                is_valid, result = MovieValidator.duplicate_genre(genre, genres)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, MovieStatus.DUPLICATE_GENRE)
        
    def test_duplicate_genre_unique(self):
        """
        Verify that new genre names are accepted and normalized.

        A genre that does not already exist in the database should be
        considered unique. The validator should return True together
        with the genre name normalized by stripping surrounding
        whitespace and converting it to lowercase.
        """
        
        # Arrange
        genres = {
            "Action" : ["The Matrix", "John Wick"],
            "Drama" : ["The Godfather", "The Shawshank Redemption"],
            "Sci-Fi" : ["Interstellar", "Inception"]
        }
        
        new_genres = [" Horror ", "COMEDY", "aniMATion", "biography"]
        
        # Act & Assert
        for genre in new_genres:
            with self.subTest(genre=genre):
        
                is_valid, result = MovieValidator.duplicate_genre(genre, genres)
                
                self.assertTrue(is_valid)
                self.assertEqual(result, genre.strip().lower())
        
    def test_validate_choice_valid_input_success(self):
        """
        Verify that valid menu selections are accepted and converted to integers.

        The validator should accept digit-only strings whose numeric
        values fall within the inclusive range from 1 to list_length.
        The returned value should be the corresponding integer rather
        than the original string.
        """
        
        # Arrange
        list_length = 10
        choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        
        # Act & Assert
        for choice in choices:
            with self.subTest(choice=choice):
                
                is_valid, result = MovieValidator.validate_choice(list_length, choice)
        
                self.assertTrue(is_valid)
                self.assertEqual(result, int(choice))
                
    def test_validate_choice_letters_returns_invalid_format(self):
        """
        Verify that non-digit menu input is rejected as invalid format.

        The validator should reject input that cannot be interpreted as
        a digit-only string, including decimal numbers, negative values,
        alphabetic characters, whitespace-only input, symbols, and
        explicitly signed positive numbers.

        Each invalid input should return False and
        MovieStatus.INVALID_CHOICE_FORMAT.
        """
        
        # Arrange
        list_length = 10
        invalid_choices = ['12.5', '-3', '-5.6', 'abc', '  ', '@$&', '\n', '\t', '+15']
        
        # Act & Assert
        for choice in invalid_choices:
            with self.subTest(choice=choice):
                
                is_valid, result = MovieValidator.validate_choice(list_length, choice)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, MovieStatus.INVALID_CHOICE_FORMAT)
                
    def test_validate_choice_invalid_choice(self):
        """
        Verify that numeric selections outside the valid range are rejected.

        Digit-only input that successfully passes the format check but
        falls outside the inclusive range from 1 to list_length should
        be rejected with MovieStatus.INVALID_CHOICE.
        """
        
        # Arrange
        list_length = 3
        invalid_choices = ['0', '4', '5']
        
        # Act & Assert
        for choice in invalid_choices:
            with self.subTest(choice=choice):
                
                is_valid, result = MovieValidator.validate_choice(list_length, choice)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, MovieStatus.INVALID_CHOICE)
                
    def test_validate_choice_single_item_boundary(self):
        """
        Verify the lower and upper valid boundary for a single-item list.

        When exactly one selectable item exists, the only valid choice
        is "1". The validator should accept this value and return the
        integer 1.
        """
        
        # Arrange & Act
        is_valid, result = MovieValidator.validate_choice(1, '1')
        
        # Assert
        self.assertTrue(is_valid)
        self.assertEqual(result, 1)
        
    def test_validate_choice_empty_list(self):
        """
        Verify that no menu selection is valid when the list is empty.

        When list_length is zero, every numeric selection is outside
        the valid range. The validator should therefore reject each
        selection with MovieStatus.INVALID_CHOICE.
        """
        
        # Arrange
        choices = ['1', '2', '3']
        
        # Act & Assert
        for ch in choices:
            with self.subTest(ch=ch):
                
                is_valid, result = MovieValidator.validate_choice(0, ch)
                
                self.assertFalse(is_valid)
                self.assertEqual(result, MovieStatus.INVALID_CHOICE)
                
if __name__ == "__main__":
    unittest.main()