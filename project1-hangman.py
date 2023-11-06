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
    guesses= []
    inProgress = True
    word= input("Enter a word: ")
    clear()
    word= word.upper()
    word= list(word)
    word_length= len(word)
    word_display= []
    for i in range(word_length):
        word_display.append("_")
    print(" ".join(word_display))
    wrong_guesses= 0
    while wrong_guesses < 6:
        guess= input("Guess a letter: ")
        guess= guess.upper()
        if guess in word:
            for i in range(word_length):
                if guess in guesses:
                    print("You already guessed that letter.")
                    break
                elif guess == word[i]:
                    guesses.append(guess)
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
    if wrong_guesses == 6:

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
