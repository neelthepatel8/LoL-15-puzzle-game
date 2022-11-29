
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
BUTTON_START = 505, 631
LOCATION_RESET_BTN = BUTTON_START[0], BUTTON_START[1]
LOCATION_LOAD_BTN = BUTTON_START[0] + 100, BUTTON_START[1]
LOCATION_QUIT_BTN = BUTTON_START[0] + 200, BUTTON_START[1]

# ------ Text Locations -------
LOCATION_MOVES_TEXT = 63, 650
LOCATION_LEADERBOARD_TITLE_TEXT = 601, 179
LOCATION_NAMES_START_TEXT = 601, 217
NAMES_TEXT_DISTANCE = 30

# ------- Text Attributes --------
DEFAULT_FONT = "Arial"
MOVES_FONT = DEFAULT_FONT, 32, "bold"
LEADERBOARD_TITLE_FONT = DEFAULT_FONT, 32, "bold"
LEADERBOARD_NAMES_FONT = DEFAULT_FONT, 20, "normal"

# --------- Even Distance between objects -------
DISTANCE_BETWEEN_OBJECTS = 45

# ----- Splash Screen Settings -----
SPLASH_LINGER_TIME = 3

# ----- Banner ------
LOCATION_COMPLETED_BANNER_IMG = 664, 70

# ------ Puzzle Images --------
DISTANCE_BETWEEN_PIECES = 16
LOCATION_FIRST_PIECE = 20 + LOCATION_PUZZLEBOARD[0]\
                     , 20 + LOCATION_PUZZLEBOARD[1]
                     
# ------- All Puzzles -------
PUZZLES = ["fifteen", "luigi", "mario", "smiley", "yoshi"]

# --------- Splashes ----------
QUIT_MESSAGE_PATH = "assets/resources/quitmsg.gif"
LOCATION_QUITMESSAGE =  400, 342

