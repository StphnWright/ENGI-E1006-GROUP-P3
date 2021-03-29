"""
A program to read and store a list of words to play a game of Hangman. The
computer randomly selects a word and allows the user to guess the word or 
individual letters, a player loses after more than five incorrect guesses. 
"""

import random
f = open('dictionary.txt', 'r')
dictionary = f.readlines()


def get_word():
    while True:
        word = random.choice(dictionary)
        if len(word) > 4:  # ensures that the word is at least four letters
            return word.upper().strip()


def play(word):
    guessed = False
    guessed_letters = []
    current_guess = ['_'] * len(word)
    
    tries = 6
    print("Let's play a game of Hangman! \n")
    print("If you guess incorrectly more than five times, you lose... ")
    print(display_hangman(tries))
    print(" ".join(current_guess))
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper().strip()
        
        if len(guess) == 1 and guess.isalpha():
            
            if guess in guessed_letters:
                print("\nYou already guessed the letter", guess, "\n")
            
            elif guess in word:
                print("\n", guess, "is in the word ")
                
                for index, letter in enumerate(word):
                    if letter == guess[0]:
                        current_guess[index] = letter
                
                guessed = True
                for letter in current_guess:
                    if letter == '_':
                        guessed = False
                        break
   
            else:
                print("\n", guess, "is not in the word ")
                tries -= 1   
           
            print(display_hangman(tries))
            print(" ".join(current_guess))
            print("\n")
            guessed_letters.append(guess)
        
        else:
            if len(guess) == len(word) and guess.isalpha():
                if guess == word:
                    guessed += 1
                else:
                    tries -= 1
                    print("\nThat is not the right word.\n")
            else:
                print("\nInvalid entry.\n")
    
    if guessed:
        print("\nYou got it! The word was " + word + "\n")
    else:
        print("\nYou're out of tries! The word was " + word + ". Better luck next time!")


def display_hangman(tries):
    stages = [ """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """ ]
    
    return stages[tries]

               
def main():
    word = get_word()
    play(word)
    
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word() 
        play(word)
    else:
        print("\nThanks for playing!")

        
if __name__ == "__main__":
    main()
    
