from CustomTurtle import CustomTurtle

class Piece:
    def __init__(self, location=(1,1), img="", isblank=False, tile_num=-1):
        self.turtle = CustomTurtle()
        self.location = location
        self.img = img
        self.isblank = isblank
        self.tile_num = tile_num