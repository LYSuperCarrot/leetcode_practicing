class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        for i in range(row-1):
            for j in range(i+1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(row):
            matrix[i] = matrix[i][::-1]


matrix = [1,2,3,4]
matrix = matrix[::-1]
print(matrix)
