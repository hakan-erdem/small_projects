import os
import random


# the steps of the hanging part
steps = [
    '''     ______
     |
     |
     |
     |
     |
    |_|''',
    '''     ______
     |   0
     |
     |
     |
     |
    |_|''',
    '''     ______
     |   0
     |   |
     |
     |
     |
    |_|''',
    '''     ______
     |   0
     |  /|
     |
     |
     |
    |_|''',
    '''     ______
     |   0
     |  /|\\
     |
     |
     |
    |_|''',
    '''     ______
     |   0
     |  /|\\
     |   |
     |
     |
    |_|''',
    '''     ______
     |   0
     |  /|\\
     |   |
     |  /
     |
    |_|''',
    '''     ______
     |   0
     |  /|\\
     |   |
     |  / \\
     |
    |_|''',
]

#esay words that contains 6 letters each
easy_words = ["poetry", "recipe", "speech", "writer", "agency", "driver", "county", "health", "throat", "editor",
              "moment", "cancer", "advice", "police", "effort", "member", "method", "office", "breath", "series"]


#the interface

chosen_word = random.choice(easy_words)
word_status = ["_" for _ in range(len(chosen_word))]
wrong_letters = []

wrong_guess = 0
while True:
    os.system('cls||clear')

    print(steps[wrong_guess])
    print("  " + " ".join(wrong_letters))
    print("  " + "".join(word_status))
    user_guess = str(input(" enter a letter: "))

    if user_guess in chosen_word:
        for i in range(len(chosen_word)):
            if user_guess == chosen_word[i]:
                word_status[i] = user_guess

    elif user_guess not in chosen_word:
        wrong_letters.append(user_guess)
        wrong_guess += 1

    if wrong_guess == len(steps)-1:
        os.system('cls||clear')

        print(steps[wrong_guess])
        print("  " + " ".join(wrong_letters))
        print("  " + "".join(word_status))
        print("\nYou're out of lives :(")
        print(f"\nThe word was {chosen_word.upper()}")
        break

    elif "".join(word_status) == chosen_word:
        os.system('cls||clear')

        print(steps[wrong_guess])
        print("  " + " ".join(wrong_letters))
        print("  " + "".join(word_status))
        print("\nCongrats! You found the word.")
        break
