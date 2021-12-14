ballhight = float(input("처음 공의 높이 지정"))
print(ballhight)
ballbounce = float(input("튀어오르는 높이 지정"))
print(ballbounce)
bouncelate = float(ballbounce/ballhight)
print(bouncelate)
ballhights = []

while ballhight > 0 :
    ballhights.append(ballhight)
    ballhight = ballhight - (1-bouncelate)*ballhight
    print(ballhight)

print(ballhights)