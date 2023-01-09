table = [" ", " ", " ", " ", " ", " ", " ", " ", " "]



game = True
player1 = True
player2 = False


def print_table():
    global table

    print(f"\n {table[0]} | {table[1]} | {table[2]} \n"
          f" --------- \n"
          f" {table[3]} | {table[4]} | {table[5]} \n"
          f" --------- \n"
          f" {table[6]} | {table[7]} | {table[8]} ")


def check_win_for_x():
    global game
    if table[0] == "X" and table[1] == "X" and table[2] == "X":
        print("Player 1 Has Won!")
        game = False
        return True
    elif table[3] == "X" and table[4] == "X" and table[5] == "X":
        print("Player 1 Has Won!")
        game = False
        return True
    elif table[6] == "X" and table[7] == "X" and table[8] == "X":
        print("Player 1 Has Won!")
        game = False
        return True
    elif table[0] == "X" and table[3] == "X" and table[6] == "X":
        print("Player 1 Has Won!")
        game = False
        return True
    elif table[1] == "X" and table[4] == "X" and table[7] == "X":
        print("Player 1 Has Won!")
        game = False
        return True
    elif table[2] == "X" and table[5] == "X" and table[8] == "X":
        print("Player 1 Has Won!")
        game = False
        return True
    elif table[0] == "X" and table[4] == "X" and table[8] == "X":
        print("Player 1 Has Won!")
        game = False
        return True
    elif table[2] == "X" and table[4] == "X" and table[6] == "X":
        print("Player 1 Has Won!")
        game = False
        return True
    elif table[0] != " " and table[1] != " " and table[2] != " " and table[3] != " " and table[4] != " " and table[5] != " " and table[6] != " " and table[7] != " " and table[8] != " ":
        print("It's a draw!")
        game = False
        return True


def check_win_for_o():
    global game
    if table[0] == "O" and table[1] == "O" and table[2] == "O":
        print("Player 2 Has Won!")
        game = False
        return True
    elif table[3] == "O" and table[4] == "O" and table[5] == "O":
        print("Player 2 Has Won!")
        game = False
        return True
    elif table[6] == "O" and table[7] == "O" and table[8] == "O":
        print("Player 2 Has Won!")
        game = False
        return True
    elif table[0] == "O" and table[3] == "O" and table[6] == "O":
        print("Player 2 Has Won!")
        game = False
        return True
    elif table[1] == "O" and table[4] == "O" and table[7] == "O":
        print("Player 2 Has Won!")
        game = False
        return True
    elif table[2] == "O" and table[5] == "O" and table[8] == "O":
        print("Player 2 Has Won!")
        game = False
        return True
    elif table[0] == "O" and table[4] == "O" and table[8] == "O":
        print("Player 2 Has Won!")
        game = False
        return True
    elif table[2] == "O" and table[4] == "O" and table[6] == "O":
        print("Player 2 Has Won!")
        game = False
        return True
    elif table[0] != " " and table[1] != " " and table[2] != " " and table[3] != " " and table[4] != " " and table[5] != " " and table[6] != " " and table[7] != " " and table[8] != " ":
        print("It's a draw!")
        game = False
        return True


# If none of the players have won repeat this.

while game:

    # If it is player1's turn.
    if player1:

        # Print out the table
        print_table()

        x = input("\nWhere do you want to put the x: ")

        # If player1 wants to put x in the first row.
        if x[0] == "0":

            # Check if that spot is empty
            if table[int(x[2])] == " ":
                table[int(x[2])] = "X"
                player1 = False

                # Check if player 1 has won.
                if check_win_for_x():
                    # Print out the table if player 1 has won.
                    print_table()
                else:
                    # If he hasn't, make it player 2's turn
                    player2 = True
            else:
                print("\nYou can't place it there. Try again.")

        # If player1 wants to put x in second row

        elif x[0] == "1":

            # Check if that spot is empty
            if table[int(x[2]) + 3] == " ":
                table[int(x[2]) + 3] = "X"
                player1 = False

                # Check if player 1 has won.
                if check_win_for_x():
                    # Print out the table if player 1 has won.
                    print_table()
                else:
                    # If he hasn't, make it player 2's turn
                    player2 = True

            else:
                print("\nYou can't place it there. Try again.")

        # If player1 wants to put x in third row

        elif x[0] == "2":

            # Check if that spot is empty
            if table[int(x[2]) + 6] == " ":
                table[int(x[2]) + 6] = "X"
                player1 = False

                # Check if player 1 has won.
                if check_win_for_x():
                    # Print out the table if player 1 has won.
                    print_table()
                else:
                    # If he hasn't, make it player 2's turn
                    player2 = True

            else:
                print("\nYou can't place it there. Try again.")
        else:
            print("\nYou can't playce it there. Try again.")

    # If it is player2's turn
    if player2:
        print(f"\n {table[0]} | {table[1]} | {table[2]} \n"
              f" --------- \n"
              f" {table[3]} | {table[4]} | {table[5]} \n"
              f" --------- \n"
              f" {table[6]} | {table[7]} | {table[8]} ")
        o = input("\nWhere do you want to put the o: ")

        # If player2 wants to put o in first row
        if o[0] == "0":

            # Check if that spot is empty
            if table[int(o[2])] == " ":
                table[int(o[2])] = "O"
                player2 = False

                # Check if player 2 has won
                if check_win_for_o():
                    # Print out the table if player 2 has won.
                    print_table()
                else:
                    # If he hasn't, make it player 1's turn
                    player1 = True

            else:
                print("\nYou can't place it there. Try again.")

        # If player2 wants to put o in second row
        elif o[0] == "1":

            # Check if that spot is empty
            if table[int(o[2]) + 3] == " ":
                table[int(o[2]) + 3] = "O"
                player2 = False

                # Check if player 2 has won
                if check_win_for_o():
                    # Print out the table if player 2 has won.
                    print_table()
                else:
                    # If he hasn't, make it player 1's turn
                    player1 = True

            else:
                print("\nYou can't place it there. Try again.")

        # If player2 wants to put o in third row
        elif o[0] == "2":

            # Check if that spot is empty
            if table[int(o[2]) + 6] == " ":
                table[int(o[2]) + 6] = "O"
                player2 = False

                # Check if player 2 has won
                if check_win_for_o():
                    # Print out the table if player 2 has won.
                    print_table()
                else:
                    # If he hasn't, make it player 1's turn
                    player1 = True

            else:
                print("\nYou can't place it there. Try again.")
        else:
            print("\nYou can't playce it there. Try again.")
