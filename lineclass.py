class lines:
    
    class linelist :
        def __setitem__(self,key,value):
            return setattr(self,key,value)
        
        def show(self):
            print(self.__dict__)

    def getlines(self,dot):
        returnline = {}
        for line in self.linelist :
            if line.dot1 == dot or line.dot2 == dot:
                returnline.append(line)
        return
    Llist = linelist()

class dot :
    def __init__(self,pos):
        #pos = [x,y]
        self.pos = pos

class line(lines) :
    
    def __init__(self,lines:lines,dot1:dot,dot2:dot):
        self.dot1 = dot1
        self.dot2 = dot2
        try:
            lines.Llist[str([dot1,dot2])] = self
        except Exception as e:
            print(e)



ans = ''
while(ans != 'end'):
    ans = input()
    try:
        exec(ans)
    except Exception as e :
        print(e)