class pebo() :
    def __init__(self,a : int ,b : int) :
        self.list = [a,b]

    def next(self) :
        self.list.append(self.list[-2]+self.list[-1])

    def getlist(self):
        return self.list

main = pebo(1,1)
leng_or = 0
p=print
for i in range(4):
    while main.getlist().__len__() != 100000:
        main.next()
    list_ = main.getlist()
    leng = list_.__len__()
    leng_or += leng
    p(i)
    main = pebo(list_[-2],list_[-1])


with open('./pebo400000.txt','w') as F:
    F.write(str(main.getlist()[-1]))