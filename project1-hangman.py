# Encoding: UTF-8
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \  |
           |
    """
]


def hangman():
    clear()
    print("Welcome to Hangman!")
    print("Enter 'exit' to exit the game at any time.")
    
    diff= input("Choose difficulty(easy-e, medium-m, hard-h): ")
    if diff == "e":
        allowed_guesses= 6
    elif diff == "m":
        allowed_guesses= 4
    elif diff == "h":
        allowed_guesses= 2
    elif diff == "exit":
        print("Thanks for playing!")
        exit() 
    else:
        print("Please enter a valid difficulty.")
        hangman()
    guesses= []
    inProgress = True
    clear()
    word= input("Enter a word: ")
    clear()
    attempts = 0
    word= word.upper()
    if word == "EXIT":
        print("Thanks for playing!")
        exit()
    word= list(word)
    word_length= len(word)
    word_display= []
    for i in range(word_length):
        word_display.append("_")
    wrong_guesses= 0
    print(hangman_stages[wrong_guesses])
    print(" ".join(word_display))
    while wrong_guesses < allowed_guesses:
        clear()
        print(hangman_stages[wrong_guesses])
        print(" ".join(word_display))
        print("\n")
        print("Attempts: {}".format(attempts))
        print("Lives: {}".format(allowed_guesses-wrong_guesses))
        print("Guesses: {}".format(", ".join(guesses)))
        
        
        guess= input("\nGuess a letter: ")
        print("\n")
        guess= guess.upper()
        if guess in guesses:
            print("You already guessed that letter.")
            continue
        else:
            guesses.append(guess)
        if guess in word:
            for i in range(word_length):
                
                if guess == word[i]:
                    
                    word_display[i]= guess
                    
            print(" ".join(word_display))
            if "_" not in word_display:
                print("You won!")
                break
        elif guess == "EXIT":
            if inProgress:
                print("You forfeited the game. The word was {}.".format("".join(word)))
                exit()
            else:
                print("Thanks for playing!")
            break
        else:
            wrong_guesses += 1
            print(hangman_stages[wrong_guesses])
            print("Wrong guess! You have {} wrong guesses left.".format(6-wrong_guesses))
    if wrong_guesses == allowed_guesses:

        print("You lost! The word was {}.".format("".join(word)))

hangman()
while True:
    play_again= input("Do you want to play again? (Y/N) ")
    if play_again.upper() == "Y":
        clear()
        hangman()
    elif play_again.upper() == "N":
        break
    else:
        print("Please enter Y or N.")
