import os   # for clearing the terminal to give a better experience to players
import time  # for pausing the script to show to user what errors occurred

# if you like to, you can change the markers of the players
PLAYER1_MARKER = "X"
PLAYER2_MARKER = "O"

####################
# USEFUL FUNCTIONS #
####################

def create_board():
    """
    This Function creates the board and returns a dictionary.
    Return format can be done in different ways, but this come to my mind in the first place.

    Separating the lines that markers will be placed will be useful when updating the board

    :return: returns a dictionary that stores the skeleton and the marker rows
    """

    board_lines = ["┏━━━━━┳━━━━━┳━━━━━┓", "┣━━━━━╋━━━━━╋━━━━━┫",
                   "┣━━━━━╋━━━━━╋━━━━━┫", "┗━━━━━┻━━━━━┻━━━━━┛"]
    piece_lines = ["┃  _  ┃  _  ┃  _  ┃", "┃  _  ┃  _  ┃  _  ┃", "┃  _  ┃  _  ┃  _  ┃"]

    board = {"edges": board_lines, "pieces": piece_lines}
    return board


def print_board(board):
    """
    Prints the board

    :param board: dictionary storing the skeleton and marker rows
    """

    # while printing, you might think using a dictionary is not sensible,
    # but it will provide ease in the other functions
    for i, j, row in zip(board["edges"], board["pieces"], "321"):
        print(" ", i)
        # printing the row number also
        print(row, j)

    # need to print the bottom of the board because edges have 4 element while marker rows have 3
    print(" ", board["edges"][-1])
    # printing the fyle character
    print("     a     b     c")


def greet_users(board):
    """
    Prints the introduction message to the terminal
    :param board: it is just used for calling the print_board() function
    """

    print("┏━━━━━━━━━━━━━━━━━━━━━━━━┓"
          "\n┃ WELCOME to TIC-TAC-TOE ┃"
          "\n┗━━━━━━━━━━━━━━━━━━━━━━━━┛")

    print_board(board)

    print("Player-1 is X")
    print("Player-2 is O")

    print("Press any button when you are ready!")
    input()

    os.system("cls")


def check_endgame(marker):
    """
    Checks if the given marker wins the game.

    Looks for:
        - east
        - south-east
        - south
        - south-west

    Directions and checks if there are 3 adjacent markers. If there is any return True.

    :param marker: X or O according to the player
    :return: boolean value
    """

    # east, south-east, south, south-west
    # other directions are not important because with for loop we start from top-left to bottom-right
    directions = [[0, 1], [1, 1], [1, 0], [1, -1]]

    # board row
    for i in range(3):
        # board col
        for j in range(3):
            # if a cell is occupied with the given marker
            if board_log[i][j] == marker:
                # check for all directions
                for direction in directions:
                    # x and y values of the direction increase or decrease
                    dx = direction[0]
                    dy = direction[1]

                    # will be used to check to neighbour cells
                    temp_x = i
                    temp_y = j

                    # check for win - if there are 2 more adjacent markers in the given direction, win occurs
                    adjacent = 1
                    for _ in range(2):
                        # increase or decrease the indexes for going to the neighbour
                        temp_x += dx
                        temp_y += dy

                        # boundary check
                        if 0 <= temp_x <= 2 and 0 <= temp_y <= 2:
                            # take the neighbour cell
                            temp = board_log[temp_x][temp_y]

                            # if neighbour cell is occupied with the given marker
                            if temp == marker:
                                # increase the adjacent variable
                                adjacent += 1

                            # break if the cell is not the marker we are looking for
                            else:
                                break

                        # break if the indexes go out of bounds
                        else:
                            break

                    # if 2 more adjacent markers found in a direction so far return True
                    if adjacent == 3:
                        return True

    # if there isn't any 3 adjacent markers in any cell return False
    return False


def is_stalemate():
    """
    If the board log is completely filled en yet no player wins, it is a stalemate.
    That is the intuition behind this function

    :return: boolean value
    """

    # check all cells in the board log
    for row in board_log:
        for cell in row:
            # if any blank cell is found return False, because a player still can place a marker
            if cell == "_":
                return False

    # return True, because no more markers can be placed on the board
    return True


def check_row_available(row):
    """
    This function is used for checking the row of the board.

    - If the row is completely occupied, returns False.
    - If there is any blank cells in the row, return True

    :param row: index storing the row number the player entered
    :return: boolean value
    """

    # check all cells in the given row of the board log
    for cell in board_log[3-int(row)]:
        # if any blank cell is found return True, because the row is still available for a placement
        if cell == "_":
            return True

    # return False, because the row is fully occupied
    return False


