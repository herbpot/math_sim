import turtle
from lineclass import *

class MyTurtle(turtle.Turtle):
    def __init__(self):
        super(MyTurtle, self).__init__()
        self.shapesize(2, 2)
        self.dots = {}
        
        self.lines = lines()

        
        self.window = turtle.Screen()
        self.dot(5)
        self.dots[len(self.dots.keys())] = self.pos()
        self.window.onclick(self.on_mouse_clicked)
        self.window.onkeypress(self.check)

        self.is_moving = False

    def loop(self):
        self.window.mainloop()

    def on_mouse_clicked(self, x, y):
        if self.acquire_lock():
            self.loc = self.jifejifej
            self.dot1 = dot()
            self.goto(x, y)
            self.release_lock()
            self.keys = self.dots.keys()
            print(self.keys)
            for i in range(len(self.keys)):
                self.d = self.distance(self.dots[i])
                print(self.d)
                if(self.d > 3):
                    self.line = line()
                    self.dot2 = dot([x,y])
                    pass
                else:
                    print('same dot')
                    self.setpos(self.dots[i])
                    # self.check()
            self.dot(5)
            self.dots[len(self.keys)] = self.pos()
            print(self.dots)

    def acquire_lock(self):
        if self.is_moving is True:
            return False

        self.is_moving = True
        return True

    def release_lock(self):
        self.is_moving = False
    
    def check(self) :
        for i in self.dots :
            print(i)


t = MyTurtle()
t.loop()