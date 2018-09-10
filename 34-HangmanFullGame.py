import random 
import re
import sys

def random_word():
    lst_words = []
    with open('sowpods.txt', 'r') as f:
        words_read = f.readline()
        while words_read:
            lst_words.append(words_read)
            words_read = f.readline()
        word_selected = str(lst_words[random.randint(0,len(lst_words)-1)])
        return word_selected
    

def user_input_guess():
    letter = input("Guess your letter: \n")
    if re.match("^[a-zA-Z]*$", letter) and len(letter) == 1:
        print("Nice input!")
        return letter
    else:
        print("Please letters from A to Z and only 1 character/letter!")
        user_input_guess()

def generate_result_string(word, letters_guessed):
    result = []
    for letter in word:
        if letter in letters_guessed: 
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)


def restart_func():
    try:
        restart_option = input("Do you want to restart the game again? Insert yes or no! \n")
        if restart_option in ["Yes", "YES", "y", "yes"]:
            main()
        elif restart_option in ["No", "NO", "n", "no"]:
            sys.exit()
    except TypeError as f:
        print(f)
        print("Wrong inputs, Insert Yes or No! Please")
        restart_option()


def main():
    WORD = random_word()
    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0


    print("****Hangman Game****")
    while (len(letters_to_guess) > 0) and num_guesses < 10:
        guess = user_input_guess()
        print(guess)
        if guess  in correct_letters_guessed or guess in incorrect_letters_guessed:
            print("Already used that letter!")
            continue
        if guess in letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            num_guesses += 1

        result_string = generate_result_string(WORD, correct_letters_guessed)
        print(result_string)
        print(f"Remaining guesses: {10 - num_guesses}! ")

    if num_guesses < 10:
        print(f"You won, the word is {WORD}!")
    else:
        print(f"No more remaining tries available!You lost! The word was {WORD}\n")
        restart_func()



main()




      