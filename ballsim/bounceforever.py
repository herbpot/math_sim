import matplotlib.pyplot as plt

ballhight = float(input("처음 공의 높이 지정>>> "))
ballbounce = float(input("튀어오르는 높이 지정>> "))
bouncelate = float(ballbounce/ballhight)
ballhights = []

while ballhight > 5e-324 :
    ballhights.append(ballhight)
    ballhight = ballhight - (1-bouncelate)*ballhight


b = []
for i in range(len(ballhights)):
    b.append(i)
plt.plot(ballhights,b)
# plt.xlim(0,1000)
plt.show()