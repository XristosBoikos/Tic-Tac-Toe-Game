import random


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+---------------+---------------+---------------+")
    print("|               |               |               |")
    print("|      ", board[0], "      |      ", board[1], "      |      ", board[2], "      |")
    print("|               |               |               |")
    print("+---------------+---------------+---------------+")
    print("|               |               |               |")
    print("|      ", board[3], "      |      ", board[4], "      |      ", board[5], "      |")
    print("|               |               |               |")
    print("+---------------+---------------+---------------+")
    print("|               |               |               |")
    print("|      ", board[6], "      |      ", board[7], "      |      ", board[8], "      |")
    print("|               |               |               |")
    print("+---------------+---------------+---------------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    available = make_list_of_free_fields(board)
    user_move = input("Make your move: ")
    choice = user_move.isdigit()
    while choice is False or int(user_move) not in available:
        print(available)
        user_move = input("Wrong! Make your move again: ")
        choice = user_move.isdigit()
    board[int(user_move) - 1] = "O"
    return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    available_spaces = []
    for i in board:
        if i != "X" and i != "O":
            available_spaces.append(i)
        else:
            continue
    if available_spaces:
        return available_spaces
    else:
        return False


def victory_for(board, sign):
    # Checks if there is a winning condition (3 in a row)
    winner_combinations = ((1, 2, 3), (1, 5, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (3, 5, 7), (4, 5, 6), (7, 8, 9))
    for i in range(len(winner_combinations)):
        if (board[(winner_combinations[i][0]) - 1] == sign and board[(winner_combinations[i][1]) - 1] == sign and
                board[(winner_combinations[i][2]) - 1] == sign):
            return True
        else:
            continue
    return False


def victory(board, sign):
    # If there is a winning condition checks who won and returns the winner
    if victory_for(board, sign):
        global result
        global winner
        result = True
        if sign == "X":
            winner = "Computer Wins"
        elif sign == "O":
            winner = "You Won!"
        else:
            print("Something went wrong")


def draw_move_auto(board, sign):
    com_move = ""
    winner_combinations = ([1, 2, 3], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9])
    available = make_list_of_free_fields(board)

    # change not available to "O" or "X"
    for i in range(len(winner_combinations)):
        for j in range(len(winner_combinations[i])):
            if board[(winner_combinations[i][j]) - 1] == sign:
                winner_combinations[i][j] = sign

    # remove all "0" or "X" from every winner combination
    # if only one remains then we must block to prevent player from winning
    for i in range(len(winner_combinations)):
        times = winner_combinations[i].count(sign)
        for j in range(times):
            winner_combinations[i].remove(sign)
        if len(winner_combinations[i]) == 1 and winner_combinations[i][0] in available:
            com_move = winner_combinations[i].pop(0)
            print(f"Computer played at {com_move}")
            board[com_move - 1] = "X"
            return board

    if com_move == "" and sign == "X":
        global current_board
        draw_move_auto(current_board, "O")

    # if no chance of win or chance of losing play random
    if com_move == "" and sign == "O":
        com_move = random.choice(available)
        print(f"Computer played at {com_move}")
        board[com_move - 1] = "X"
        return board


def check_for_moves(board):
    # if there are no other possible moves and no winner, the game is a draw
    if make_list_of_free_fields(board) is False:
        global draw
        draw = True
        display_board(current_board)
        print("Draw")


current_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = False
winner = ""
draw = False

# asks user who plays first until proper answer
while True:
    choice = input("You want to start first? Y or N: ")
    if choice.upper() == "Y":
        player_first = True
        break
    elif choice.upper() == "N":
        player_first = False
        break
    else:
        print("Wrong input try again")

# user starts first
if player_first:
    while not result and not draw:
        # Player Move
        display_board(current_board)
        current_board = enter_move(current_board)
        victory(current_board, "O")
        check_for_moves(current_board)
        if not result and not draw:
            # Computer Move:
            draw_move_auto(current_board, "X")
            victory(current_board, "X")
            check_for_moves(current_board)
# computer starts first
else:
    while not result and not draw:
        # Computer Move:
        check_for_moves(current_board)
        draw_move_auto(current_board, "X")
        victory(current_board, "X")
        check_for_moves(current_board)
        if not result and not draw:
            # Player Move
            display_board(current_board)
            current_board = enter_move(current_board)
            victory(current_board, "O")
# after game ends (via winner or draw) prints the last "stage" of the board and the winner
if result:
    display_board(current_board)
    print(winner)
