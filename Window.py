import turtle
import time

class GameWindow:
    def __init__(self, title="Game Window", width=800, height=450):
        self.window = turtle.Screen()
        turtle.setup(width, height)
        turtle.title(title)
    
    def set_bg_image(self, path):
        self.window.bgpic(path)
        self.window.update()
    
    def get_input(self, title, prompt):
        return self.window.textinput(title, prompt)

    def display_splash(self, path):
        self.set_bg_image(path)
        time.sleep(3)
        self.set_bg_image("")

    
    