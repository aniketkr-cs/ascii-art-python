WIDTH = 80
HEIGHT = 35

r = 0
while r < HEIGHT:
    c = 0
    while c < WIDTH:

        # ROW 0
        if r == 0:
            ch = "+" if 31 <= c <= 42 else " "

        # ROW 1
        elif r == 1:
            ch = "+" if 24 <= c <= 48 else " "

        # ROW 2
        elif r == 2:
            ch = "+" if (22 <= c <= 33 or 43 <= c <= 50) else " "

        # ROW 3
        elif r == 3:
            ch = "+" if (18 <= c <= 31 or 46 <= c <= 51) else " "

        # ROW 4
        elif r == 4:
            ch = "+" if (17 <= c <= 30 or 45 <= c <= 50) else " "

        # ROW 5
        elif r == 5:
            ch = "+" if (15 <= c <= 28 or 48 <= c <= 53) else " "

        # ROW 6
        elif r == 6:
            ch = "+" if (15 <= c <= 17 or 19 <= c <= 23 or 49 <= c <= 52) else " "

        # ROW 7
        elif r == 7:
            ch = "+" if (13 <= c <= 21 or 49 <= c <= 52) else " "

        # ROW 8
        elif r == 8:
            ch = "+" if (11 <= c <= 15 or 17 <= c <= 21 or 51 <= c <= 54) else " "

        # ROW 9
        elif r == 9:
            ch = "+" if (11 <= c <= 13 or 17 <= c <= 20 or 55 <= c <= 56) else " "

        # ROW 10
        elif r == 10:
            ch = "+" if (12 <= c <= 13 or 18 <= c <= 21) else " "

        # ROW 11
        elif r == 11:
            ch = "+" if 17 <= c <= 21 else " "

        # ROW 12
        elif r == 12:
            ch = "+" if 18 <= c <= 22 else " "

        # ROW 13
        elif r == 13:
            ch = "+" if 20 <= c <= 23 else " "

        # ROW 14
        elif r == 14:
            ch = "+" if (12 <= c <= 13 or 20 <= c <= 22) else " "

        # ROW 15
        elif r == 15:
            ch = "+" if (8 <= c <= 9 or 11 <= c <= 13 or c == 20 or 22 <= c <= 27) else " "

        # ROW 16
        elif r == 16:
            ch = "+" if (10 <= c <= 12 or 20 <= c <= 25 or 26 <= c <= 28 or
                          29 <= c <= 31 or 39 <= c <= 40 or 41 <= c <= 43 or
                          44 <= c <= 47) else " "

        # ROW 17
        elif r == 17:
            ch = "+" if (10 <= c <= 12 or 18 <= c <= 33 or 41 <= c <= 46 or c == 49) else " "

        # ROW 18
        elif r == 18:
            ch = "+" if (11 <= c <= 13 or 19 <= c <= 26 or c == 27 or c == 29 or
                          30 <= c <= 35 or c == 43 or 45 <= c <= 47) else " "

        # ROW 19
        elif r == 19:
            ch = "+" if (19 <= c <= 23 or c == 29 or 32 <= c <= 34) else " "

        # ROW 20
        elif r == 20:
            ch = "+" if (c == 13 or c == 18 or 30 <= c <= 34) else " "

        # ROW 21
        elif r == 21:
            ch = "+" if (18 <= c <= 19 or 30 <= c <= 33) else " "

        # ROW 22
        elif r == 22:
            ch = "+" if (16 <= c <= 23 or 31 <= c <= 33) else " "

        # ROW 23
        elif r == 23:
            ch = "+" if (16 <= c <= 23 or 25 <= c <= 26 or 29 <= c <= 33) else " "

        # ROW 24
        elif r == 24:
            ch = "+" if (16 <= c <= 27 or 30 <= c <= 34) else " "

        # ROW 25
        elif r == 25:
            ch = "+" if 17 <= c <= 36 else " "

        # ROW 26
        elif r == 26:
            ch = "+" if (17 <= c <= 34 or c == 36) else " "

        # ROW 27
        elif r == 27:
            ch = "+" if 17 <= c <= 31 else " "

        # ROW 28
        elif r == 28:
            ch = "+" if (18 <= c <= 34 or 43 <= c <= 44) else " "

        # ROW 29
        elif r == 29:
            ch = "+" if 19 <= c <= 39 else " "

        # ROW 30
        elif r == 30:
            ch = "+" if 20 <= c <= 31 else " "

        # ROW 31
        elif r == 31:
            ch = "+" if 21 <= c <= 28 else " "

        # ROW 32
        elif r == 32:
            ch = "+" if 23 <= c <= 33 else " "

        # ROW 33
        elif r == 33:
            ch = "+" if (27 <= c <= 41 or 44 <= c <= 45) else " "

        # ROW 34
        elif r == 34:
            ch = "+" if 29 <= c <= 45 else " "

        else:
            ch = " "

        print(ch, end="")
        c += 1

    print()
    r += 1
