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
LOCATION_COLOR_RECT = 405, 631
LOCATION_MODE_BTN = 385, 631
LOCATION_MODE_BTN_MOVED = 430, 631

# ------ Text Locations -------
LOCATION_MOVES_TEXT = 63, 650
LOCATION_MOVESCOUNTER_TEXT = 370, 650
LOCATION_LEADERBOARD_TITLE_TEXT = 601, 179
LOCATION_NAMES_START_TEXT = 601, 217
NAMES_TEXT_DISTANCE = 30

# ------- Text Attributes --------
DEFAULT_FONT = "Courier"
MOVES_FONT = DEFAULT_FONT, 32, "bold"
LEADERBOARD_TITLE_FONT = DEFAULT_FONT, 32, "bold"
LEADERBOARD_NAMES_FONT = DEFAULT_FONT, 24, "bold"

# --------- Even Distance between objects -------
DISTANCE_BETWEEN_OBJECTS = 45
IMAGE_MOVE = 98 + 16

# ----- Images -----
IMAGE_START_CORNER = 65, 65
BG_IMG = "assets/resources/bg_img.gif"

# ----- Splash Screen Settings -----
SPLASH_LINGER_TIME = 3

# ----- Banner ------
LOCATION_THUMBNAIL = 664, 70

# ------ Puzzle Images --------
DISTANCE_BETWEEN_PIECES = 16 + 98
LOCATION_FIRST_PIECE = 20 + 49 + LOCATION_PUZZLEBOARD[0]\
                     , 20 + 49 + LOCATION_PUZZLEBOARD[1]
                     
# ------- All Puzzles -------
PUZZLES = ["fifteen", "luigi", "mario", "smiley", "yoshi"]

# --------- Splashes ----------
QUIT_MESSAGE_PATH = "assets/resources/quitmsg.gif"
LOCATION_QUITMESSAGE =  400, 342
FILEERROR_MESSAGE_PATH = "assets/resources/file_error.gif"

# ----- Colors -----


