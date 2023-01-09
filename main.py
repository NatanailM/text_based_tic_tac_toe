table = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

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


def print_table():
    print(f"\n {table[0]} | {table[1]} | {table[2]} \n"
          f" --------- \n"
          f" {table[3]} | {table[4]} | {table[5]} \n"
          f" --------- \n"
          f" {table[6]} | {table[7]} | {table[8]} ")


input_map = {
    "00": 0, "01": 1, "02": 2,
    "10": 3, "11": 4, "12": 5,
    "20": 6, "21": 7, "22": 8,
}

current_player = "X"

while True:
    print_table()
    print(f"\n{current_player}'s turn.")
    while True:
        x = input("Where do you want to put the marker: ")
        if x in input_map and table[input_map[x]] == " ":
            table[input_map[x]] = current_player
            break
        print("Invalid input. Try again.")

    if check_win(current_player):
        print_table()
        break
    if check_draw():
        print_table()
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"
