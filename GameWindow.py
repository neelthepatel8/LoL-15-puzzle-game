import turtle
import time
from CustomTurtle import CustomTurtle
from helper import *
import random
from Puzzle import Puzzle
import math
from settings import *

class GameWindow:
    
    # Constructor
    def __init__(self, title="Game Window", size=WINDOW_SIZE):
        self.window = turtle.Screen()
        
        self.width, self.height = size
        self.corner = 0 - self.width/2, self.height/2
        
        turtle.setup(self.width, self.height)
        turtle.title(title)
    
    def set_bg_image(self, path):
        self.window.bgpic(path)
        self.window.update()
    
    def get_input(self, title, prompt):
        return self.window.textinput(title, prompt)

    def display_splash(self, path):
        self.set_bg_image(path)
        time.sleep(SPLASH_LINGER_TIME)
        self.set_bg_image("")
    
    def create_turtle(self):
        return CustomTurtle()

    def draw_board(self, total_moves, leaderboard):
             
        # ----- DRAW BOARDS ------
        
        # Puzzle board
        self.create_turtle().draw_rectangle(location=LOCATION_PUZZLEBOARD, dimensions=PUZZLEBOARD_SIZE)
        
        # Leader board
        self.create_turtle().draw_rectangle(location=LOCATION_LEADERBOARD, dimensions=LEADERBOARD_SIZE, color="blue")
        
        # Options board
        self.create_turtle().draw_rectangle(location=LOCATION_OPTIONSBOARD, dimensions=OPTIONSBOARD_SIZE)
        
        # -------- PLACE BUTTONS -------
        reset = self.place_image("assets/resources/resetbutton.gif", LOCATION_RESET_BTN)
        
        load = self.place_image("assets/resources/loadbutton.gif", LOCATION_LOAD_BTN)
        load.turtle.onclick(self.load_puzzle)
        
        quit = self.place_image("assets/resources/quitbutton.gif", LOCATION_QUIT_BTN)
        quit.turtle.onclick(self.quit)
        
        # ------ DRAW TEXT ------
        moves = self.place_text(f"Player Moves: {total_moves}", MOVES_FONT, LOCATION_MOVES_TEXT)
        leader = self.place_text("Leaders", LEADERBOARD_TITLE_FONT, LOCATION_LEADERBOARD_TITLE_TEXT, "blue")
        
        # ------ LEADERBOARD NAMES -------
        X, Y = LOCATION_NAMES_START_TEXT
        for each in leaderboard:
            self.place_text(f"{each} : {leaderboard[each]}", LEADERBOARD_NAMES_FONT, (X, Y), "blue")
            Y += NAMES_TEXT_DISTANCE
    
    def place_image(self, image_path, coordinates):
        x, y = self.corner
        X, Y = coordinates
        t = self.create_turtle()
        self.window.addshape(image_path)        
        t.turtle.shape(image_path)   
        t.goto(x + X, y - Y)
        t.turtle.showturtle()
        return t
    
    def place_text(self, text, font, coordinates, color="black"):
        x, y = self.corner
        X, Y = coordinates
        t = self.create_turtle()
        t.goto(x + X, y - Y)
        t.turtle.pencolor(color)
        t.turtle.write(text, move=False, font=font)
        return t
    
    def load_puzzle(self, _, __):
        puzzle = self.get_input("What puzzle?", f"fifteen.puz\nluigi.puz\nmario.puz\nsmiley.puz\nyoshi.puz")
    
    def quit(self, x, y):
        self.place_image(QUIT_MESSAGE_PATH, LOCATION_QUITMESSAGE)
        time.sleep(2)
        self.window.bye()
                    
    def display_round(self, puzzle):
            
        # Place Thumbnail
        self.place_image(puzzle["thumbnail"], LOCATION_COMPLETED_BANNER_IMG)      
        
        # Get coordinates of first piece
        first = LOCATION_FIRST_PIECE[0] + 98/2 \
            ,  LOCATION_FIRST_PIECE[1] + 98/2

        dist = DISTANCE_BETWEEN_PIECES + 98

        solution, shuffled = shuffle_puzzle(puzzle["images"])
        
        pieces_in_line = math.floor(math.sqrt(int(puzzle["number"])))
         
        pieces = []
        placed = 0
        X, Y = first
        
        for image in shuffled:
            
            t = self.place_image(shuffled[image], (X, Y))
            pieces.append(t)
            
            placed += 1
            if X <= PUZZLEBOARD_SIZE[0] - dist and placed < pieces_in_line:
                X += dist
                
            else:
                placed = 0
                X = first[0]
                Y += dist
        
        return pieces
                     
    def start_game(self, puzzle_name):
        puzzle_dict = generate_puzzle_data("assets/" + puzzle_name)
        puzzle = Puzzle(puzzle_dict["number"], puzzle_dict["name"])
        p = self.display_round(puzzle_dict)