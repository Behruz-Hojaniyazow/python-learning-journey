import random

class RecommenderSystem:
    """A movie recommendation system for KRYOS users."""
    
    def __init__(self, movies_db):
        self.movies_db = movies_db
        
    def _calculate_algorithm(self, genre):
        """
        Calculates the algorithm based on the entered genre and selects one random movie.
        Returns None if the genre is not in the database.
        """
        
        if genre in self.movies_db and self.movies_db[genre]:
            return random.choice(self.movies_db[genre])
        return None
        
    def get_recommendation(self, genre):
        """Returns a movie recommendation or a fallback message if the genre is missing."""
        
        selected_movie = self._calculate_algorithm(genre)
        if selected_movie:
            return selected_movie
        
        return f"Sorry, Currently we have no movies in the genre '{genre}'"

def main():
    """The main launch point of the program (Entry point)"""
    
    movies_data = {
        "Action": ["John Wick", "Fast and Furious", "Mad Max"],
        "Sci-Fi": ["Avatar", "Interstellar", "Inception"],
        "Comedy": ["Mr.Bean", "Home Alone", "The Mask"],
        "Horror": ["It", "The Conjuring"]
    }
    target_genre = "Comedy"
    movies_system = RecommenderSystem(movies_data)
    recommended_movie = movies_system.get_recommendation(target_genre)
    
    print("--- 🎬 Welcome to KRYOS Movie Recommender System🎬 ---")
    print(f"\nWe recommend you to watch '{recommended_movie}' movie")
    print("Enjoy your view 🍿")

if __name__ == "__main__":        
    main()