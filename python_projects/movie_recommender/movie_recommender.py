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