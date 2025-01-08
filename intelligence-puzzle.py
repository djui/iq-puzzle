#!/usr/bin/env python3

# We only need 2 rotated positions and 2x2 flips, as a 180 degree rotation and
# its flips are identical to the 0 degree rotation and its (counter-)flips, thus
# 8 positions.
# As flipping does operations in the same space, they are preferred over
# rotations, as for rotations one needs to find the best rotation angle point.
# (criteria is to have the piece in the upper left corner after rotation)
#
# 2222  1111     4  3
#    2  1     4444  3333
#
#  8    7     55    66
#  8    7      5    6
#  8    7      5    6
# 88    77     5    6
#
# 3        4  1111  2222
# 3333  4444  1        2
#
# 66    55    7      8
# 6      5    7      8
# 6      5    7      8
# 6      5    77    88
#

## TODO: do matrix-operations to do rotations and flips.
pieces = {
    "w": [
        0b11000000000_10000000000_00000000000_00000000000_00000000000, #  0 
        0b11000000000_01000000000_00000000000_00000000000_00000000000, #  0 h
        0b10000000000_11000000000_00000000000_00000000000_00000000000, #  0 v
        0b01000000000_11000000000_00000000000_00000000000_00000000000, #  0 h+v
    ],
    "g": [
        0b01000000000_11100000000_01000000000_00000000000_00000000000, #  0
    ],
    "y": [ 
        0b11100000000_10100000000_00000000000_00000000000_00000000000, #  0
        0b10100000000_11100000000_00000000000_00000000000_00000000000, #  0 v
        0b11000000000_10000000000_11000000000_00000000000_00000000000, # 90
        0b11000000000_01000000000_11000000000_00000000000_00000000000, # 90 h
    ],
    "o": [ 
        0b11100000000_10000000000_00000000000_00000000000_00000000000, #  0
        0b11100000000_00100000000_00000000000_00000000000_00000000000, #  0 h
        0b10000000000_11100000000_00000000000_00000000000_00000000000, #  0 v
        0b00100000000_11100000000_00000000000_00000000000_00000000000, #  0 h+v
        0b11000000000_10000000000_10000000000_00000000000_00000000000, # 90
        0b11000000000_01000000000_01000000000_00000000000_00000000000, # 90 h
        0b10000000000_10000000000_11000000000_00000000000_00000000000, # 90 v
        0b01000000000_01000000000_11000000000_00000000000_00000000000, # 90 h+v
    ],
    "r": [ 
        0b11100000000_11000000000_00000000000_00000000000_00000000000, #  0
        0b11100000000_01100000000_00000000000_00000000000_00000000000, #  0 h
        0b11000000000_11100000000_00000000000_00000000000_00000000000, #  0 v
        0b01100000000_11100000000_00000000000_00000000000_00000000000, #  0 h+v
        0b11000000000_11000000000_10000000000_00000000000_00000000000, # 90
        0b10000000000_11000000000_11000000000_00000000000_00000000000, # 90 v
        0b11000000000_11000000000_01000000000_00000000000_00000000000, # 90 h
        0b01000000000_11000000000_11000000000_00000000000_00000000000, # 90 h+v
    ],
    "p": [ 
        0b11110000000_01000000000_00000000000_00000000000_00000000000, #  0
        0b11110000000_00100000000_00000000000_00000000000_00000000000, #  0 h
        0b01000000000_11110000000_00000000000_00000000000_00000000000, #  0 v
        0b00100000000_11110000000_00000000000_00000000000_00000000000, #  0 h+v
        0b10000000000_11000000000_10000000000_10000000000_00000000000, # 90
        0b01000000000_11000000000_01000000000_01000000000_00000000000, # 90 h
        0b10000000000_10000000000_11000000000_10000000000_00000000000, # 90 v
        0b01000000000_01000000000_11000000000_01000000000_00000000000, # 90 h+v
    ],
    "v": [ 
        0b11110000000_00000000000_00000000000_00000000000_00000000000, #  0
        0b10000000000_10000000000_10000000000_10000000000_00000000000, # 90
    ],
    "m": [ 
        0b11000000000_01100000000_00100000000_00000000000_00000000000, #  0
        0b01100000000_11000000000_10000000000_00000000000_00000000000, #  0 h
        0b00100000000_01100000000_11000000000_00000000000_00000000000, #  0 v
        0b10000000000_11000000000_01100000000_00000000000_00000000000, #  0 h+v
    ],
    "b": [ 
        0b11110000000_10000000000_00000000000_00000000000_00000000000, #  0
        0b11110000000_00010000000_00000000000_00000000000_00000000000, #  0 h
        0b10000000000_11110000000_00000000000_00000000000_00000000000, #  0 v
        0b00010000000_11110000000_00000000000_00000000000_00000000000, #  0 h+v
        0b11000000000_10000000000_10000000000_10000000000_00000000000, # 90
        0b11000000000_01000000000_01000000000_01000000000_00000000000, # 90 h
        0b10000000000_10000000000_10000000000_11000000000_00000000000, # 90 v
        0b01000000000_01000000000_01000000000_11000000000_00000000000, # 90 h+v
    ],
    "c": [ 
        0b11100000000_10000000000_10000000000_00000000000_00000000000, #  0
        0b11100000000_00100000000_00100000000_00000000000_00000000000, #  0 h
        0b10000000000_10000000000_11100000000_00000000000_00000000000, #  0 v
        0b00100000000_00100000000_11100000000_00000000000_00000000000, #  0 h+v
    ],
    "e": [ 
        0b01110000000_11000000000_00000000000_00000000000_00000000000, #  0
        0b11100000000_00110000000_00000000000_00000000000_00000000000, #  0 h
        0b11000000000_01110000000_00000000000_00000000000_00000000000, #  0 v
        0b00110000000_01110000000_00000000000_00000000000_00000000000, #  0 h+v
        0b10000000000_11000000000_01000000000_01000000000_00000000000, # 90
        0b01000000000_11000000000_10000000000_10000000000_00000000000, # 90 h
        0b01000000000_01000000000_11000000000_10000000000_00000000000, # 90 v
        0b10000000000_10000000000_11000000000_01000000000_00000000000, # 90 h+v
    ],
    "l": [ 
        0b11000000000_11000000000_00000000000_00000000000_00000000000, #  0
    ],
}

