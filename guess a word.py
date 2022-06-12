import random
from words import words
import string


def get_random_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def guess_a_word():
    word = get_random_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0:
        print('You have used these letters: ',' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter) 
                print('')

            else:
                print("Your letter '", user_letter ,"' have not in word. Guess another letter :)\n")

        elif user_letter in used_letters:
            print("You already use that letter.")

        else:
            print("That is not a valid letter.\n")
    else:
        print("Congrats, You find the word!\nword = {}".format(word))

if __name__ == '__main__':
    guess_a_word()
