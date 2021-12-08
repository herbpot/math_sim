# from random import*

# user = [i for i in range(1,47)]
# print(user)
# shuffle(user)
# print(user)
# print("---오늘의 복권번호----")
# user = sorted(user[:7])

# print(f"오늘의 복권 수는 {user}입니다.")

# print("---오늘의 복권번호----")

# import random

# b = int(0)
# c = int(0)

# while True :
#     a = random.randint(0,10000)
#     b += 1
#     if b == 5 :
#         c += 1
#         b = []
#     for i in range(c):
#         print(['◼️','◼️','◼️','◼️','◼️'])

# a = 'g i w j d p s k o p b f d n w j o 3 p i 5 2 9 t 4 u r e h o g I _ $ @ _ ) % I W T E P T E K '.split(' ')
# print(len(a))

# from fibo import fib
# print(fib(10))

# a = int(input('층수를 입력하세요 >>>'))
# for i in range(a) :
#     b = ''
#     for l in range(2*i-1) :
#         b +='*'
#     c = ''
#     for k in range(a-i):
#         c += ' '
#     print(c+b)

import turtle as t
import random

def turn_up():
    t.left(2)
def turn_down():
    t.right(2)

def fire():
    ang = t.heading()
    while t.ycor() > 0 :
        t.fd(15)
        t.rt(5)
    d = t.distance(target,0)
    t.sety(random.randint(10,100))
    if d<25:
        t.color("blue")
        t.write("Good!",False,"center",("",15))
        t.color("black")
        t.goto(-200,10)
        t.setheading(ang)
    else :
        t.color("red")
        t.write("Bad",False,"center",(",15"))
        t.color("black")
        t.goto(-200,10)
        t.setheading(ang)

t.goto(-300,0)
t.down()
t.goto(300,0)
target = random.randint(50,150)
t.pensize(3)
t.color("green")
t.up()
t.goto(target-25,2)
t.down()
t.goto(target+25,2)
t.color("black")
t.up()
t.goto(-200,10)
t.setheading(20)
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire,"space")
while True:
    t.listen()