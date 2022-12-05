import turtle
import time
from CustomTurtle import CustomTurtle
from helper import *
from Puzzle import Puzzle
from settings import *
from functools import partial
import pickle
import os

class GameWindow:
    def __init__(self, title="Game Window", size=WINDOW_SIZE):
        self.window = turtle.Screen()
        self.width, self.height = size
        self.corner = 0 - self.width/2, self.height/2
        self.window.setup(self.width, self.height)
        # self.window.screensize(sizex, sizey)
        # self.window.setup(width=1.0, height=1.0, startx=None, starty=None)
        self.window.title(title)
        self.puzzle = Puzzle("masteryi.puz")
        self.mode = "LIGHT"
        self.leaders = {}
                
        self.start_game()
        
    def set_bg_image(self, path):
        """Sets the background image and updates window

        Args:
            path (str): path of image
        """
        self.window.bgpic(path)
        self.window.update()
    
    def get_input(self, title, prompt):
        """Gets a string input from user

        Args:
            title (str): Title of window
            prompt (str): Input question

        Returns:
            str: user input
        """
        n = self.window.textinput(title, prompt)
        if n:
            return n
    
    def get_num_input(self, title, prompt):
        """Gets number input from user

        Args:
            title (str): Title of the window
            prompt (str): input question

        Returns:
            int: user input number
        """
        m = turtle.numinput(title, prompt, default=20, minval=5, maxval=200)
        if m: 
            return int(m)
        else: return 20
    
    def display_splash(self, path):
        """Displays the splash screen for some time

        Args:
            path (str): path of the splash image
        """
        self.set_bg_image(path)
        time.sleep(SPLASH_LINGER_TIME)
        self.set_bg_image("")
    
    def create_turtle(self):
        """Creates a custom turtle on the board

        Returns:
            turtle object: Object of a custom turtle
        """
        return CustomTurtle()
             
    def draw_board(self):
        """Draws the main gui of the game

        Returns:
            button objects: All buttons created
        """
        self.set_bg_image(BG_IMG)
        color = "black"
        leadercolor = "black"   
        
        # ----- DRAW BOARDS ------
        # Puzzle board
        # self.create_turtle().draw_rectangle(location=LOCATION_PUZZLEBOARD, dimensions=PUZZLEBOARD_SIZE, color=color)
        
        # Leader board
        # self.create_turtle().draw_rectangle(location=LOCATION_LEADERBOARD, dimensions=LEADERBOARD_SIZE, color=leadercolor)
        
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
        
        leader = self.create_turtle()
        leader = self.place_text("Leaders", LEADERBOARD_TITLE_FONT, LOCATION_LEADERBOARD_TITLE_TEXT, turt=leader, color=leadercolor)
        
        # ------ LEADERBOARD NAMES -------
        X, Y = LOCATION_NAMES_START_TEXT
        leaders = []
        for leader in self.leaders:
            leaders.append([leader, self.leaders[leader]])
        
        names = self.create_turtle()
        for each in sorted(leaders):
            names = self.place_text(f"{each[0]} : {each[1]}", LEADERBOARD_NAMES_FONT, (X, Y), turt=names, color=leadercolor)
            Y += NAMES_TEXT_DISTANCE
        
        return reset, load, quit, moves_counter, leader
    
    def place_text(self, text, font, coordinates, color="black", turt=CustomTurtle()):
        """Places a text on screen

        Args:
            text (str): Text
            font (tuple): Font options
            coordinates (tuple): x, y coordinates where text is
            color (str, optional): Color of text. Defaults to "black".
            turt (turtle, optional): Turlte object. Defaults to CustomTurtle().

        Returns:
            object: turtle object that wrote text
        """
        x, y = self.corner
        X, Y = coordinates
        turt.goto(x + X, y - Y)
        turt.turtle.pencolor(color)
        turt.turtle.write(text, move=False, font=font)
        return turt
                  
    def load_puzzle(self, x, y):
        """Loads a new puzzle from given list of puzzles

        Args:
            x (int): Passed not used
            y (int): Passed not used
        """
        names = ""
        puz_files = os.listdir("assets")
        
        if len(puz_files) > 15:
            with open("5001_puzzle.err", 'w') as file:
                file.write(f"{time.localtime()} WARNING More than 15 puzzles exist, loading first 15. func.load_puzzle()")
                
        for puz in puz_files:
            if puz.endswith(".puz"):
                names += f"{puz}\n"
                
        puz_name = self.get_input("What puzzle?", names)
        
        puzzle2 = Puzzle(puz_name) 
        if puzzle2.error:
            self.file_error()
            with open("5001_puzzle.err", 'w') as file:
                file.write(f"{time.localtime()} ERROR Cannot find the puzzle file. func.load_puzzle()")
        else:
            self.puzzle.clear()
            self.puzzle = puzzle2
            self.puzzle.create_puzzle_pieces()
            self.update_moves(reset=True)
            self.display_round(True)
            self.begin_round()
              
    def reset_game(self, x, y):
        """Resets a puzzle

        Args:
            x (int): Passed not used
            y (int): Passed not used
        """
        self.puzzle.clear()
        self.puzzle = Puzzle(self.puzzle.get_name()) 
        self.puzzle.create_puzzle_pieces()
        self.display_round(False) 
        self.begin_round()
              
    def quit_game(self, x, y):
        """Quits the gamre

        Args:
            x (int): Passed not used
            y (int): Passed not used
        """
        self.window.clear()
        self.create_turtle().place_image(QUIT_MESSAGE_PATH, LOCATION_QUITMESSAGE)
        time.sleep(2)
        self.window.bye()
                   
    def display_round(self, shuffled=True):
        """Displays a new puzzle

        Args:
            shuffled (bool, optional): If shuffling is required or not. Defaults to True.
        """
        
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
        """Begins a new round
        """
        data = self.puzzle.data       
        for row in data:
            for piece in row:
                piece.turtle.turtle.onclick(partial(self.check_swap, piece))
    
    def check_swap(self, piece, x, y):
        """Checks if 2 tiles can be swapped

        Args:
            piece (Piece): Piece object
            x (int): Passed not used
            y (int): Passed not used
        """
        
        neighbours = self.puzzle.get_neighbours(piece)
        blank = self.puzzle.check_swap(neighbours)
        
        if not blank: return
            
        self.update_moves()
        
        won = self.puzzle.swap_pieces(piece, blank)
        
        if won:
            self.win()
            
    def update_moves(self, reset=False):
        """Updates the moves counter

        Args:
            reset (bool, optional): If new game or not. Defaults to False.
        """
        if reset:
            self.moves = self.initialmoves
        
        else:
            self.moves -= 1
            
        self.moves_counter.turtle.clear()
        self.place_text(f"{self.moves}", MOVES_FONT, LOCATION_MOVESCOUNTER_TEXT, turt=self.moves_counter, color="black")
        if self.moves == 0: 
            self.lost()
            
    def lost(self):
        """Lost game and quit
        """
        self.window.clear()
        self.set_bg_image("assets/resources/Lose.gif")
        time.sleep(3)
        self.window.bye()
        
    def win(self):
        """Winner, update leaderboard and quit
        """
        moves_used = self.initialmoves - self.moves
        
        self.update_leaders(moves_used)
        self.window.clear()
        self.set_bg_image("assets/resources/winner.gif")
        time.sleep(4)
        self.create_turtle().place_image("assets/resources/credits.gif", LOCATION_QUITMESSAGE)
        time.sleep(2)
        self.window.bye()
    
    def file_error(self):
        """File not found error handling
        """
        file_error = self.create_turtle()
        file_error.place_image(FILEERROR_MESSAGE_PATH, LOCATION_QUITMESSAGE)
        time.sleep(2)
        file_error.turtle.hideturtle()
        self.load_puzzle(0, 0)
    
    def update_leaders(self, moves):
        """Updates leaderboard when someone wins

        Args:
            moves (int): Moves used
        """
        self.leaders[moves] = self.name
        self.save_leaders()
     
    def save_leaders(self):
        """Saves leaders to data file
        """
        outputFile = 'leaders.data'
        with open(outputFile, 'wb') as fw:
            pickle.dump(self.leaders, fw)
  
    def restore_leaders(self):
        """Restores leaderboard from data file
        """
        inputFile = 'leaders.data'
        with open(inputFile, 'rb') as fd:
            self.leaders = pickle.load(fd)
                                
    def start_game(self, x=0, y=0):
        """Starts the main game

        Args:
            x (int, optional): Passed not used. Defaults to 0.
            y (int, optional): Passed not used. Defaults to 0.
        """
        # ------- Display Splash -------
        self.display_splash("assets/resources/splash_screen.gif")

        # # ------- Get Inputs -------
        self.name = self.get_input("Welcome", "Enter your name: ")
        self.moves = self.get_num_input("Moves", "Enter the number of moves you want (5 - 200): ")
        
        # ---- Create Board -----
        self.restore_leaders()
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
