import random

print('WELCOME TO HANG MAN')
print('______________________')

word = ["monday", "house", "diamond", "love", "hello"]
# choose a random word
random_word = random.choice(word)

for x in random_word:
    print("_", end=" ")

def man(wrong):
    if(wrong == 0):
        print("\n+----+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+----+")
        print("0   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+----+")
        print("0   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+----+")
        print(" 0  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+----+")
        print(" 0  |")
        print("/|\ |")
        print("   ===")
    elif(wrong == 5):
        print("\n+----+")
        print(" 0  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
        print("\n+----+")
        print(" 0  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")

def print_word(guess):
    counter = 0
    right_letters = 0
    for char in random_word:
        if(char in guess):
            print(random_word[counter], end=" ")
            right_letters +=1
        else:
            print(" ", end=" ")
        counter +=1
    return right_letters

def print_line():
    print("\r")
    for char in random_word:
        print("\u203e", end=" ")

length_of_word_to_guess = len(random_word)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong !=6 and current_letters_right != length_of_word_to_guess):
    print("\nletters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
#     prompt user for input
    letter_guessed = input("\nGuess a letter: ")
#     user is right
    if(random_word[current_guess_index]==letter_guessed):
        man(amount_of_times_wrong)
#         print word
        current_guess_index+=1
        current_letters_guessed.append(letter_guessed)
        current_letters_right = print_word(current_letters_guessed)
        print_line()
#     user was wrong

    else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letter_guessed)
        # update the drawing
        man(amount_of_times_wrong)
        # print word
        current_letters_right = print_word(current_letters_guessed)
        print_line()
print("\nGAME IS OVER.....")