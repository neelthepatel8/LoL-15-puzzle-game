from helper import *
from random import shuffle
import math
import time
from Piece import Piece
        
class Puzzle:
    def __init__(self, path):
        
        self.path = "assets/" + path
        
        try:
            self.dict = generate_puzzle_data(self.path)
        
        except FileNotFoundError as er:
            self.error = True
            return
        
        self.error = False
        self.images = self.dict["images"]
        self.name = self.path[len("assets/"):]        
        self.thumbnail_turtle = []
        
        if not self.get_num_pieces():
            self.error = True
            with open("5001_puzzle.err", 'w') as file:
                file.write(f"{time.localtime()} ERROR Puzzle size doesnt work with my grid!. func.Puzzle.__init__()")
            return
            
        self.length = int(math.sqrt(self.get_num_pieces()))
        self.data = []
           
    # ----- GETTERS -----
    def get_num_pieces(self):
        n = int(self.dict["number"])
        sqrt = math.sqrt(n)
        
        if int(sqrt + 0.5) ** 2 == n:
            return n
        return None
    
    def get_name(self):
        return self.name
    
    def get_path(self):
        return self.path 
    
    def get_dict(self):
        return self.dict
    
    def get_thumbnail(self):
        return self.dict["thumbnail"]
    
    def get_turtles(self):
        return self.turtles
               
    # ----- SETTERS -----
    def set_turtles(self, t):
        self.turtles = t
  
    # ----- METHODS -----
    def clear(self):
        """Clears puzzle off the screen
        """
        
        # Reset puzzle pieces
        for row in self.data:
            for piece in row:
                piece.turtle.turtle.hideturtle()
                # piece.turtle.turtle.reset()
            
        # Reset thumbnail
        for t in self.thumbnail_turtle:
            t.turtle.hideturtle()
            
    def create_puzzle_pieces(self):
        """Creates turtles for pieces and stores in nested list
        """
        images = self.images
        count = 1
        
        for i in range(self.length):
            self.data.append([])
            for j in range(self.length):
                image = images[f"{count}"]
                
                blank = False
                if image[-9:-4] == "blank":
                    blank = True
                
                piece = Piece((i, j), image, blank, tile_num=count)
                
                self.data[i].append(piece)
                count += 1
                   
    def get_neighbours(self, piece):
        """Gets neighbours of a particular tile

        Args:
            piece (Piece): tile clicked

        Returns:
            list: list of neighbours
        """
        x, y = piece.location
        neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for row in self.data:
            for p in row:
                if p.location in neighbours:
                    neighbours.remove(p.location)
                    neighbours.append(p)
        
        res = []
        for each in neighbours:
            if isinstance(each, tuple): continue
            res.append(each)
        
        return res
    
    def check_swap(self, neighbours):
        """Checks if can be swapped

        Args:
            neighbours (list): List of neighbours of clicked tile

        Returns:
            Piece : neighbour that can be swapped
        """
        for neighbour in neighbours:
            if neighbour.isblank:
                return neighbour
    
    def swap_pieces(self, piece, blank):
        """Swaps 2 pieces

        Args:
            piece (Piece): clicked piece
            blank (Piece): blank piece

        Returns:
            bool: If win or no
        """
        
        x, y = blank.location
        a, b = piece.location

        piece.location = x, y
        blank.location = a, b
        
        self.data[a][b], self.data[x][y] = self.data[x][y], self.data[a][b]
          
        
        p_x, p_y = piece.turtle.turtle.pos()
        b_x, b_y = blank.turtle.turtle.pos()
        
        piece.turtle.goto(b_x, b_y)
        blank.turtle.goto(p_x, p_y)
                
        
        return self.check_win()
    
    def check_win(self):
        """Checks if there is a win condition
        """ 
        lst = []
        for row in self.data:
            for piece in row:
                lst.append(piece.tile_num)
                
        if lst == sorted(lst, reverse=False):
            return True
                
    def is_impossible_to_solve(self):
        """Tried to implement the bonus but this doesnt work 

        Returns:
            bool: If impossible to solve or not
        """
        puzzle = self.data
        
        # check if the puzzle is a 3x3 grid
        if len(puzzle) != 3 or len(puzzle[0]) != 3:
            return True
        
        # check if the puzzle contains 8 numbers and one empty space
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        for row in puzzle:
            for num in row:
                if num not in nums and num != 0:
                    return True
                elif num in nums:
                    nums.remove(num)
        if len(nums) != 0:
            return True
        
        # count the number of inversions
        inversions = 0
        flat_puzzle = [num for row in puzzle for num in row]
        for i in range(len(flat_puzzle) - 1):
            for j in range(i + 1, len(flat_puzzle)):
                if flat_puzzle[i] and flat_puzzle[j] and flat_puzzle[i] > flat_puzzle[j]:
                    inversions += 1
                    
        # check if the puzzle is solvable
        if inversions % 2 == 0:
            return False
        else:
            return True 
                      
    def shuffle(self):
        """Shuffles a puzzle
        """
        new_data = []
        for row in self.data:
            for piece in row:
                new_data.append(piece)

        shuffle(new_data)
        
        self.data = []
        for i in range(self.length):
            self.data.append([])
            for j in range(self.length):
                piece = new_data.pop()
                self.data[i].append(piece)
                piece.location = i, j