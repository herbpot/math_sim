import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

ax=plt.axes()

ballhight = float(input("처음 공의 높이 지정>>> "))
ballbounce = float(input("튀어오르는 높이 지정>> "))
bouncelate = float(ballbounce/ballhight)
ballhights = []
ballhight_ = 0

while ballhight > 5e-324  :
    ballhights.append(ballhight)
    ballhight = ballhight - (1-bouncelate)*ballhight
    if ballhight == ballhight_:break
    ballhight_ = ballhight


b = []
for i in range(len(ballhights)):
    b.append(i)

# print(ballhights)
# print(b)
plt.xlim(0,100)#len(b)
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.plot(b,ballhights,c='red')
plt.scatter(b,ballhights)
plt.text(b[-1],ballhights[-1],ballhights[-1])
plt.show()