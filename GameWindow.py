import turtle
import time
from CustomTurtle import CustomTurtle
from helper import *
import random
from Puzzle import Puzzle
from settings import *
from functools import partial
from pprint import pprint
import pickle


class GameWindow:
    
    def __init__(self, title="Game Window", size=WINDOW_SIZE):
        self.window = turtle.Screen()
        self.width, self.height = size
        self.corner = 0 - self.width/2, self.height/2
        self.window.setup(self.width, self.height)
        self.window.title(title)
        self.puzzle = Puzzle("mario.puz")
        self.mode = "LIGHT"
                
        self.start_game()
        
    def set_bg_image(self, path):
        self.window.bgpic(path)
        self.window.update()
    
    def get_input(self, title, prompt):
        n = self.window.textinput(title, prompt)
        if n:
            return n
    
    def get_num_input(self, title, prompt):
        m = turtle.numinput(title, prompt, default=20, minval=5, maxval=200)
        if m: 
            return int(m)
        else: return 20
    
    def display_splash(self, path):
        self.set_bg_image(path)
        time.sleep(SPLASH_LINGER_TIME)
        self.set_bg_image("")
    
    def create_turtle(self):
        return CustomTurtle()

    def draw_board(self, total_moves=10, leaderboard=LEADERS, dark=False):
         
        color = "black" 
        leadercolor = "blue"   
        if dark:
            color = "white"
            leadercolor = "lightblue"
        
        # ----- DRAW BOARDS ------
        # Puzzle board
        self.create_turtle().draw_rectangle(location=LOCATION_PUZZLEBOARD, dimensions=PUZZLEBOARD_SIZE, color=color)
        
        # Leader board
        self.create_turtle().draw_rectangle(location=LOCATION_LEADERBOARD, dimensions=LEADERBOARD_SIZE, color=leadercolor)
        
        # Options board
        self.create_turtle().draw_rectangle(location=LOCATION_OPTIONSBOARD, dimensions=OPTIONSBOARD_SIZE, color=color)
        
        # -------- PLACE BUTTONS -------
        reset = self.create_turtle()
        reset.place_image("assets/resources/resetbutton.gif", LOCATION_RESET_BTN)
        
        load = self.create_turtle()
        load.place_image("assets/resources/loadbutton.gif", LOCATION_LOAD_BTN)
        
        quit = self.create_turtle()
        quit.place_image("assets/resources/quitbutton.gif", LOCATION_QUIT_BTN)
        
        # ------ DRAW TEXT ------
        moves = self.create_turtle()
        moves = self.place_text("Moves Remaining:", MOVES_FONT, LOCATION_MOVES_TEXT, turt=moves, color=color)
        moves_counter = self.place_text(f"{self.moves}", MOVES_FONT, LOCATION_MOVESCOUNTER_TEXT, color=color)
        
        self.initialmoves = self.moves
        
        leader = self.place_text("Leaders", LEADERBOARD_TITLE_FONT, LOCATION_LEADERBOARD_TITLE_TEXT, color=leadercolor)
        
        # ------ LEADERBOARD NAMES -------
        X, Y = LOCATION_NAMES_START_TEXT
        for each in leaderboard:
            self.place_text(f"{each} : {leaderboard[each]}", LEADERBOARD_NAMES_FONT, (X, Y), color=leadercolor)
            Y += NAMES_TEXT_DISTANCE
        
        return reset, load, quit, moves_counter, leader
    
    def place_text(self, text, font, coordinates, color="black", turt=CustomTurtle()):
        x, y = self.corner
        X, Y = coordinates
        turt.goto(x + X, y - Y)
        turt.turtle.pencolor(color)
        turt.turtle.write(text, move=False, font=font)
        return turt
       
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
            
        self.update_moves()
        
        won = self.puzzle.swap_pieces(piece, blank)
        
        if won:
            self.win()
            
    def update_moves(self):
        self.moves -= 1
        self.moves_counter.turtle.clear()
        self.place_text(f"{self.moves}", MOVES_FONT, LOCATION_MOVESCOUNTER_TEXT, turt=self.moves_counter, color="black")
        if self.moves == 0: 
            self.lost()
            
    def lost(self):
        lost = self.create_turtle()
        lost.place_image("assets/resources/Lose.gif", LOCATION_QUITMESSAGE)
        time.sleep(2)
        self.window.bye()
        
    def win(self):
        moves_used = self.initialmoves - self.moves
        
        self.update_leaders(moves_used)
        
        win = self.create_turtle()
        win.place_image("assets/resources/winner.gif", LOCATION_QUITMESSAGE)  
        time.sleep(2)
        win.turtle.hideturtle()
        win.place_image("assets/resources/credits.gif", LOCATION_QUITMESSAGE)
        time.sleep(2)
        self.window.bye()
     
    def update_leaders(self, moves):
        self.leaders.update({moves: self.name})
        self.save_leaders(self.leaders)
        pprint(self.leaders)
     
    
    def save_leaders(self, data):
        try:
            with open("data.pickle", "wb") as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)

    
    def get_leaders(self):
        try:
            with open("data.pickle", "rb") as f:
                return pickle.load(f)
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)
 
                                
    def start_game(self, x=0, y=0):
        # ------- Display Splash -------
        self.display_splash("assets/resources/splash_screen.gif")

        # # ------- Get Inputs -------
        self.name = self.get_input("Welcome", "Enter your name: ")
        self.moves = self.get_num_input("Moves", "Enter the number of moves you want (5 - 200): ")
        
        # ---- Create Board -----
        self.leaders = {}
        self.leaders = self.get_leaders()
        option_buttons = self.draw_board()
        reset, load, quit, self.moves_counter, self.leader = option_buttons
        
        # ----- Display First Puzzle ------
        self.puzzle.create_puzzle_pieces()
        self.display_round()
        
        # ------ Begin Round -----
        self.begin_round()
        
        # ----- Assign buttons -------
        load.turtle.onclick(self.load_puzzle)
        reset.turtle.onclick(self.reset_game)
        quit.turtle.onclick(self.quit_game)
