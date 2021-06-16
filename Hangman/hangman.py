from random_word import RandomWords
import random

user_total_tries = 10
user_correct_guesses = 0
user_guesses = []
game_running = True
   
def get_word_to_guess():
    try:
        r = RandomWords()
        words_list = r.get_random_words()
        word_to_guess = words_list[random.randint(0, len(words_list)-1)].lower()
    except TypeError as e:
        print("-----------------------------------------------------------------------------------------")
        print("'random_word' module did not succesfully return a list of words. Picking one from the default list.")
        print("-----------------------------------------------------------------------------------------")
        default_words = ["noiseless", "day", "boring", "holiday", "grieving", "subtract", "love", "whine", "bustling", 
                 "craven", "guttural", "muscle", "choke", "oatmeal", "shrill", "shade", "can", "hilarious", 
                 "discreet", "big"]
        word_to_guess = default_words[random.randint(0, len(default_words)-1)].lower()
    return word_to_guess   

word_to_guess = get_word_to_guess()

def split_word(word):
    return [char for char in word]

def check_user_input(user_input):
    global user_correct_guesses, user_total_tries
    if len(user_input) > 1:
        print("Input only one letter at a time!")
    else:
        user_guesses.append(user_input)
        if user_input in word_to_guess:
            print(f"Correct! '{user_input}' appears {len([x for x in split_word(word_to_guess) if x == user_input])} time(s) in the secret word.")
            user_correct_guesses += len([x for x in split_word(word_to_guess) if x == user_input])
        else:
            print(f"You guessed Wrong! '{user_input}' does not appear in the secret word. Try again!")
            user_total_tries -= 1
            print(f"{user_total_tries} tries left.")

def print_secret_word():
    global word_to_guess
    print("".join([x if x in user_guesses else "_" for x in word_to_guess ]))

def play_again():
    global word_to_guess, user_total_tries, user_correct_guesses, game_running

    play_again_input = input("\nPlay again? Y/N y/n?")
    if play_again_input == 'Y' or play_again_input == 'y':
        word_to_guess = get_word_to_guess()
        user_total_tries = 10
        user_correct_guesses = 0
        user_guesses.clear()
        print_secret_word()

    elif play_again_input == 'N' or play_again_input == 'n':
        game_running = False

def check_game_over():
    global game_running, word_to_guess
    if user_correct_guesses == len(word_to_guess):
        print(f"Congrats! You guessed the secret word: {word_to_guess}!")
        play_again()
    elif user_total_tries == 0:
        print(f"Bad Luck! You did not guess correctly. The secret word was {word_to_guess}.")
        play_again()

print_secret_word()
while game_running:
    user_input = input("\nTry to guess a letter: ")
    check_user_input(user_input)
    print_secret_word()
    check_game_over()







