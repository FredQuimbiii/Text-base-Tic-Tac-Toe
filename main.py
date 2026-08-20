
print(r"""___________.__         ___________               ___________
\__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____
  |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \
  |    |   |  \  \___    |    |   / __ \\  \___    |    |(  <_> )  ___/
  |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >
                   \/                 \/     \/                      \/ """)

#Todo create labels for X and O points for users to identify
def show_label():
    print("How to play: When asked, please type corresponding label to mark your point(a1, a2, a3.....a9)")
    return f"""
     a1 | a2 | a3 
     ---+----+---
     a4 | a5 | a6 
     ---+----+---
     a7 | a8 | a9 
     """

#Todo create parameters for each X and O point of the game
id_1 = "X"
id_2 = "O"
board = {"a1":" ", "a2": " ", "a3": " ", "a4": " ", "a5": " ", "a6": " ", "a7": " ", "a8": " ", "a9": " "}
#Todo create ascii for the tic tac toe game
def show_game():
    return f"""
     {board["a1"]} | {board["a2"]} | {board["a3"]} 
    ---+---+---
     {board["a4"]} | {board["a5"]} | {board["a6"]} 
    ---+---+---
     {board["a7"]} | {board["a8"]} | {board["a9"]} 
    """

def clear_board():
    for lb in range(1, 10):
        board[f"a{lb}"] = " "

#Todo create questions model
def start_game():
    game_state = False
    print(show_label())
    p1 = input("Welcome, Player 1 please select an option 'X' or 'O'?").lower()
    p2 = ""
    if p1 == "x":
        p1 = id_1
        p2 = id_2
        print(f"Player 1 symbol is {p1} and Player 2 symbol is {p2}")
        print(show_game())
        game_state = True
    elif p1 == "o":
        p1 = id_2
        p2 = id_1
        print(f"Player 1 symbol is {p1} and Player 2 symbol is {p2}")
        print(show_game())
        game_state = True
    else:
        print("Wrong input, please try again")
        start_game()

    p1_turn = True
    p2_turn = False

    # Todo create update model
    def update_board(player, player_id):
        player_input = input(f"Player: {player} please choose a label between 'a1 - a9' to mark your point").lower()
        if player_input in board:
            if board[player_input] == " ":
                board[player_input] = player_id
                return show_game()
            else:
                print("mark taken, try another.")
                return False
        else:
            print("No such label, please try again")
            return False
    label_count = 0
    p1_score = 0
    p2_score = 0

    def play_again():
        p_again = input("Print do you want to play again? (yes/no)").lower()
        if p_again == "yes":
            return "yes"
        elif p_again == "no":
            return "no"
        else:
            print("Wrong input!")
            return play_again()



    def check_winner(player):
        if board["a1"] == player and board["a2"] == player and board["a3"] == player:
            return "False"
        elif board["a4"] == player and board["a5"] == player and board["a6"] == player:
            return "False"
        elif board["a7"] == player and board["a8"] == player and board["a9"] == player:
            return "False"
        elif board["a1"] == player and board["a4"] == player and board["a7"] == player:
            return "False"
        elif board["a2"] == player and board["a5"] == player and board["a8"] == player:
            return "False"
        elif board["a3"] == player and board["a6"] == player and board["a9"] == player:
            return "False"
        elif board["a1"] == player and board["a5"] == player and board["a9"] == player:
            return "False"
        elif board["a3"] == player and board["a5"] == player and board["a7"] == player:
            return "False"
        else:
            return "True"
    while game_state:
        while p1_turn:
            # print(f"Score: P1-{p1_score}  P2-{p2_score}")
            print(f"Score: Player 1  Player 2\n"
                  f"         {p1_score}        {p2_score}")
            p1_label = update_board(player=1, player_id=p1)
            print(show_game())
            if p1_label:
                p2_turn = True
                p1_turn = False
                label_count += 1
                if check_winner(p1) == "False":
                    p1_score += 1
                    print("Player 1 wins!")
                    label_count = 0
                    status = play_again()
                    if status == "yes":
                        clear_board()
                        print("Player 2 starts!")
                        print(show_game())
                    elif status == "no":
                        print("p1 Game Over!")
                        game_state = False
                        p2_turn = False
                elif label_count == 9:
                    print("Its a Draw!")
                    label_count = 0
                    status = play_again()
                    if status == "yes":
                        clear_board()
                        print("Player 2 starts!")
                        print(show_game())
                    elif status == "no":
                        print("Game Over!")
                        game_state = False
                        p2_turn = False
        while p2_turn:
            print(f"Score: Player 1  Player 2\n"
                  f"         {p1_score}        {p2_score}")
            p2_label = (update_board(player=2, player_id=p2))
            print(show_game())
            if p2_label:
                p1_turn = True
                p2_turn = False
                label_count += 1
                if check_winner(p2) == "False":
                    p2_score += 1
                    print("Player 2 wins!")
                    label_count = 0
                    status = play_again()
                    if status == "yes":
                        clear_board()
                        print("Player 1 starts!")
                        print(show_game())
                    elif status == "no":
                        print("Game Over!")
                        game_state = False

                elif label_count == 9:
                    print("Its a Draw!")
                    label_count = 0
                    status = play_again()
                    if status == "yes":
                        clear_board()
                        print("Player 1 starts!")
                        print(show_game())
                    elif status == "no":
                        print("Game Over!")
                        game_state = False

start_game()


#Todo create score board model