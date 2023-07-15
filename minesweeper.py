grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]


def minesweeper():
    rows = len(grid)
    columns = len(grid[0])
    empty_grid = [['0' for imlosingmysanity in range(columns)] for abcd in range(rows)] # CREATING A 2D LIST WITH THE SAME ROWS AND COLUMNS

    for row_index in range(rows):
        for col_index in range(columns):
            if grid[row_index][col_index] == '#':
                empty_grid[row_index][col_index] = '#' # IF GRID.INDEX.INDEX == # APPENDS EMPTY_GRID.INDEX.INDEX TO A #
            else: # IF GRID.INDEX.INDEX == "-"
                count = 0
                for i in range(max(0, row_index - 1), min(rows, row_index + 2)):  # ENSURES CODE DOESNT GO NEGATIVE INDEX AND DOESNT EXCEED THE ENDING INDEXES
                    for j in range(max(0, col_index - 1), min(columns, col_index + 2)):  # READS LINES ADJACENT/ABOVE/BELOW THE INDEXES
                        if grid[i][j] == '#': # IF GRID.INDEX.INDEX = # BOMB
                            count += 1 # COUNTS +1 IF A BOMB IS NEARBY
                empty_grid[row_index][col_index] = str(count)  # EMPTY GRID.INDEX.INDEX = COUNT (OF BOMBS NEARBY)
    print(empty_grid)  # EMPTY GRID.INDEX.INDEX = COUNT (OF BOMBS NEARBY)
minesweeper()



