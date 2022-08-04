import os

def clear():
    os.system('cls')

print("Welcome to the secret auction program.")

dic = {}
end = False
while not end:
    name = input("What is your name?:")
    bid = input("What's your bid? $:")
    int_bid = int(bid)
    
    dic[name] = int_bid
    types = input("Are there any other bidders? Type 'yes' or 'no':")   
    if types == 'yes':
        clear()
        end = False
    elif types =='no':
        end = True
else:
    clear()
    max_key = max(dic, key=dic.get)    #딕셔너리에서 value가 최댓값인 key 구하기 
    max_value = dic[max_key]
    print(f"The winner is {max_key} with a bid of ${max_value}")
    
    
# ---강의 정답---

# 최댓값 구하는 함수 
# bidding_record = {"Angela": 123, "James": 321}
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:    # 비교해가면서 최댓값구하기 
            highest_bid = bid_amount
            winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")
