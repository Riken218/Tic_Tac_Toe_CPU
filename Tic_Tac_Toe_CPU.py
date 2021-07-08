import random

# Makes tic-tac-toe board of rows x columns size.
def make_board(rows=3, columns=3):
    new_board = []
    for i in range(rows):
        new_row = []
        for j in range(columns):
            new_row.append(" ")
        new_board.append(new_row)
    return new_board

# Prints the board to the terminal (working on GUI version).
def print_board(board, separator = "|"):
    row = ""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j < len(board[0])-1:
                row = row + str(board[i][j]) + separator
            else:
                row = row + str(board[i][j])
        print("\t\t{}".format(row))
        if i < len(board)-1:
            row_sep = "-"
            for k in range(len(board[0])-1):
                row_sep = row_sep + "+-"
            print("\t\t{}".format(row_sep))
        row = ""

# Marks the board based on the current state of the board,
# the position to mark the board, and the player's mark.
# Returns "True" if the board has been marked.
def mark_board(board, r, c, mark):
    if board[r][c] == " ":
        board[r][c] = mark
        return True
    else:
        return False

# Checks each row for it to be full of either player's marker.
def check_rows(board, players):
    for i in range(len(board)):
        xes = []
        oes = []
        for j in range(len(board[0])):
            if board[i][j] == players[0]:
                xes.append(board[i][j])
            elif board[i][j] == players[1]:
                oes.append(board[i][j])
        if (len(xes) == len(board[0])) or (len(oes) == len(board[0])):
            return True
    if (len(xes) == len(board[0])) or (len(oes) == len(board[0])):
        return True
    else:
        return False

# Checks each row separately for 1 less than length of row 
# to check if it needs to / can block player.
def check_1_row(board, players, row):
    xes = []
    oes = []
    for j in range(len(board)):
        if board[row][j] == players[0]:
            xes.append(board[row][j])
        elif board[row][j] == players[1]:
            oes.append(board[row][j])
    if ((len(xes) == len(board[0])-1) and (len(oes) == 0)) or ((len(oes) == len(board[0])-1) and (len(xes) == 0)):
        return True
    else:
        return False

# Checks all rows to see if player needs to be / can be blocked.
def check_rows_CPU(board, players):
    for i in range(len(board)):
        if check_1_row(board, players, i):
            return True
    return False

# Checks if the CPU has a winning move in a row
def CPU_win_move_row(board, players, row, CP, Player):
    P_list = []
    CP_list = []
    for i in range(len(board)):
        if board[row][i] == players[CP]:
            CP_list.append(board[row][i])
        elif board[row][i] == players[Player]:
            P_list.append(board[row][i])
    if ((len(CP_list) == len(board[0])-1) and len(P_list) == 0):
        return True
    else:
        return False

# Checks each column for it to be full of either player's marker.
def check_columns(board, players):
    for j in range(len(board[0])):
        xes = []
        oes = []
        for i in range(len(board)):
            if board[i][j] == players[0]:
                xes.append(board[i][j])
            elif board[i][j] == players[1]:
                oes.append(board[i][j])
        if (len(xes) == len(board[0])) or (len(oes) == len(board[0])):
            return True
    if (len(xes) == len(board[0])) or (len(oes) == len(board[0])):
        return True
    else:
        return False

# Checks each row separately for 1 less than length of column 
# to check if it needs to / can block player.
def check_1_column(board, players, col):
    xes = []
    oes = []
    for i in range(len(board)):
        if board[i][col] == players[0]:
            xes.append(board[i][col])
        elif board[i][col] == players[1]:
            oes.append(board[i][col])
    if ((len(xes) == len(board[0])-1) and (len(oes) == 0)) or ((len(oes) == len(board[0])-1) and (len(xes) == 0)):
        return True
    else:
        return False

# Checks all columns to see if player needs to be / can be blocked.
def check_columns_CPU(board, players):
    for j in range(len(board)):
        if check_1_column(board, players, j):
            return True
    return False

