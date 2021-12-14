import matplotlib.pyplot as plt
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