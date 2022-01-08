field = ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
game_on = True
player = "X"


def check_win():
    if field[1] == field[2] and field[1] == field[3]:
        return False
    elif field[4] == field[5] and field[4] == field[6]:
        return False
    elif field[7] == field[8] and field[7] == field[9]:
        return False
    elif field[1] == field[5] and field[1] == field[9]:
        return False
    elif field[7] == field[5] and field[7] == field[3]:
        return False
    elif field[1] == field[4] and field[1] == field[7]:
        return False
    elif field[2] == field[5] and field[2] == field[8]:
        return False
    elif field[3] == field[6] and field[3] == field[9]:
        return False
    else:
        return True


def check_draw():
    for character in field:
        if character.isdigit():
            return False
    return True


def move():
    valid_input = False
    t = input(player + " choose field: ")

    while valid_input is False:
        if t.isdigit() is True and 1 <= int(t) <= 9 and field[int(t)].isdigit() is True:
            valid_input = True
        else:
            t = input(player + " choose VALID field: ")

    return int(t)


while game_on is True:
    print(field[1] + " | " + field[2] + " | " + field[3])
    print(field[4] + " | " + field[5] + " | " + field[6])
    print(field[7] + " | " + field[8] + " | " + field[9])

    field[move()] = player
    game_on = check_win()

    if game_on is False:
        print("The winner is: " + player)

    if check_draw() is True:
        print("It's a draw!")
        game_on = False

    if player == "X":
        player = "O"
    else:
        player = "X"