# Checks if the CPU has a winning move in a column
def CPU_win_move_column(board, players, col, CP, Player):
    P_list = []
    CP_list = []
    for i in range(len(board)):
        if board[i][col] == players[CP]:
            CP_list.append(board[i][col])
        elif board[i][col] == players[Player]:
            P_list.append(board[i][col])
    if ((len(CP_list) == len(board[0])-1) and len(P_list) == 0):
        return True
    else:
        return False

# # Checks each diagonal for it to be full of either player's marker.
def check_diagonals(board, players):
    x = len(board)-1
    for i in range(len(board)):
        # Top-left to bottom-right diagonal check.
        # (Also checks smaller diagonals but doesn't slow down program overall.)
        xes = []
        oes = []
        for j in range(len(board)):
            if board[j][j] == players[0]:
                xes.append(board[j][j])
            elif board[j][j] == players[1]:
                oes.append(board[j][j])
            if (len(xes) == len(board[0])) or (len(oes) == len(board[0])):
                return True
        # Top-right to bottom-left diagonal check.
        # (Also checks smaller diagonals but doesn't slow down program overall.)
        xes = []
        oes = []
        for k in range(len(board)):
            if board[k][x-k] == players[0]:
                xes.append(board[k][x-k])
            elif board[k][x-k] == players[1]:
                oes.append(board[k][x-k])
            if (len(xes) == len(board[0])) or (len(oes) == len(board[0])):
                return True
        if (len(xes) == len(board[0])) or (len(oes) == len(board[0])):
            return True
    if (len(xes) == len(board[0])) or (len(oes) == len(board[0])):
        return True
    else:
        return False

# Checks top-left to bottom-right diagonal for CPU to block player.
# Left over from 2-Player program
def check_1st_diag(board, players):
    xes = []
    oes = []
    for j in range(len(board)):
        if board[j][j] == players[0]:
            xes.append(board[j][j])
        elif board[j][j] == players[1]:
            oes.append(board[j][j])
    if ((len(xes) == len(board[0])-1) and (len(oes) == 0)) or ((len(oes) == len(board[0])-1) and (len(xes) == 0)):
        return True
    else:
        return False

# Same as "check_1st_diag" function, but specifies CPU and Player.
# Replace "check_1st_diag" function with this in future version.
def CPU_win_move_1_diag(board, players, CP, Player):
    P_list = []
    CP_list = []
    for i in range(len(board)):
        if board[i][i] == players[CP]:
            CP_list.append(board[i][i])
        elif board[i][i] == players[Player]:
            P_list.append(board[i][i])
    if ((len(CP_list) == len(board[0])-1) and len(P_list) == 0):
        return True
    else:
        return False

# Checks top-right to bottom-left diagonal for CPU to block player.
# Left over from 2-Player program
def check_2nd_diag(board, players):
    x = len(board)-1
    xes = []
    oes = []
    for k in range(len(board)):
        if board[k][x-k] == players[0]:
            xes.append(board[k][x-k])
        elif board[k][x-k] == players[1]:
            oes.append(board[k][x-k])
    if ((len(xes) == len(board[0])-1) and (len(oes) == 0)) or ((len(oes) == len(board[0])-1) and (len(xes) == 0)):
        return True
    else:
        return False

# Same as "check_2nd_diag" function, but specifies CPU and Player.
# Replace "check_2nd_diag" function with this in future version.
def CPU_win_move_2_diag(board, players, CP, Player):
    x = len(board)-1
    P_list = []
    CP_list = []
    for i in range(len(board)):
        if board[i][x-i] == players[CP]:
            CP_list.append(board[i][x-i])
        elif board[i][x-i] == players[Player]:
            P_list.append(board[i][x-i])
    if ((len(CP_list) == len(board[0])-1) and len(P_list) == 0):
        return True
    else:
        return False

# Full checking for CPU to win in next move.
def CPU_win_move(board, players, CP, Player):
    for i in range(len(board)):
        if CPU_win_move_row(board, players, i, CP, Player) or CPU_win_move_column(board, players, i, CP, Player) or CPU_win_move_1_diag(board, players, CP, Player) or CPU_win_move_2_diag(board, players, CP, Player):
            return True
    else:
        return False

