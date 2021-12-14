class linelist :
    def __setitem__(self,key,value):
        return setattr(self,key,value)
    
    def show(self):
        print(self.__dict__)

class lines:
    
    def __init__(self):
        self.Llist = linelist()

    def getlines(self,dot):
        returnline = {}
        for line in self.Llist :
            if line.dot1 == dot or line.dot2 == dot:
                returnline.append(line)
        return

class dot :
    def __init__(self,pos:list):
        #pos = [x,y]
        self.pos = pos

class line(lines) :
    
    def __init__(self,lines:lines):
        self.dot = {}
    def setdot(self,xy:list):
        if not len(self.dot.keys()) == 2:
            self.dot[str(xy)] = dot(xy)
        else:
            print('the line has already 2 dots')

    def setline(self):
        try:
            self.dotkey = list(self.dot.keys())
            print(self.dotkey)
            lines.Llist[self.dot[self.dotkey[0],self.dotkey[1]]] = self
        except Exception as e:
            print(e)


# ans = ''
# while(ans != 'end'):
#     ans = input()
#     try:
#         exec(ans)
#     except Exception as e :
#         print(e)




'''
lines = lines()
linea = line(lines)
linea.setdot([1,3])
linea.setdot([3,5])
linea.setline()
print(lines.Llist)

'''