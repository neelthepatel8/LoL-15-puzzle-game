from Window import GameWindow

window = GameWindow(title="Puzzle Game by Neel", width=950, height=650)

window.display_splash("assets/resources/splash_screen.gif")

name = window.get_input("Welcome", "Enter your name: ")
moves = window.get_input("Moves", "Enter the number of moves you want (5 - 200): ")

window.window.exitonclick()