# Checks for if either player has won yet.
# Left over from 2-Player program
def check_board(board, players):
    if check_rows(board, players) or check_columns(board, players) or check_diagonals(board, players):
        return True
    else:
        return False

# Full Single-Player Program
# Make GUI in future version
def Tic_Tac_Toe_CPU(rows='', first='y', marks='', separator=''):
    print("\n\n\n\tWelcome to Tic Tac Toe\n")
    if rows == "":
        rows = 3
    elif (type(rows) == type(3)):
        pass
    else:
        rows = str(input("\tPlease enter the number of rows and columns you'd like to play with (example: 3)\n\t\tDefaults to 3x3 if no input: "))
        if rows == '':
            rows = 3
        rows = int(rows)
        
    while rows >= 8:
        rows = int(input("\tThis board is too large for any reasonable person to want to play.\n\tPlease enter a number less than 8: "))
    
    if first != "y" and first != "n":
        first = "y"
    #first = input("\tEnter \"y\" if you'd like to go first, or \"n\" if you'd like the computer to go first: ")
    
    columns = rows
    board_positions = rows * columns
    
    if marks == "":
        marks = ["x"," ","o"]
    else:
        #marks = str(input("\tNow enter the marks you want to use (example: x o)\n\t\tDefaults to \"x\" and \"o\" if no input: "))
        #if marks == "":
        #    marks = ["x"," ","o"]
        marks = list(marks)
    players = [marks[0],marks[2]]

    if separator == "":
        separator = "|"
    else:
        separator = str(input("\tPlease input desired separator\n\t\tDefaults to \"|\" if no input: "))
        if separator == "":
            separator = "|"
    
    # Start of Game
    turn = 1
    board = make_board(rows, columns)
    # Prints empty board
    print_board(board, separator)
    
    # Player goes first
    if first == "y":
        CP = 1
        Player = 0
        while turn <= board_positions and not check_board(board, players):
            # Player's turn
            if (turn+1)%2 == 0:
                move = list(input("\n\n\tTurn {}, Player {} enter row then column (example: 12 is top center of 3x3 board): ".format(turn,players[(turn+1)%2])))
                move = [int(move[0]),int(move[1])]
                r = move[0]-1
                c = move[1]-1
                while r < 0 or c < 0 or r+1 > rows or c+1 > rows:
                    move = list(input("\n\tThe space you've entered is invalid.\n\tPlease enter a position with values between 1 and {}: ".format(rows)))
                    move = [int(move[0]),int(move[1])]
                    r = move[0]-1
                    c = move[1]-1
                if mark_board(board, r, c, players[(turn+1)%2]):
                    print_board(board,separator)
                    turn = turn + 1
                else:
                    print ("\n\tThe space is already marked, please choose another position\n")
            # CPU's turn
            else:
                x = len(board) - 1
                if CPU_win_move(board, players, CP, Player):
                    for i in range(len(board)):
                        if CPU_win_move_row(board, players, i, CP, Player):
                            r = int(i)
                            for col in board[i]:
                                if col == " ":
                                    c = board[i].index(" ")
                        elif CPU_win_move_column(board, players, i, CP, Player):
                            c = int(i)
                            for row in range(len(board)):
                                if board[row][c] == " ":
                                    r = row
                        elif CPU_win_move_1_diag(board, players, CP, Player):
                            if board[i][i] == " ":
                                r = i
                                c = i
                        elif CPU_win_move_2_diag(board, players, CP, Player):
                            if board[i][x-i] == " ":
                                r = i
                                c = x-i
                elif check_rows_CPU(board, players):
                    for i in range(len(board)):
                        if check_1_row(board, players, i):
                            r = int(i)
                            for col in board[i]:
                                if col == " ":
                                    c = board[i].index(" ")
                elif check_columns_CPU(board, players):
                    for j in range(len(board)):
                        if check_1_column(board, players, j):
                            c = int(j)
                            for i in range(len(board)):
                                if board[i][c] == " ":
                                    r = i     
                elif check_1st_diag(board, players):
                    for i in range(len(board)):
                        if board[i][i] == " ":
                            r = i
                            c = i
                elif check_2nd_diag(board, players):
                    for m in range(len(board)):
                        if board[m][x-m] == " ":
                            r = m
                            c = x-m
                # If CPU can't win or block, play random move.
                else:
                    r = random.randint(0,rows-1)
                    c = random.randint(0,rows-1)
                
                # Check the board to proceed to next turn.
                if mark_board(board, r, c, players[(turn+1)%2]):
                    print("\n\n\tTurn {}".format(turn))
                    print_board(board,separator)
                    turn = turn + 1
        # Checks the board to see if either player has won and how they won.
        if check_rows(board, players):
            print("\tPlayer {} is the winner in a row".format(players[(turn)%2]))
        elif check_columns(board, players):
            print("\tPlayer {} is the winner in a column".format(players[(turn)%2]))
        elif check_diagonals(board, players):
            print("\tPlayer {} is the winner in a diagonal".format(players[(turn)%2]))
        else:
            print("\tThe game was a draw")
    # CPU goes first
    else:
        CP = 0
        Player = 1
        while turn <= board_positions and not check_board(board, players):
            # Player's turn
            if turn%2 == 0:
                move = list(input("\n\n\tTurn {}, Player {} enter row then column (example: 12 is top center of 3x3 board): ".format(turn,players[(turn+1)%2])))
                move = [int(move[0]),int(move[1])]
                r = move[0]-1
                c = move[1]-1
                while r < 0 or c < 0 or r+1 > rows or c+1 > rows:
                    move = list(input("\n\tThe space you've entered is invalid.\n\tPlease enter a position with values between 1 and {}: ".format(rows)))
                    move = [int(move[0]),int(move[1])]
                    r = move[0]-1
                    c = move[1]-1
                if mark_board(board, r, c, players[(turn+1)%2]):
                    print_board(board,separator)
                    turn = turn + 1
                else:
                    print ("\n\tThe space is already marked, please choose another position\n")
            # CPU's turn
            else:
                x = len(board) - 1
                if CPU_win_move(board, players, CP, Player):
                    for i in range(len(board)):
                        if CPU_win_move_row(board, players, i, CP, Player):
                            r = int(i)
                            for col in board[i]:
                                if col == " ":
                                    c = board[i].index(" ")
                        elif CPU_win_move_column(board, players, i, CP, Player):
                            c = int(i)
                            for row in range(len(board)):
                                if board[row][c] == " ":
                                    r = row
                        elif CPU_win_move_1_diag(board, players, CP, Player):
                            if board[i][i] == " ":
                                r = i
                                c = i
                        elif CPU_win_move_2_diag(board, players, CP, Player):
                            if board[i][x-i] == " ":
                                r = i
                                c = x-i
                elif check_rows_CPU(board, players):
                    for i in range(len(board)):
                        if check_1_row(board, players, i):
                            r = int(i)
                            for col in board[i]:
                                if col == " ":
                                    c = board[i].index(" ")
                elif check_columns_CPU(board, players):
                    for j in range(len(board)):
                        if check_1_column(board, players, j):
                            c = int(j)
                            for i in range(len(board)):
                                if board[i][c] == " ":
                                    r = i     
                elif check_1st_diag(board, players):
                    for i in range(len(board)):
                        if board[i][i] == " ":
                            r = i
                            c = i
                elif check_2nd_diag(board, players):
                    for m in range(len(board)):
                        if board[m][x-m] == " ":
                            r = m
                            c = x-m
                # If CPU can't win or block, play random move.
                else:
                    r = random.randint(0,rows-1)
                    c = random.randint(0,rows-1)
                
                # Check the board to proceed to next turn.
                if mark_board(board, r, c, players[(turn+1)%2]):
                    print("\n\n\tTurn {}".format(turn))
                    print_board(board,separator)
                    turn = turn + 1
        # Checks the board to see if either player has won and how they won.
        if check_rows(board, players):
            print("\tPlayer {} is the winner in a row".format(players[turn%2]))
        elif check_columns(board, players):
            print("\tPlayer {} is the winner in a column".format(players[turn%2]))
        elif check_diagonals(board, players):
            print("\tPlayer {} is the winner in a diagonal".format(players[turn%2]))
        else:
            print("\tThe game was a draw")
