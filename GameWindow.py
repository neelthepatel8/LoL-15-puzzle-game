import turtle
import time
from CustomTurtle import CustomTurtle
from helper import *

# ------ Window Dimensions --------
WINDOW_SIZE = 800, 730

# ------- Board Sizes ------
PUZZLEBOARD_SIZE = 480, 480
LEADERBOARD_SIZE = 185, 480
OPTIONSBOARD_SIZE = 710, 115

# ------ Board Locations -------
LOCATION_PUZZLEBOARD = 45, 45
LOCATION_LEADERBOARD = 570, 45
LOCATION_OPTIONSBOARD = 45, 570

# ------- Button Locations -------
BUTTON_START = 500, 630
LOCATION_RESET_BTN = BUTTON_START[0], BUTTON_START[1]
LOCATION_LOAD_BTN = BUTTON_START[0] + 100, BUTTON_START[1]
LOCATION_QUIT_BTN = BUTTON_START[0] + 200, BUTTON_START[1]

# ------ Text Locations -------
LOCATION_MOVES_TEXT = 80, 650
LOCATION_LEADERBOARD_TITLE_TEXT = 615, 190
LOCATION_NAMES_START_TEXT = 615, 220
NAMES_TEXT_DISTANCE = 30

# ------- Text Attributes --------
DEFAULT_FONT = "Arial"
MOVES_FONT = DEFAULT_FONT, 32, "bold"
LEADERBOARD_TITLE_FONT = DEFAULT_FONT, 24, "bold"
LEADERBOARD_NAMES_FONT = DEFAULT_FONT, 16, "normal"

# --------- Even Distance between objects -------
DISTANCE_BETWEEN_OBJECTS = 45

# ----- Splash Screen Settings -----
SPLASH_LINGER_TIME = 3

class GameWindow:
    
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
        
        x, y = self.corner

        # ----- DRAW BOARDS ------
        
        # Puzzle board
        self.create_turtle().draw_rectangle(location=LOCATION_PUZZLEBOARD, dimensions=PUZZLEBOARD_SIZE, sc=WINDOW_SIZE)
        
        # Leader board
        self.create_turtle().draw_rectangle(location=LOCATION_LEADERBOARD, dimensions=LEADERBOARD_SIZE, color="blue", sc=WINDOW_SIZE)
        
        # Options board
        self.create_turtle().draw_rectangle(location=LOCATION_OPTIONSBOARD, dimensions=OPTIONSBOARD_SIZE, sc=WINDOW_SIZE)
        
        # -------- PLACE BUTTONS -------
        reset = self.place_image("assets/resources/resetbutton.gif", LOCATION_RESET_BTN)
        load = self.place_image("assets/resources/loadbutton.gif", LOCATION_LOAD_BTN)
        quit = self.place_image("assets/resources/quitbutton.gif", LOCATION_QUIT_BTN)
        
        # ------ DRAW TEXT ------
        moves = self.place_text(f"Player Moves: {total_moves}", MOVES_FONT, LOCATION_MOVES_TEXT)
        leader = self.place_text("Leaders", LEADERBOARD_TITLE_FONT, LOCATION_LEADERBOARD_TITLE_TEXT, "blue")
        
        # ------ LEADERBOARD NAMES -------
        X, Y = LOCATION_NAMES_START_TEXT
        for each in leaderboard:
            self.place_text(f"{each} : {leaderboard[each]}", LEADERBOARD_NAMES_FONT, (X, Y), "blue")
            Y += NAMES_TEXT_DISTANCE
    
    def place_image(self,image_path, coordinates):
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
    
    def display_round(self, puzzle):
        x, y = self.corner
        
            

    def start_game(self, names, moves, puzzle_name):
        puzzle = generate_puzzle_data(puzzle_name)
        self.display_round(puzzle)
        
             
        