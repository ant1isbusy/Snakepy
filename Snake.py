
import random

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
SNAKE = ["D2", "D3", "D4"]
ORIENTATION = 5

APPLE = "G4"
APPLE_LIVES = 12
APPLE_GOT_EATEN = False
LIVES = 3
SCORE = 0
BIGGER_SNAKE = False
rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
columns = ["0", "1", "2", "3", "4", "5", "6", "7"]

def _7_submit_score():
    global SNAKE, SCORE, LIVES
    SNAKE_LENGTH = len(SNAKE)
    UserName = input("Your name for the history: ")
    userstats = UserName + " - Score: " + \
        str(SCORE) + " - Lives: " + str(LIVES) + \
        " - Snake Length: " + str(SNAKE_LENGTH) + "\n"

    with open("history.txt", "a") as highscores:
        highscores.write(userstats)
    print("\n\nHistory:")

    with open("history.txt", "r") as history:
        playersLIST = history.readlines()
        if len(playersLIST) == 5:
            leaderboard = playersLIST[1:]
            with open("history.txt", "w") as history:
                for player in leaderboard:
                    history.write(player)
            print(*leaderboard, sep="", end="")
        else:
            print(*playersLIST, sep="", end="")


def _6_spawn_apple():
    global APPLE, SNAKE, APPLE_LIVES, LIVES
    APPLE_LIVES = APPLE_LIVES - 1
    if APPLE_LIVES < 1 and APPLE_GOT_EATEN == False:
        while True:
            newAPPLE = random.choice(rows) + str(random.choice(range(0, 8)))
            if newAPPLE not in SNAKE and newAPPLE != APPLE:
                APPLE = newAPPLE
                break

    if APPLE_GOT_EATEN == True:
        APPLE_LIVES = 12
        while True:
            newAPPLE = random.choice(rows) + str(random.choice(range(0, 8)))
            if newAPPLE not in SNAKE:
                APPLE = newAPPLE
                break

    if APPLE_LIVES == 0:
        LIVES = LIVES - 1
        APPLE_LIVES = 12


def _5_detect_collision():
    global BIGGER_SNAKE, APPLE_GOT_EATEN
    # using ascii characters for borders out of range
    nextrow = chr(ord(SNAKE[-1][0]))
    nextcol = chr(ord(SNAKE[-1][1]))
    if nextrow == "@":
        return True
    if nextrow == "I":
        return True
    if nextcol == "8":
        return True
    if nextcol == "/":
        return True

    if SNAKE[-1] == APPLE:
        BIGGER_SNAKE = True
        APPLE_GOT_EATEN = True
    else:
        BIGGER_SNAKE = False
        APPLE_GOT_EATEN = False

    body = SNAKE[:-1]
    if SNAKE[-1] in body:
        return True


def _4_move_snake():
    if ORIENTATION == 2:
        snakehead = str(chr(ord(SNAKE[-1][0]) - 1)) + str(SNAKE[-1][1])
        SNAKE.append(snakehead)
        if BIGGER_SNAKE == False:
            del SNAKE[0]

    elif ORIENTATION == 4:
        snakehead = str(chr(ord(SNAKE[-1][0]) + 1)) + str(SNAKE[-1][1])
        SNAKE.append(snakehead)
        if BIGGER_SNAKE == False:
            del SNAKE[0]

    if ORIENTATION == 3:
        snakehead = str(SNAKE[-1][0]) + str(chr(ord(SNAKE[-1][1]) - 1))
        SNAKE.append(snakehead)
        if BIGGER_SNAKE == False:
            del SNAKE[0]

    if ORIENTATION == 5:
        snakehead = str(SNAKE[-1][0]) + str(chr(ord(SNAKE[-1][1]) + 1))
        SNAKE.append(snakehead)
        if BIGGER_SNAKE == False:
            del SNAKE[0]


def _3_is_snake(row, column):
    if row == SNAKE[-1][0] and column == SNAKE[-1][1]:
        return ORIENTATION

    for snakecord in SNAKE:
        if row == snakecord[0] and column == snakecord[1]:
            is_snake = 1
            break
        elif row != snakecord[0] or column != snakecord[1]:
            is_snake = 0
    return is_snake


def _2_is_apple(row, column):
    if (row == APPLE[0] and column == APPLE[1]):
        return True
    else:
        return False


def _1_print_game_board():
    print("Lives:", LIVES, "- Apple Lives:", APPLE_LIVES, "- Score:", SCORE)
    print("----------------------------")
    for row in rows:
        print(row + " |", end="")
        for col in columns:
            if _2_is_apple(row, col):
                print(" O ", end="")
                continue
            if _3_is_snake(row, col) == 1:
                print(" + ",  end="")
                continue
            elif _3_is_snake(row, col) == 2:
                print(" ∧ ", end="")
                continue
            elif _3_is_snake(row, col) == 3:
                print(" < ", end="")
                continue
            elif _3_is_snake(row, col) == 4:
                print(" v ", end="")
                continue
            elif _3_is_snake(row, col) == 5:
                print(" > ", end="")
                continue
            print("   ", end="")
        print("|")
    print("----------------------------")
    print("    0  1  2  3  4  5  6  7")


def main():
    global SCORE, ORIENTATION
    while True:
        _1_print_game_board()
        if LIVES == 0:
            return
        userinput = input("input [w a s d]:")
        if ORIENTATION == 4 and userinput == "w":
            print("INVALID")
            continue
        elif userinput == "w":
            ORIENTATION = 2
        if ORIENTATION == 5 and userinput == "a":
            print("INVALID")
            continue
        elif userinput == "a":
            ORIENTATION = 3
        if ORIENTATION == 2 and userinput == "s":
            print("INVALID")
            continue
        elif userinput == "s":
            ORIENTATION = 4
        if ORIENTATION == 3 and userinput == "d":
            print("INVALID")
            continue
        elif userinput == "d":
            ORIENTATION = 5
        if userinput == "q":
            exit(0)

        _4_move_snake()
        if _5_detect_collision() == True:
            return
        SCORE = SCORE + 1
        _6_spawn_apple()


if __name__ == '__main__':
    main()
    _7_submit_score()
