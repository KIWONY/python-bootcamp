from game_data import data
from random import randrange

#랜덤으로 data에서 뽑아내기 
def pick_data(n):
    name = data[n]['name']
    description = data[n]['description']
    country = data[n]['country']
    return f'{name} , {description}, from {country}'

score = 0 
game_over = False
    
while not game_over:
    # 랜덤 숫자
    index1 = randrange(len(data))
    
    follower1 = data[index1]['follower_count']
    d1 = pick_data(index1)
    print(f'Compare A : {d1}')
    #agianst
    index2 = randrange(len(data))
    # 만약 같은 data를 뽑아냈다면 바꾸기
    if index1 == index2:
        index2 = randrange(len(data))
    follower2 = data[index2]['follower_count']
    d2 = pick_data(index2)
    print(f'Against B : {d2}')
    
    answer = input('WHO has more followers? Type A or B: ')
    if follower1 < follower2 and answer == 'B':
        score += 1 
        print(f"You're score is {score}")
    elif follower1 > follower2 and answer == 'A':
        score += 1
        print(f"You're score is {score}")
    else:
        print(f"WRONG! You're FINAL score is {score}")
        game_over = True
    
    





