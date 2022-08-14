from higher_lower_game_data import data
import random
import os

def clear():
    os.system('cls')

def pick_data(dic):
    # data 딕셔너리에서 3가지 항목 추출
    name = dic['name']
    description = dic['description']
    country = dic['country']
    return f'{name} , {description}, from {country}'

def check_answer(guess, follower_a, follower_b):
    # 답 체크 
    if follower_a > follower_b:
        return guess == 'A'     # guess 가 A라면 True반환, B라면 False반환/ 어차피 같은 경우는 없음.
    else:
        return guess == 'B'

score = 0 
game_over = False
data_b = random.choice(data)   
 
while not game_over: 
    print(f"You're current score is {score}")
    # 리스트에서 직접 랜덤 추출
    data_a = data_b
    data_b = random.choice(data)
    
    # 앞서 뽑은 data_b가 중복되지않게 하기 위해서 중복되지않을 때까지 반복
    while data_a == data_b:
        data_b = random.choice(data)

    compare = pick_data(data_a)
    against = pick_data(data_b)
    print(f'Compare A : {compare}')
    print(f'Against B : {against}')
    
    guess = input('WHO has more followers? Type A or B: ').upper()
    follower_a = data_a['follower_count']
    follower_b = data_b['follower_count']
    is_correct = check_answer(guess, follower_a, follower_b)

    if is_correct == True:
        score += 1
        print(f"You're score is {score}")
        clear()
    else: 
        print(f"WRONG! You're FINAL score is {score}")
        game_over = True

    
    
    
    
    
### 내가 부족했던 부분
# 1. 리스트에서 랜덤으로 추출 (랜덤 숫자로 하면 번거로움)
# 2. 팔로우 수 비교하는 함수 생성 
# 3. b가 그다음 a가 되도록 


