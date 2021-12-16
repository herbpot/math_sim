import matplotlib.pyplot as plt

print('''
공이 튀어오르는 각 횟수당 높이를 수열을 통해 구하고 그래프로 나타내 줍니다
''')

ballhight = float(input("처음 공의 높이 지정>>> "))
print(ballhight)
ballbounce = float(input("튀어오르는 높이 지정>> "))
print(ballbounce)
bouncelate = float(ballbounce/ballhight)
print(bouncelate)
ballhights = []

for i in range(80) :
    ballhights.append(ballhight)
    ballhight = ballhight - (1-bouncelate)*ballhight
    print(ballhight)


print(ballhights)
b = []
for i in range(len(ballhights)):
    b.append(i)
print(len(ballhights)==len(b))
plt.plot(ballhights,b)
# plt.xlim(0,1000)
plt.show()