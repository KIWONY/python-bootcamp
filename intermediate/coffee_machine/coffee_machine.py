from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 객체 생성
coffee = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_list = coffee.get_items()

machine_off = False
while not machine_off: 
    order = input(f"What would you like?({coffee_list}): ")

    if order == "off":
        machine_off = True
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else: 
        """ 커피를 골랐을 때 """
        item = coffee.find_drink(order)                 
        if coffee_maker.is_resource_sufficient(item):             # True를 반환 시(can_make = True?))
            cost = item.cost       # 원하는 커피의 가격(attribute)
            if money_machine.make_payment(cost):                    # True 반환 시 계산 or 환불 -> 잔돈
                coffee_maker.make_coffee(item)
