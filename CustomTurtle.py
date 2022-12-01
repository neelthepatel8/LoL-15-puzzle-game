import turtle
from settings import *

class CustomTurtle():
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed("fastest")
    
    def goto(self, x, y):
        self.turtle.penup()
        self.turtle.setpos(x, y)
        self.turtle.pendown()
        return x, y
        
    def draw_rectangle(self,location,dimensions, size=5,color="black",fill=""):
        sc_w, sc_h = WINDOW_SIZE
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
    
    def place_image(self, image_path, coordinates):
        x, y = - WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2
        X, Y = coordinates
        turtle.register_shape(image_path)    
        self.turtle.shape(image_path)   
        self.goto(x + X, y - Y)
        self.turtle.showturtle()