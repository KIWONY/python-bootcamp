import random


from basics.hangman.hangman_art import stages, logo
from basics.hangman.word import word_list


print(logo)

# 목숨값
lives = 6


chosen_word = random.choice(word_list)
length = len(chosen_word)

list = []
guess_list =[]

for i in range(length):
    list.append("_")
print(list)

print("__________________________________________")

while "_" in list:
    guess = input("Guess a letter:").lower()

    if guess in guess_list:
        print("You've already guessed")

    for i in range(length):
        if chosen_word[i] == guess:
            list[i] = guess

    print(list)

    if guess not in chosen_word:
        lives = lives -1
        print(stages[lives])
        if lives == 0:
            print("LOSE")

    guess_list.append(guess)

else:
    print("WIN")

