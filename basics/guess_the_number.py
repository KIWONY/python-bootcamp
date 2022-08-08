from art import guess_the_number
from random import randrange

def choice_level():
    level = input("I'M THINKING OF A NUMBER BETWEEN 1 AND 100. CHOOSE A DIFFICULTY. TYPE 'easy' OR 'hard': ")

    if level == 'easy':
        chance = 10
    else: 
        chance = 5 
    return chance

def compare(guess, number, turn):
    if guess > number:
        print("Too high")
        return turn - 1
    elif guess < number:
        print("Too low")
        return turn - 1
    else: 
        print("You win")
    
def game():
    print(guess_the_number)
    
    number = randrange(100)
    chance = choice_level()
    
    while chance > 0:
        guess = int(input("Make a guess: "))
        chance = compare(guess, number, chance)         # compare함수의 return 값을 chance에 할당
        if chance == 0:
            print("You've run out of guesses, you lose.")
            return
        # 함수종료 
game()
