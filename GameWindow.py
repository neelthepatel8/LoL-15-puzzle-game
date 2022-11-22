import turtle
import time
from CustomTurtle import CustomTurtle

class GameWindow:
    
    def __init__(self, title="Game Window", width=800, height=800):
        self.window = turtle.Screen()
        
        self.X = 0 - width/2
        self.Y = height/2
        
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
    
    def create_turtle(self):
        return CustomTurtle()

    def draw_board(self, player_name, total_moves, leaderboard):
        board = self.create_turtle()
        
        x = self.X
        y = self.Y
        
        board.draw_rectangle(x + 45, y - 45, 480, 550, 5, "black", "",x,y)
        board.draw_rectangle(x + 570, y - 45, 185, 550, 5, "blue", "",x,y)
        board.draw_rectangle(x + 45, y - 640, 710, 115, 5, "black", "",x,y)
        
        reset = self.create_turtle()
        self.window.addshape("assets/resources/resetbutton.gif")
        reset.turtle.shape("assets/resources/resetbutton.gif")   
        reset.goto(x + 495, y - 700)
        reset.turtle.showturtle()
        
        load = self.create_turtle()
        self.window.addshape("assets/resources/loadbutton.gif")        
        load.turtle.shape("assets/resources/loadbutton.gif") 
        load.goto(x + 595, y - 700)
        load.turtle.showturtle()
        
        quit = self.create_turtle()
        self.window.addshape("assets/resources/quitbutton.gif")        
        quit.turtle.shape("assets/resources/quitbutton.gif")        
        quit.goto(x + 695, y - 700)
        quit.turtle.showturtle()
        
        moves = self.create_turtle()
        moves.goto(x + 80, y - 720)
        moves.turtle.write(f"Player Moves: {total_moves}", font=("Arial", 32, "bold"))
        
        leader = self.create_turtle()
        leader.goto(x + 615, y - 187)
        leader.turtle.pencolor("blue")
        leader.turtle.write(f"Leaders", font=("Arial", 24, "bold"))
        
        count = 227
        for each in leaderboard:
            t = self.create_turtle()
            t.turtle.pencolor("blue")
            t.goto(x + 615, y - count)
            count += 20
            t.turtle.write(f"{each} : {leaderboard[each]}", font=("Arial", 15, "normal"))
    
    # def display_round(self, image):

    # def start_game(self, names, moves):
         
    #     self.display_round(image)
        
             
        