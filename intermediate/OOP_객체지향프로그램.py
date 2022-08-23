"""
import another_module
another_module.another_variable
"""
   
from turtle import Turtle, Screen

# 클래스로부터 객체 생성 -> 그것을 timmy라는 변수에 담음.
timmy = Turtle()        
# 객체 = 클래스()
# print(timmy) = <turtle.Turtle object at 0x0000024F8C8C5700> =  객체 

my_screen = Screen()
# 객체의 속성불러오기
my_screen.canvheight
# canvheight은 객체 my_screen의 속성(attribute)

# 메소드 실행
timmy.shape("turtle")
timmy.color('pink')
timmy.speed(10)
timmy.forward(100)
timmy.right(60)
timmy.backward(30)
print(timmy.position())     # (85.00,25.98)
timmy.home()
timmy.circle(140,110)

timmy.pendown()
my_screen.exitonclick()
