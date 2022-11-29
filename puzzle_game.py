from GameWindow import GameWindow
from helper import *

LEADERS = {
    3: "Neel",
    5: "Mikhael",
    10: "John",
    1: "Andrew",
    12: "Neeeeeele"
}
window = GameWindow(title="Puzzle Game by Neel")

window.display_splash("assets/resources/splash_screen.gif")

name = window.get_input("Welcome", "Enter your name: ")
moves = window.get_input("Moves", "Enter the number of moves you want (5 - 200): ")

window.draw_board(moves, LEADERS)

CURRENT_PUZZLE = "mario.puz"
window.start_game(CURRENT_PUZZLE)

window.window.mainloop()