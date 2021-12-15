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
        self.on_mouse_clicked(0,0)
        self.window.onclick(self.on_mouse_clicked)

    def on_mouse_clicked(self,x,y):
        self.set
        self.degree1 = self.heading()
        self.goto(x,y)
        self.set_dot(self.toward(x,y))
        self.degree2 = self.degree1

    def set_dot(self,degree):
        self.dot = self.position()
        self.set_line(self.dot,self.dot_,degree)
        self.dot_= self.dot

    def set_line(self,a,b,degree):
        self.line = (a,b,degree)
        self.lines.append(self.line)

    def culS(self):
        self.line1 = self.lines[0]
        self.line2 = self.lines[1]
        self.ss = math.sin(self.line2[2])*self.line1*self.line2/2
        self.write(self.ss)

    def loop(self):
        self.window.mainloop()


        

        
p = T()
p.loop()

