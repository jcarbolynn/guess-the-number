from art import logo

#global constant for levels
EASY_LEVEL = 10
HARD_LEVEL = 5

turns = 0
def checkAnswer(guess, answer, turns):
  '''checks answer against guess, returns number of turns remaining'''
  if guess > answer:
    print("Too high")
    return turns -1
  elif guess < answer:
    print("Too low")
    return turns -1
  else:
    print(f"You got it! The answer was {answer}.")

def setDifficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL

print(logo)

#put game functionality inside own function
def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  import random
  answer = random.randint(1, 100)
  print(f"Psst, the correct answer is {answer}")
  
  #function to set difficulty
  turns = setDifficulty()
  
  
  #user guess number
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Guess a number: "))
    #because checkAnswer() returns number of turns, save it to the turns variable
    #doesnt need to be global because not in new function from where turns declared
    turns = checkAnswer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()

#function to check user guess against number

#track number of turns and reduce by 1 if wrong guess

# repeat guessing if wrong guess and still have turns left
