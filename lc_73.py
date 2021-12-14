class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeros.append([i, j])
        
        r_set = []
        c_set = []
        for z in zeros:
            r_set.append(z[0])
            c_set.append(z[1])
        r_set = set(r_set)
        c_set = set(c_set)
        row_zeros = [0 for _ in range(col)]
        for row_num in r_set:
            matrix[row_num] = row_zeros
        
        for col_num in c_set:
            for i in range(row):
                matrix[i][col_num] = 0



matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol = Solution()
sol.setZeroes(matrix)
print(matrix)

    