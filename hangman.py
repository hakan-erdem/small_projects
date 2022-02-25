import os   # for clearing the terminal to give a better experience to user
import random   # for choosing a random word
import time     # for pausing the script to show to user what did they do wrong


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

#easy words that contains 6 letters each
easy_words = ["poetry", "recipe", "speech", "writer", "agency", "driver", "county", "health", "throat", "editor",
              "moment", "cancer", "advice", "police", "effort", "member", "method", "office", "breath", "series"]

#medium words that contains 8 letters each
medium_words = ["aviation", "ideology", "addicted", "dedicate", "reliable", "vertical", "sandwich", "fragment",
                "coincide", "omission", "headline", "tolerant", "mushroom", "approach", "crossing", "ministry",
                "relative", "handicap", "disclose", "concrete"]

#hard words that contains 11 letters each
hard_words = ["environment", "resignation", "commemorate", "contraction", "replacement",
              "respectable", "advertising", "responsible", "comfortable", "astonishing",
              "fashionable", "progressive", "celebration", "sympathetic", "expectation",
              "transaction", "association", "beneficiary", "incongruous","disposition"]

#the interface
while True:
    os.system('cls||clear')
    print("\t-| WELCOME TO HANGMAN |- \n\nChoose a difficulty:")
    print(" -1 for easy difficulty (words with 6 letters)\n -2 for medium difficulty (words with 8 letters)\
          \n -3 for hard difficulty (words with 11 letters)")

    try:
        difficulty = int(input("Enter your difficulty: "))
        assert difficulty in [1, 2, 3]

        if difficulty in [1, 2, 3]:
            break
    except:
        print("\n Please enter a valid entry (1, 2 or 3)")
        time.sleep(2)

# setting the parameters of the levels
level_title = None
if difficulty == 1:
    chosen_word = random.choice(easy_words)
    level_title = "EASY DIFFICULTY"

elif difficulty == 2:
    chosen_word = random.choice(medium_words)
    level_title = "MEDIUM DIFFICULTY"

else:
    chosen_word = random.choice(hard_words)
    level_title = "HARD DIFFICULTY"

# word_status shows how much letters the user has guessed correctly
word_status = ["_" for _ in range(len(chosen_word))]
wrong_letters = []

wrong_guess = 0
while True:
    os.system('cls||clear')

    print(f"\t{level_title}")
    print(f"\n  {len(chosen_word)} letters")
    print(steps[wrong_guess])
    print("  " + " ".join(wrong_letters))
    print("\n  " + "".join(word_status))

    try:
        user_guess = input(" Enter a letter: ")
        assert user_guess.isalpha(), "\n Please enter a letter"
        assert len(user_guess) > 0, "\n Please type an entry"
        assert len(user_guess) < 2, "\n Please enter only one letter"

        if user_guess.lower() in chosen_word:
            for i in range(len(chosen_word)):
                if user_guess == chosen_word[i]:
                    word_status[i] = user_guess

        elif user_guess.lower() not in chosen_word:
            wrong_letters.append(user_guess.lower())
            wrong_guess += 1

        # out of lives case
        if wrong_guess == len(steps) - 1:
            os.system('cls||clear')

            print(f"\t{level_title}")
            print(f"\n  {len(chosen_word)} letters")
            print(steps[wrong_guess])
            print("  " + " ".join(wrong_letters))
            print("\n  " + "".join(word_status))
            print("\nYou're out of lives :(")
            print(f"\nThe word was {chosen_word.upper()}\n")
            break

        # user wins case
        elif "".join(word_status) == chosen_word:
            os.system('cls||clear')

            print(f"\t{level_title}")
            print(f"\n  {len(chosen_word)} letters")
            print(steps[wrong_guess])
            print("  " + " ".join(wrong_letters))
            print("\n  " + "".join(word_status))
            print("\nCongrats! You found the word.\n")
            break

    except AssertionError as err:
        print(err)
        time.sleep(2)