starting_board = {
    "w": 0b00000000000_11000000000_01000000000_00000000000_00000000000,
    "g": 0b00000000000_00000000000_00000000000_00000000000_00000000000,
    "y": 0b00000000000_00000000000_00000000000_00000000000_00000000000,
    "o": 0b00000000000_00000000000_00000000000_00000000000_00000000000,
    "r": 0b00000000000_00000000000_00000000000_00000000000_00000000000,
    "p": 0b00000000000_00000000000_00000000000_01111000000_00000000000,
    "v": 0b00000000000_00000000000_00000000000_00000000000_00000000000,
    "m": 0b00000000000_00000000000_00000000000_00000000000_00000000000,
    "b": 0b11110000000_00010000000_00000000000_00000000000_00000000000,
    "c": 0b00000000000_00000000000_10000000000_10000000000_11100000000,
    "e": 0b00000000000_00000000000_00000000000_00000000000_00000000000,
    "l": 0b00000000000_00000000000_00000000000_00000000000_00000000000,
}

colors = {
    "w": "\033[37m●\033[0m",       # white
    "g": "\033[38;5;16m●\033[0m",  # gray
    "y": "\033[33m●\033[0m",       # yellow
    "o": "\033[38;5;208m●\033[0m", # orange
    "r": "\033[31m●\033[0m",       # red
    "p": "\033[35m●\033[0m",       # pink
    "v": "\033[38;5;63m●\033[0m",  # violet
    "m": "\033[38;5;???●\033[0m",  # magenta
    "b": "\033[34m●\033[0m",       # blue
    "c": "\033[36m●\033[0m",       # cyan
    "e": "\033[32m●\033[0m",       # emerald
    "l": "\033[38;5;46m●\033[0m",  # lime
}

def print_board():
    board = [[" " for _ in range(11)] for _ in range(5)]

    # Assign colors to one board by collapsing all color boards
    for c, b in starting_board.items():
        for i in range(5*11):
            bit = (b >> (5*11-1) - i) & 1
            if bit:
                board[i // 11][i % 11] = c

    # Display the board
    for row in board:
        for col in row:
            if col == " ":
                print("·", end="")
            else:
                print(colors[col], end="")
        print("")

# Questions:
#  Q1. How to allow for backtracking? (would need 11 depth recursion)
#  Q4. How to do safe try-positioning without going out of bound? (-> Check if bits fell out counting the bits)

def debug_print(p):
    print(bin(p)[2:].zfill(55))
    print()

def debug_print_2d(p):
    rows = [(p >> (11 * i)) & 0b11111111111 for i in range(4,-1,-1)]
    debug_print_rows(rows)
    print()

def debug_print_rows(rows):
    [print(bin(row)[2:].zfill(11)) for row in rows]
    print()

def move(p, right, down):
    # Split into rows    
    rows = [(p >> (11 * i)) & 0b11111111111 for i in range(4,-1,-1)]

    # Calculate safe right-shift amount
    zeroes = [(row & -row).bit_length() - 1 for row in rows if row > 0]
    r = min(right, min(zeroes))

    # Shift all rows right
    rows = [row >> r for row in rows]

    # Shift all rows down
    while rows[-1] == 0 and down > 0:
        rows.pop()
        rows.insert(0, 0) # add empty row in the front
        down -= 1

    # Combine all rows again
    q = 0
    for row in rows:
        q = (q << 11) | row

    return q

def main():
    print_board()

    # Merge all boards to a temporary board
    board = sum(starting_board.values())

    for c, ps in pieces.items():
        # Skip pre-set pieces
        if starting_board[c]:
            continue

        valid = False

        for p in ps:
            if valid:
                continue

            for y in range(5):
                if valid:
                    continue
        
                for x in range(11):
                    if valid:
                        continue

                    # Move piece
                    p = move(p, x, y)

                    debug_print_2d(board)

                    # Add piece in certain transformation at given position
                    b = board | p

                    debug_print_2d(b)
                    import sys
                    sys.exit(1)

                    if b > 0:
                        print("piece placement invalid")
                        continue

                    if b == 0:
                        print("piece placement valid")
                        # Jump out of piece trial
                        valid = True
                        board |= p
    
    print_board()

if __name__ == "__main__":
    main()
