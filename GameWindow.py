import turtle
import time
from CustomTurtle import CustomTurtle

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
    
    def __init__(self, title="Game Window", width=WINDOW_SIZE[0], height=WINDOW_SIZE[1]):
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
        time.sleep(SPLASH_LINGER_TIME)
        self.set_bg_image("")
    
    def create_turtle(self):
        return CustomTurtle()

    def draw_board(self, player_name, total_moves, leaderboard):
        board = self.create_turtle()
        
        x = self.X
        y = self.Y
        
        # ----- DRAW BOARDS ------
        # Puzzle board
        w, h = PUZZLEBOARD_SIZE
        X, Y = LOCATION_PUZZLEBOARD
        board.draw_rectangle(x + X, y - Y, w, h, sc=WINDOW_SIZE)
        
        # Leader board
        w, h = LEADERBOARD_SIZE
        X, Y = LOCATION_LEADERBOARD
        board.draw_rectangle(x + X, y - Y, w, h, color="blue", sc=WINDOW_SIZE)
        
        # Options board
        w, h = OPTIONSBOARD_SIZE
        X, Y = LOCATION_OPTIONSBOARD
        board.draw_rectangle(x + X, y - Y, w, h, sc=WINDOW_SIZE)
        
        # -------- DRAW BUTTONS -------
        reset = self.create_turtle()
        X, Y = LOCATION_RESET_BTN
        self.window.addshape("assets/resources/resetbutton.gif")
        reset.turtle.shape("assets/resources/resetbutton.gif")   
        reset.goto(x + X, y - Y)
        reset.turtle.showturtle()
        
        load = self.create_turtle()
        X, Y = LOCATION_LOAD_BTN
        self.window.addshape("assets/resources/loadbutton.gif")        
        load.turtle.shape("assets/resources/loadbutton.gif") 
        load.goto(x + X, y - Y)
        load.turtle.showturtle()
        
        quit = self.create_turtle()
        X, Y = LOCATION_QUIT_BTN
        self.window.addshape("assets/resources/quitbutton.gif")        
        quit.turtle.shape("assets/resources/quitbutton.gif")        
        quit.goto(x + X, y - Y)
        quit.turtle.showturtle()
        
        # ------ DRAW TEXT ------
        moves = self.create_turtle()
        X, Y = LOCATION_MOVES_TEXT
        moves.goto(x + X, y - Y)
        moves.turtle.write(f"Player Moves: {total_moves}", font=MOVES_FONT)
        
        leader = self.create_turtle()
        X, Y = LOCATION_LEADERBOARD_TITLE_TEXT
        leader.goto(x + X, y - Y)
        leader.turtle.pencolor("blue")
        leader.turtle.write(f"Leaders", font=LEADERBOARD_TITLE_FONT)
        
        # ------ LEADERBOARD NAMES -------
        X, Y = LOCATION_NAMES_START_TEXT
        for each in leaderboard:
            t = self.create_turtle()
            t.turtle.pencolor("blue")
            t.goto(x + X, y - Y)
            Y += NAMES_TEXT_DISTANCE
            t.turtle.write(f"{each} : {leaderboard[each]}", font=LEADERBOARD_NAMES_FONT)
    
    # def display_round(self, image):

    # def start_game(self, names, moves):
         
    #     self.display_round(image)
        
             
        