import turtle

class CustomTurtle():
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(10)
    
    def goto(self, x, y):
        self.turtle.penup()
        self.turtle.setpos(x, y)
        self.turtle.pendown()
        return x, y
        
    def draw_rectangle(self,location,dimensions,sc, size=5,color="black",fill=""):
        sc_w, sc_h = sc
        x, y = 0 - sc_w / 2, sc_h / 2
        X, Y = location
        width, height = dimensions
        
        t = self.turtle
        t.fillcolor(fill)
        t.pencolor(color)
        t.pensize(size)
        t.begin_fill()
        
        t.up()
        t.goto(x + X, y - Y)
        t.down()
        
        # draw top
        t.forward(width)

        # draw right
        t.right(90)
        t.forward(height)
        
        # draw bottom
        t.right(90)
        t.forward(width)
        
        # draw left
        t.right(90)
        t.forward(height)
        t.end_fill()
        
        self.goto(x, y)
    