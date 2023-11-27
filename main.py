#Board values
tic_dict = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

#Max turns until board is full
turns = 9
is_on = False


#Condition if X or O is the winner,XXX or OOO via vertical, horizontal or diagonal
def winner():
    if tic_dict['1'] == "X" and tic_dict['2'] == "X" and tic_dict['3'] == "X":
        return "Winner X"
    elif tic_dict['1'] == "O" and tic_dict['2'] == "O" and tic_dict['3'] == "O":
        return "Winner O"

    elif tic_dict['4'] == "X" and tic_dict['5'] == "X" and tic_dict['6'] == "X":
        return "Winner X"
    elif tic_dict['4'] == "O" and tic_dict['2'] == "O" and tic_dict['3'] == "O":
        return "Winner O"

    elif tic_dict['7'] == "X" and tic_dict['8'] == "X" and tic_dict['9'] == "X":
        return "Winner X"
    elif tic_dict['7'] == "O" and tic_dict['8'] == "O" and tic_dict['9'] == "O":
        return "Winner O"

    elif tic_dict['1'] == "X" and tic_dict['4'] == "X" and tic_dict['7'] == "X":
        return "Winner X"
    elif tic_dict['1'] == "O" and tic_dict['4'] == "O" and tic_dict['7'] == "O":
        return "Winner O"

    elif tic_dict['2'] == "X" and tic_dict['5'] == "X" and tic_dict['8'] == "X":
        return "Winner X"
    elif tic_dict['2'] == "O" and tic_dict['5'] == "O" and tic_dict['8'] == "O":
        return "Winner O"

    elif tic_dict['3'] == "X" and tic_dict['6'] == "X" and tic_dict['9'] == "X":
        return "Winner X"
    elif tic_dict['3'] == "O" and tic_dict['6'] == "O" and tic_dict['9'] == "O":
        return "Winner O"

    elif tic_dict['1'] == "X" and tic_dict['5'] == "X" and tic_dict['9'] == "X":
        return "Winner X"
    elif tic_dict['1'] == "O" and tic_dict['5'] == "O" and tic_dict['9'] == "O":
        return "Winner O"

    elif tic_dict['3'] == "X" and tic_dict['5'] == "X" and tic_dict['7'] == "X":
        return "Winner X"
    elif tic_dict['3'] == "O" and tic_dict['5'] == "O" and tic_dict['7'] == "O":
        return "Winner O"


board = ("-------------\n"
         f"| {tic_dict['1']} | {tic_dict['2']} | {tic_dict['3']} |\n"
         "-------------\n"
         f"| {tic_dict['4']} | {tic_dict['5']} | {tic_dict['6']} |\n"
         "-------------\n"
         f"| {tic_dict['7']} | {tic_dict['8']} | {tic_dict['9']} |\n"
         "-------------")

print("XXX~~~~~~Welcome to TIC-TAC-TOE!~~~~~~OOO")
choice = input("Start First? Y or N: ").lower()

print(board)

while not is_on:
    mark_x = None
    mark_o = None
    if choice == "y":
        mark_x = "X"
        mark_o = "O"
    elif choice == "n":
        mark_x = "O"
        mark_o = "X"
    else:
        print("Y or N only..")

    print(f"You're Player {mark_x}!")
    player1_spot = input("Enter Spot Player 1: ")
    tic_dict[player1_spot] = mark_x
    turns -= 1
    board = ("-------------\n"
             f"| {tic_dict['1']} | {tic_dict['2']} | {tic_dict['3']} |\n"
             "-------------\n"
             f"| {tic_dict['4']} | {tic_dict['5']} | {tic_dict['6']} |\n"
             "-------------\n"
             f"| {tic_dict['7']} | {tic_dict['8']} | {tic_dict['9']} |\n"
             "-------------")
    print(board)
    if winner() == "Winner X":
        print(f"Player {mark_x}, Winner X")
        break
    elif winner() == "Winner O":
        print(f"Player {mark_x}, Winner O")
        break
    print(f"Turns: {turns}")

    print(f"You're Player {mark_o}!")
    player2_spot = input("Enter Spot Player 2: ")
    tic_dict[player2_spot] = mark_o
    turns -= 1
    board = ("-------------\n"
             f"| {tic_dict['1']} | {tic_dict['2']} | {tic_dict['3']} |\n"
             "-------------\n"
             f"| {tic_dict['4']} | {tic_dict['5']} | {tic_dict['6']} |\n"
             "-------------\n"
             f"| {tic_dict['7']} | {tic_dict['8']} | {tic_dict['9']} |\n"
             "-------------")
    print(board)
    if winner() == "Winner X":
        print(f"Player {mark_o}, Winner X")
        break
    elif winner() == "Winner O":
        print(f"Player {mark_o}, Winner O")
        break
    print(f"Turns: {turns}")

    if turns == 0:
        is_on = True




