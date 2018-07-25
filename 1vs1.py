import os


def clear():
    if (ms_terminal == False): return
    try:
        os.system('cls')
    except:
        os.system('clear')


from enum import Enum


# region keypress
class arrowkeys(Enum):
    up = 72
    down = 80
    left = 75
    right = 77


ms_terminal = True
try:
    from msvcrt import getch
    from sys import modules

    if ("idlelib" in modules): i = 1 / 0
except ImportError:
    ms_terminal = False
except ZeroDivisionError:
    ms_terminal = False


def getkey():
    if (ms_terminal):
        while True:  # get key press
            key = ord(getch())
            if key == 32:  # space
                return "space"
            elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
                key = ord(getch())
                return arrowkeys(key).name
    else:
        key = "0"
        domain = "wasdpWASDP"
        print("[w : ↑][a : ←][s : ↓][d : →][p: place]")
        while (key not in domain):
            key = str(input(">"))
            try:
                key = key[0].lower()
            except:
                pass
        if (key == 'w'):
            return "up"
        elif (key == 'a'):
            return "left"
        elif (key == 's'):
            return "down"
        elif (key == 'd'):
            return "right"
        elif (key == 'p'):
            return "space"


# endregion
'''
while (True):
    c = getkey()
    print(c)
'''
maps = []


# initialize map
class settings:
    width = 8


for i in range(0, settings.width):
    maps.append([])
for i in range(0, settings.width):
    for j in range(0, settings.width):
        maps[i].append(0)


def printmap():
    for row in maps:
        for column in row:
            if (column == 0):
                print(' ', end="")
            else:
                print(column, end="")
        print(end="\n")


def place(x, y, n):
    clear()
    print("%c's turn." % n)
    i = 0
    for row in maps:
        j = 0
        for column in row:
            if (i == y and j == x):
                print('^', end='')
            else:
                if (column == 0):
                    print(" ", end='')
                else:
                    print(column, end='')
            j += 1
        print()
        i += 1
    # get userinput
    while (True):
        c = getkey()
        if (c == "up" and y - 1 >= 0):
            place(x, y - 1, n)
        elif (c == "left" and x - 1 >= 0):
            place(x - 1, y, n)
        elif (c == "right" and x + 1 < settings.width):
            place(x + 1, y, n)
        elif (c == "down" and y + 1 < settings.width):
            place(x, y + 1, n)
        elif (c == "space" and maps[y][x] == 0):
            # print("you replaced %d at %d, %d" %(maps[y][x],x,y))
            maps[y][x] = n
            check()
            if (n == 'X'):
                n = 'O'
            else:
                n = 'X'
            place(x, y, n)
            return
        else:
            print("Invalid Move")


def win(x):
    clear()
    printmap()
    print("%c has won!" % x)
    input("press enter to restart game")
    maps[:] = []
    for i in range(0, settings.width):
        maps.append([])
    for i in range(0, settings.width):
        for j in range(0, settings.width):
            maps[i].append(0)
    place(0, 0, 'X')


def checkstr(x):
    # print(x)
    if (x[0] == '0'): return False
    for t in range(1, len(x)):
        if (x[t] != x[t - 1]): return False
    return True


def check():
    for i in range(0, settings.width):
        for j in range(0, settings.width):
            n = str(maps[j][i])
            tmp = n
            # diag
            try:
                tmp += str(maps[j + 1][i + 1])
                tmp += str(maps[j + 2][i + 2])
                tmp += str(maps[j + 3][i + 3])
                if (checkstr(tmp)): win(n)
            except IndexError:
                pass
            tmp = n
            # opp diag
            try:
                tmp += str(maps[j + 1][i - 1])
                tmp += str(maps[j + 2][i - 2])
                tmp += str(maps[j + 3][i - 3])
                if (checkstr(tmp)): win(n)
            except IndexError:
                pass
            tmp = n
            # vertical
            try:
                tmp += str(maps[j + 1][i])
                tmp += str(maps[j + 2][i])
                tmp += str(maps[j + 3][i])
                if (checkstr(tmp)): win(n)
            except IndexError:
                pass
            tmp = n
            # horizontal
            try:
                tmp += str(maps[j][i + 1])
                tmp += str(maps[j][i + 2])
                tmp += str(maps[j][i + 3])
                if (checkstr(tmp)): win(n)
            except IndexError:
                pass


place(0, 0, 'X')
