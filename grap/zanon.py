import matplotlib.pyplot as plt
import math
from time import *

print('''
시그마를 통해 제논의 역설에서 목적지 까지의 남은 거리를 표현한 그래프 입니다 
''')
plus = '''제논의 역설은 거북이가 먼저 출발하면 아무리 빠른 아킬레스라고 해도 거북이를 따라잡을 수 없다는 주장입니다.
아킬레스가 거북이보다 10배 빠르고 100m 뒤에서 달려온다고 가정합니다. 아킬레스가 거북이를 잡기위해100m를 이동하면 거북이는 10m를 이동할겁니다.
또한 거북이를 잡기위해 10m를 이동하면 거북이는 1m를 이동할겁니다. 계속해서 1m를 이동하면 거북이는 0.1m, 0.1m를 이동하면 거북이는 0.01m를 이동합니다.
이처럼 아킬레스가 거북이를 따라잡으면 거북이는 항상 앞서 있기 때문에 거북이를 따라잡을 수 없습니다.

해설:하지만 이 주장은 틀렸습니다. 왜냐하면 아무리 무한한 값을 더해도 이 값은 무한히 커지는 것이 아닌 유한값이기 때문입니다.
아킬레스가 뛴 거리를 더하면100+10+1+0.1+0.01+0.001....=111.11111...입니다. 하지만 이 값은 아무리 더하더라도 112를 넘지는 못할 것 입니다.
아킬레스가 112m를 뛰는 것은 할 수 있을테니 아킬레스는 거북이를 잡을 수 있습니다.'''

while True:
    ans = str(input("제논의 역설에 대한 설명이 필요하신가요?(y/n)"))
    if ans == 'y':
        print(plus)
        sleep(10)
        break
    elif ans == 'n':
        break
    else:
        pass


def sigma(x):
    ret = 0
    c = []
    for val in x:
       ret += val
       c.append(ret)
    return c


b = []

for i in range(5,1000):
        b.append(i/100*100*(1/10))

d = sigma(b)
a = []

for i in range(len(b)):
    a.append(i)

plt.plot(a,b)
plt.ylim(0,300)
plt.xlim(0,a[-1])
plt.show()