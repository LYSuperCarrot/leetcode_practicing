class Solution:
    def findDiagonalOrder(self, mat):
        row, col = len(mat), len(mat[0])
        r, c = 0, 0
        result = [0 for _ in range(row*col)]
        for i in range(len(result)):
            result[i] = mat[r][c]
            if (r+c) % 2 == 0:  # 向上遍历
                if c == col - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    c += 1
                    r -= 1
            else:   # 向下遍历
                if r == row - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return result

mat = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
result = sol.findDiagonalOrder(mat)
print(result)

