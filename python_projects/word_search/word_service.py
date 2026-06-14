import sys
import random
from validator import validate_letter
from english_words import create_words
from logger_config import get_logger
from config import STOP_COMMAND

logger = get_logger()
words = create_words()

def exit_app():
  """
  Exit the application gracefully
  """
  print("\nThank you for using Kryos Word Guessing Game! GoodBye!")
  sys.exit()

def select_random_word():
  """
  Select a random word from the word list.
  """
  selected_word = random.choice(words)
  return selected_word.strip().upper()

def display(user_letters, word):
  """
  Display guessed letters and hide unknown letters.
  """
  display_letter = ""
  user_letters = user_letters.upper()
  for letter in word:
    if letter in user_letters:
      display_letter += letter
    
    else:
      display_letter += "_ "
  
  return display_letter
  
def play():
  """
  Start the word guessing game.
  """
  logger.info("Word guessing game started")
  
  word = select_random_word()
  word_letters = set(word)
  user_letters = ""
  attempts = 0
  
  logger.debug(f"Random word selected. Length {len(word)}")
  print("\nI have chosen a word, Can you guess it")
  print(f"I chose a word with {len(word)} letters")
  
  while word_letters:
    attempts += 1
    print(display(user_letters, word))
    if len(user_letters) > 0:
      print(f"Letters which you have entered: '{user_letters}'")
    
    print("\nType 'stop' if you can't find the word!")  
    user_letter = input(f"\nATTEMPT - {attempts} Enter a letter: ").strip().upper()
    
    if user_letter == STOP_COMMAND:
      print("\nGame stopped")
      print(f"The word I chose was '{word}'")
      logger.info("Player stopped the game")
      break
    
    is_valid, result = validate_letter(user_letter)
    if not is_valid:
      print(f"\n❌️ {result}")
      logger.warning(f"Validation failed: {result}")
      continue
    
    if user_letter in user_letters:
      print("You have entered this letter before, Enter a new letter!")
      logger.warning(f"Duplicate letter entered: '{user_letter}'")
      continue
    
    elif user_letter in word:
      word_letters.remove(user_letter)
      print(f"'{user_letter}' letter is correct!")
      logger.info(f"Correct guess: '{user_letter}'")
    
    else:
      print(f"'{user_letter}' letter does not exist in the word")
      logger.info(f"Incorrect guess: '{user_letter}'")
      
    user_letters += user_letter
  
  else:
    print(
      f"\nCongratulations! "
      f"You found the word '{word}' "
      f"in {attempts} attempts"
    )
    logger.info(
      f"Game completed successfully "
      f"in {attempts} attempts"
    )