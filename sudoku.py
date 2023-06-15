""""
Sudoku auto-solver!
"""

table = [
    [0, 0, 0, 3, 8, 2, 7, 0, 0],
    [2, 0, 7, 5, 1, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [7, 0, 0, 9, 0, 0, 2, 0, 8],
    [0, 0, 1, 0, 0, 0, 6, 0, 0],
    [6, 0, 8, 0, 0, 7, 0, 0, 5],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 7, 9, 5, 0, 3],
    [0, 0, 6, 4, 5, 1, 0, 0, 0],
]


def print_table():

    for i in range(len(table)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        for j in range(len(table[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(str(table[i][j]))
            else:
                print(str(table[i][j]) + " ", end="")


def valid(table, num, pos):
    valid = True
    for i in range(len(table)):

        if table[pos[0]][i] == num and pos[1] != i:
            print(f"invalid number {num} at position {pos}," +
                  f"coincides with the number at position {pos[0]}, {i}")
            valid = False
            break
        
        elif table[i][pos[1]] == num and pos[0] != i:
            print(f"invalid number {num} at position {pos}," +
                  f"coincides with the number at position {i}, {pos[1]}")
            valid = False
            break

    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if table[i][j] == num and (i, j) != pos:
                valid = False
                break
        
        if not valid:
            break

    return valid


def find_empty(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 0:
                return(i, j)
        

def solve(table):
    empty_pos = find_empty(table)

    if not empty_pos:
        print("Everything filled!")
        return True
    else:
        row, col = empty_pos

    for i in range(1,10):
        if valid(table, i (row, col)):
            table[row][col] = i

            if solve(table):
                return True
            
            table[row][col] = 0

    return False

print_table()
valid(table, 4, (2, 3))