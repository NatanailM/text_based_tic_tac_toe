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


winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]  # diagonals
]


def check_win(player):
    for combination in winning_combinations:
        if all(table[i] == player for i in combination):
            print(f"\n{player} has won!")
            return True
    return False


def check_draw():
    return all(cell != " " for cell in table)


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
                if check_win("X"):
                    # Print out the table if player 1 has won.
                    print_table()
                    break
                else:
                    # If he hasn't, make it player 2's turn
                    player2 = True

                # Check if it's a draw
                if check_draw():
                    # Print out the table if it's a draw.
                    print_table()
                    print("It's a draw!")
                    break
            else:
                print("\nYou can't place it there. Try again.")

        # If player1 wants to put x in second row

        elif x[0] == "1":

            # Check if that spot is empty
            if table[int(x[2]) + 3] == " ":
                table[int(x[2]) + 3] = "X"
                player1 = False

                # Check if player 1 has won.
                if check_win("X"):
                    # Print out the table if player 1 has won.
                    print_table()
                    break
                else:
                    # If he hasn't, make it player 2's turn
                    player2 = True

                # Check if it's a draw
                if check_draw():
                    # Print out the table if it's a draw.
                    print_table()
                    print("It's a draw!")
                    break
            else:
                print("\nYou can't place it there. Try again.")

        # If player1 wants to put x in third row

        elif x[0] == "2":

            # Check if that spot is empty
            if table[int(x[2]) + 6] == " ":
                table[int(x[2]) + 6] = "X"
                player1 = False

                # Check if player 1 has won.
                if check_win("X"):
                    # Print out the table if player 1 has won.
                    print_table()
                    break
                else:
                    # If he hasn't, make it player 2's turn
                    player2 = True

                # Check if it's a draw
                if check_draw():
                    # Print out the table if it's a draw.
                    print_table()
                    print("It's a draw!")
                    break
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

                # Check if player 1 has won.
                if check_win("O"):
                    # Print out the table if player 2 has won.
                    print_table()
                    break
                else:
                    # If he hasn't, make it player 1's turn
                    player1 = True

                # Check if it's a draw
                if check_draw():
                    # Print out the table if it's a draw.
                    print_table()
                    print("\nIt's a draw!")
                    break
            else:
                print("\nYou can't place it there. Try again.")

        # If player2 wants to put o in second row
        elif o[0] == "1":

            # Check if that spot is empty
            if table[int(o[2]) + 3] == " ":
                table[int(o[2]) + 3] = "O"
                player2 = False

                # Check if player 2 has won.
                if check_win("O"):
                    # Print out the table if player 2 has won.
                    print_table()
                    break
                else:
                    # If he hasn't, make it player 1's turn
                    player1 = True

                # Check if it's a draw
                if check_draw():
                    # Print out the table if it's a draw.
                    print_table()
                    print("\nIt's a draw!")
                    break
            else:
                print("\nYou can't place it there. Try again.")

        # If player2 wants to put o in third row
        elif o[0] == "2":

            # Check if that spot is empty
            if table[int(o[2]) + 6] == " ":
                table[int(o[2]) + 6] = "O"
                player2 = False

                # Check if player 2 has won.
                if check_win("O"):
                    # Print out the table if player 2 has won.
                    print_table()
                    break
                else:
                    # If he hasn't, make it player 1's turn
                    player1 = True

                # Check if it's a draw
                if check_draw():
                    # Print out the table if it's a draw.
                    print_table()
                    print("\nIt's a draw!")
                    break

            else:
                print("\nYou can't place it there. Try again.")
        else:
            print("\nYou can't playce it there. Try again.")
