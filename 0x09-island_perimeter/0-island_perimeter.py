#!/usr/bin/python3
''' Island Perimeter '''


def island_perimeter(grid):
    ''' island perimeter '''
    perimeter = 0
    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                # check left
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # check right
                if j + 1 == col or grid[i][j + 1] == 0:
                    perimeter += 1
                # check top
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # check bottom
                if i + 1 == row or grid[i + 1][j] == 0:
                    perimeter += 1
    return perimeter
