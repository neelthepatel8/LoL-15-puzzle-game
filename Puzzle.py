from helper import *
from random import shuffle
import math
from CustomTurtle import CustomTurtle
from pprint import pprint
from Piece import Piece
from copy import deepcopy

class Puzzle:
    def __init__(self, path):
        self.path = "assets/" + path
        self.dict = generate_puzzle_data(self.path)
        self.images = self.dict["images"]
        self.name = self.path[len("assets/"):]        
        self.thumbnail_turtle = []
        self.length = int(math.sqrt(self.get_num_pieces()))
        self.data = []
        
        
        
    # ----- GETTERS -----
    def get_num_pieces(self):
        return int(self.dict["number"])
    
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
        
        # Reset puzzle pieces
        for row in self.data:
            for piece in row:
                piece.turtle.turtle.hideturtle()
                # piece.turtle.turtle.reset()
            
        # Reset thumbnail
        for t in self.thumbnail_turtle:
            t.turtle.hideturtle()
            
    def create_puzzle_pieces(self):
        images = self.images
        count = 1
        
        for i in range(self.length):
            self.data.append([])
            for j in range(self.length):
                image = images[f"{count}"]
                
                blank = False
                if image[-9:-4] == "blank":
                    blank = True
                
                piece = Piece((i, j), image, blank)
                
                self.data[i].append(piece)
                count += 1
        
              
    def create_order_list(self):
        lst = []
        for row in self.data:
            for piece in row:
                if not piece.isblank: 
                    img = piece.img[-6:].strip("/")[:-4]
                    lst.append(int(img))
                else:
                    lst.append(0)
        
        return lst   

    def get_neighbours(self, piece):
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
        for neighbour in neighbours:
            if neighbour.isblank:
                return neighbour
    
    def swap_pieces(self, piece, blank):
        
        x, y = blank.location
        a, b = piece.location

        piece.location = x, y
        blank.location = a, b
        
        piece_data = self.data[a][b] 
        blank_data = self.data[x][y] 
        
        p_x, p_y = piece.turtle.turtle.pos()
        b_x, b_y = blank.turtle.turtle.pos()
        
        piece.turtle.goto(b_x, b_y)
        blank.turtle.goto(p_x, p_y)
        
        piece_data, blank_data = blank_data, piece_data 
        
        return self.check_win()
    
    def check_win(self):
        print(self.create_order_list())
        print(sorted(self.create_order_list(), reverse=True))
        if self.create_order_list() == sorted(self.create_order_list(), reverse=True):
            return True
                      
    def shuffle(self):
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
        
    
    # def make_adjacency_matrix(self):
    #     matrix = {}
    #     for row_index, row in enumerate(self.puzzle_data):
    #         for index, each in enumerate(row):
    #             pass
            
    #     print(matrix)
        
    # def find_blank_tile(self):
    #     self.blank_tile_data = "", 1, (1, 2)
    #     for row in self.puzzle_data:
    #         for img, turt in row:
    #             if img[-9:-1] == "blank.gif":
    #                 index = self.puzzle_data.index(row), row.index((img, turt))
    #                 self.blank_tile_data = img, turt, index
    #     self.blank_tile_data