def check_cell_available(row, col):
    """
    This function is used for checking the cell of the board.

    - If the cell is blank, returns True.
    - If there are any marker in the cell, returns False

    :param row: index storing the row number the player entered
    :param col: index storing the column number the player entered
    :return: boolean value
    """

    # used for changing fyle characters into integers
    fyle_to_num = {"a": 0, "b": 1, "c": 2}

    # changing row to integer
    row = int(row)
    # getting the column value via the dictionary
    col = fyle_to_num[col]

    # if the cell is blank, return True
    if board_log[3-row][col] == "_":
        return True

    # else return False
    return False


def apply_move(board, move, marker):
    """
    This function takes the move that the player entered and updates the board and board_log

    :param board: dictionary storing the skeleton and marker rows
    :param move: row and column values the player entered
    :param marker: X or O according to the player
    :return: updated board dictionary
    """

    # used for changing fyle characters into integers
    fyle_to_num = {"a": 0, "b": 1, "c": 2}

    # changing row to integer
    row = int(move[0])
    # getting the column value via the dictionary
    col = fyle_to_num[move[1]]

    # user enters the row number according to the terminal output of the board
    # terminal output's row values are upside down, so we apply 3-row
    # temp stores the marker row that we will be updating
    temp = board["pieces"][3-row]

    # slicing the string and putting the marker in the correct position
    temp = temp[:6*col+3] + marker + temp[6*col+4:]

    # finally, updating the board dictionary and board log
    board["pieces"][3-row] = temp
    board_log[3-row][col] = marker

    return board


def get_move(player, marker):
    """
    This function carefully applies error handling while taking the row and column values from the player.

    :param player: 1 or 2 referring to the player-1 and player-2 respectively
    :param marker: X or O according to the player
    :return: list consisting of the row and column value the player entered
    """

    while True:
        # used for clearing the terminal. helps to give the players a much pleasant experience
        os.system("cls")
        # printing the board
        print_board(my_board)

        try:
            # printing the correct player name and its marker
            print(f"\nPlayer-{player} plays -> {marker}\n")
            print("Enter your move:")

            # getting the row input
            user_move_row = input("row (1,2 or 3): ")

            # applying error handling
            assert 0 < len(user_move_row), "Please enter a input"
            assert len(user_move_row) < 2, "Please enter only one character"
            assert user_move_row in "123", "Please enter a relevant input."
            assert check_row_available(user_move_row), "Row is fully occupied"

            # getting the column input
            user_move_col = input("fyle (a,b or c): ")

            # applying error handling
            assert 0 < len(user_move_col), "Please enter a input"
            assert len(user_move_col) < 2, "Please enter only one character"
            assert user_move_col.lower() in "abc", "Please enter a relevant input."
            assert check_cell_available(user_move_row, user_move_col.lower()), "Cell is already occupied"

            break

        # printing the error messages if occurs
        except AssertionError as err:
            print(err)
            # used for showing the error message before clearing the terminal
            time.sleep(1.5)

    # return the row and column values the user entered
    return [user_move_row, user_move_col]


#############
# MAIN GAME #
#############

# CREATING THE NECESSARY BACKGROUND VARIABLES
# the main board
my_board = create_board()
# board log for storing the user entries in the board. helps to check wins or stalemates
board_log = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

# printing the introduction message in the terminal
greet_users(my_board)

# used for calling the functions for player-1 or player-2. if the move count is odd call for player-2 etc.
move_count = 0

# the main while loop for the game
while True:
    # used for clearing the terminal. helps to give the players a much pleasant experience
    os.system("cls")
    # printing the board in each iteration
    print_board(my_board)

    # check if player-1 wins
    if check_endgame(PLAYER1_MARKER):
        print("Player-1 Wins!\n")
        break

    # check if player-2 wins
    elif check_endgame(PLAYER2_MARKER):
        print("Player-2 Wins!\n")
        break

    # check stalemate
    elif is_stalemate():
        print("Stalemate! - No winner.\n")
        break

    # player-1 moves
    if move_count % 2 == 0:
        user_move = get_move(1, PLAYER1_MARKER)
        my_board = apply_move(my_board, user_move, PLAYER1_MARKER)

    # player-2 moves
    else:
        user_move = get_move(2, PLAYER2_MARKER)
        my_board = apply_move(my_board, user_move, PLAYER2_MARKER)

    # increase the move count to change the turn to the other player
    move_count += 1
