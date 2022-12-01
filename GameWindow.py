import turtle
import time
from CustomTurtle import CustomTurtle
from helper import *
import random
from Puzzle import Puzzle
from settings import *
from functools import partial



class GameWindow:
    
    def __init__(self, title="Game Window", size=WINDOW_SIZE):
        self.window = turtle.Screen()
        self.width, self.height = size
        self.corner = 0 - self.width/2, self.height/2
        self.window.setup(self.width, self.height)
        self.window.title(title)
        self.puzzle = Puzzle("mario.puz")
                
        self.start_game()
        
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

    def draw_board(self, total_moves=10, leaderboard=LEADERS):
             
        # ----- DRAW BOARDS ------
        # Puzzle board
        self.create_turtle().draw_rectangle(location=LOCATION_PUZZLEBOARD, dimensions=PUZZLEBOARD_SIZE)
        
        # Leader board
        self.create_turtle().draw_rectangle(location=LOCATION_LEADERBOARD, dimensions=LEADERBOARD_SIZE, color="blue")
        
        # Options board
        self.create_turtle().draw_rectangle(location=LOCATION_OPTIONSBOARD, dimensions=OPTIONSBOARD_SIZE)
        
        # -------- PLACE BUTTONS -------
        reset = self.create_turtle()
        reset.place_image("assets/resources/resetbutton.gif", LOCATION_RESET_BTN)
        
        load = self.create_turtle()
        load.place_image("assets/resources/loadbutton.gif", LOCATION_LOAD_BTN)
        
        quit = self.create_turtle()
        quit.place_image("assets/resources/quitbutton.gif", LOCATION_QUIT_BTN)
        
        # ------ DRAW TEXT ------
        moves = self.place_text(f"Player Moves: {total_moves}", MOVES_FONT, LOCATION_MOVES_TEXT)
        leader = self.place_text("Leaders", LEADERBOARD_TITLE_FONT, LOCATION_LEADERBOARD_TITLE_TEXT, "blue")
        
        # ------ LEADERBOARD NAMES -------
        X, Y = LOCATION_NAMES_START_TEXT
        for each in leaderboard:
            self.place_text(f"{each} : {leaderboard[each]}", LEADERBOARD_NAMES_FONT, (X, Y), "blue")
            Y += NAMES_TEXT_DISTANCE
        
        return reset, load, quit, moves, leader
    
    def place_text(self, text, font, coordinates, color="black"):
        x, y = self.corner
        X, Y = coordinates
        t = self.create_turtle()
        t.goto(x + X, y - Y)
        t.turtle.pencolor(color)
        t.turtle.write(text, move=False, font=font)
        return t
       
    def load_puzzle(self, x, y):
        puz_name = self.get_input("What puzzle?", f"fifteen.puz\nluigi.puz\nmario.puz\nsmiley.puz\nyoshi.puz")
        self.puzzle.clear()
        self.puzzle = Puzzle(puz_name) 
        self.puzzle.create_puzzle_pieces()
        self.display_round(True)
        self.begin_round()
        
    def reset_game(self, x, y):
        self.puzzle.clear()
        self.puzzle = Puzzle(self.puzzle.get_name()) 
        self.puzzle.create_puzzle_pieces()
        self.display_round(False) 
        self.begin_round()
              
    def quit_game(self, x, y):
        self.create_turtle().place_image(QUIT_MESSAGE_PATH, LOCATION_QUITMESSAGE)
        time.sleep(2)
        self.window.bye()
                   
    def display_round(self, shuffled=True):
        
        
        # Do thumbnail stuff
        thumbnail = self.puzzle.get_thumbnail()
        thumb = self.create_turtle()
        thumb.place_image(thumbnail, LOCATION_THUMBNAIL)
        self.puzzle.thumbnail_turtle.append(thumb)
        
        in_line = self.puzzle.length
            
        if shuffled:
            self.puzzle.shuffle()
            
        
        # Get coordinates of first piece
        first = LOCATION_FIRST_PIECE
        dist = DISTANCE_BETWEEN_PIECES
        
        placed = 0
        X, Y = first
        for row in self.puzzle.data:
            
            for piece in row:
                image = piece.img
                turt = piece.turtle
                
                turt.place_image(image, (X, Y))
                
                X += dist
                placed += 1
                
                if placed >= in_line ** 2:
                    turt.turtle.hideturtle()
                    continue
                
            placed = 0
            X = first[0]
            Y += dist
               
    def begin_round(self):
        data = self.puzzle.data
        for row in data:
            for piece in row:
                piece.turtle.turtle.onclick(partial(self.check_swap, piece))
    
    def check_swap(self, piece, x, y):
        neighbours = self.puzzle.get_neighbours(piece)
        blank = self.puzzle.check_swap(neighbours)
        if not blank: return
        won = self.puzzle.swap_pieces(piece, blank)
        if won:
            win = self.create_turtle()
            win.place_image("assets/resources/winner.gif", LOCATION_QUITMESSAGE)  
            time.sleep(2)
            win.turtle.hideturtle()
            win.place_image("assets/resources/credits.gif", LOCATION_QUITMESSAGE)
            time.sleep(2)
            turtle.bye()
        
    def start_game(self, x=0, y=0):
        # ------- Display Splash -------
        # self.display_splash("assets/resources/splash_screen.gif")

        # # ------- Get Inputs -------
        # self.name = self.get_input("Welcome", "Enter your name: ")
        # self.moves = self.get_input("Moves", "Enter the number of moves you want (5 - 200): ")
        
        # ---- Create Board -----
        option_buttons = self.draw_board()
        reset, load, quit, totalmoves, leader = option_buttons
        
        # ----- Display First Puzzle ------
        self.puzzle.create_puzzle_pieces()
        self.display_round()
        
        # ------ Begin Round -----
        self.begin_round()
        
        # ----- Assign buttons -------
        load.turtle.onclick(self.load_puzzle)
        reset.turtle.onclick(self.reset_game)
        quit.turtle.onclick(self.quit_game)