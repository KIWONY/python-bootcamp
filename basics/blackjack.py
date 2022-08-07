import random
import os

def clear():
    os.system('cls')

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def deal_card(n):
    """
    카드 랜덤 뽑기
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.sample(cards,n)
    return card

def calculate_score(m):
    """
    카드 합계 계산 
    """
    sum_cards = sum(m)
    if sum_cards == 21 and len(m) == 2:
        return 0
    elif 11 in m and sum_cards > 21:
        # replace는 문자열에서만 가능하니까
        m.remove(11)
        m.append(1) 
        return sum(m)
    return sum_cards    

def winner(user_score,computer_score):
    """
    점수 비교
    """
    if user_score > computer_score:
        return "WIN"
    elif user_score == computer_score:
        return "DRAW"
    elif user_score == 0:
        return "WIN"
    elif computer_score > 21:
        return "WIN"
    elif user_score > 21:
        return "LOSE"
    elif computer_score == 0:
        return "LOSE, COMPUTER HAS BLACKJACK"
    else:
        return "LOSE"

def play_game():
    
    print("GAME")   

    user = deal_card(2)
    computer = deal_card(2)


    game_over = False
    while not game_over:
        
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        
        print(f"YOUR CARD IS {user}, YOUR SCORE IS {user_score}")
        print(f"COMPUTER CARD IS {computer[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
            
        else:
            answer = input("TYPE 'y' TO GET ANOTHER CARD, TYPE 'n' TO PASS: ")
            if answer == 'y':
                user = user + deal_card(1) # 리스트 합치기
            
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer = computer + deal_card(1)
        computer_score = calculate_score(computer)

    print(f"YOUR FINAL HAND: {user}, FINAL SCORE: {user_score}")
    print(f"COMPUTER'S FINAL HAND: {computer}, FINAL SCORE: {computer_score}")
    print(winner(user_score,computer_score))

play_game()

while input(
        "CONTINUE? TYPE 'y' OR 'n': ") == "y":
    clear()
    play_game()
