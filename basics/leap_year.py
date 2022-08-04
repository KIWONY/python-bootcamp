def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    # 윤년이 아니면  
    if is_leap(y) == False:
        return month_days[m-1]
    else:
        # 윤년이면 
        month_days[1] = 29
        return month_days[m-1]
    

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# 강의 정답 함수
# days_in_month함수
def days_in_month_answer(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month == 2:           # 여기서 is_leap(year)은 True
        return 29
    return month_days[month - 1]










