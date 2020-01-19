# https://leetcode.com/problems/island-perimeter/submissions/

def islandPerimeter(grid) -> int:
    def traverse(grid, x, y):
        if x >= len(grid[0]) or y >= len(grid) or x < 0 or y < 0 or grid[y][x] == 0: 
            return 1

        if grid[y][x] == 2:
            return 0

        # marking a tile with 2 means we visited it already, no perimeter added
        grid[y][x] = 2
        perimeter = 0

        perimeter += traverse(grid, x, y-1)
        perimeter += traverse(grid, x, y+1) 
        perimeter += traverse(grid, x+1, y)
        perimeter += traverse(grid, x-1, y)

        return perimeter


    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                return traverse(grid, x, y)
