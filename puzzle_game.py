from GameWindow import GameWindow
from helper import *
from pprint import pprint

LEADERS = {
    3: "Neel",
    5: "Mikhael",
    10: "John",
    1: "Andrew",
}
window = GameWindow(title="Puzzle Game by Neel")

window.display_splash("assets/resources/splash_screen.gif")

name = window.get_input("Welcome", "Enter your name: ")
moves = window.get_input("Moves", "Enter the number of moves you want (5 - 200): ")

window.draw_board(name, moves, LEADERS)

puzzles = generate_puzzle_data()
pprint(puzzles)
# window.start_game(name, moves, puzzles)

window.window.exitonclick()