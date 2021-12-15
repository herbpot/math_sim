import turtle as t
import math

class T(t.Turtle):
    def __init__(self):
        super(T, self).__init__()
        self.shapesize(2,2)
        self.window = t.Screen()
        self.lines = []
        self.degree2 = 0
        self.dot_ = self.position()
        self.on_mouse_clicked(1,1)
        self.window.onclick(self.on_mouse_clicked)
        self.window.listen()
        self.window.onkeypress(self.on_keypress,"1")

    def on_mouse_clicked(self,x,y):
        self.setheading(self.towards(x,y))
        self.degree1 = self.heading()
        self.dis = self.distance(x,y)
        self.deg = self.towards(x,y)
        self.goto(x,y)
        self.set_dot(self.deg,self.dis)
        self.degree2 = self.degree1


    def on_keypress(self):
        self.culS()

    def set_dot(self,degree,dis):
        self.dot = self.position()
        self.set_line(self.dot,self.dot_,degree,dis)
        self.dot_= self.dot

    def set_line(self,a,b,degree,dis):
        self.line = (a,b,degree,dis)
        self.lines.append(self.line)

    def culS(self):
        self.line1 = self.lines[0]
        self.line2 = self.lines[1]
        self.ss = abs(math.sin(int(math.floor(self.line2[2])))*self.line1[3]*self.line2[3]/2)
        print(math.floor(self.line1[2]))
        print(self.line1[3])
        print(self.line2[3])
        print(self.ss)
        self.write(self.ss)

    def loop(self):
        self.window.mainloop()


        

        
p = T()
p.loop()

