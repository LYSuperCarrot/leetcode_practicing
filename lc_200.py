

# class Solution:
#     def __init__(self):
#         self.island_num = 0

#     def numIslands(self, grid) -> int:
#         sea = self.generate_sea_grid(grid)
#         for i in range(1, len(sea)-1):
#             for j in range(1, len(sea[0])-1):
#                 if sea[i][j] == '1':
#                     if sea[i-1][j] == '0' and sea[i][j-1] == '0':
#                         self.island_num += 1
#         return self.island_num

    
#     def generate_sea_grid(self, grid):
#         row = len(grid)
#         col = len(grid[0])
#         sea_row = row + 2
#         sea_col = col + 2
#         sea = [['0' for _ in range(sea_col)] for _ in range(sea_row)]
#         for i in range(1, sea_row-1):
#             for j in range(1, sea_col-1):
#                 sea[i][j] = grid[i-1][j-1]
#         return sea
class Solution:

    def numIslands(self, grid) -> int:
        islandNum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.infect(grid, i, j)
                    islandNum += 1
        return islandNum

    def infect(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '2'
        self.infect(grid, i-1, j)
        self.infect(grid, i+1, j)
        self.infect(grid, i, j-1)
        self.infect(grid, i, j+1)

grid = [
  ["1","1","1"],
  ["0","1","0"],
  ["1","1","1"],
]
sol = Solution()

# print(sol.generate_sea_grid(grid))
# island_num = sol.numIslands(grid)
sol.infect(grid, 0, 0)
print(grid)