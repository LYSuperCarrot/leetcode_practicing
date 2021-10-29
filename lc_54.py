class Solution:
    def spiralOrder(self, matrix):
        # m_left = 0
        # m_right = len(matrix[0])-1
        # n_top = 0
        # n_down = len(matrix)-1

        # result = []
        # i, j = 0, 0
        # while m_left <= m_right or n_top <= n_down:
            
        #     # move right
        #     while j < m_right:
        #         result.append(matrix[i][j])
        #         j += 1
        #     n_top += 1

        #     # move down
        #     while i < n_down:
        #         result.append(matrix[i][j])
        #         i += 1
        #     m_right -= 1

        #     # move left
        #     while j > m_left:
        #         result.append(matrix[i][j])
        #         j -= 1
        #     n_down -= 1

        #     # move up
        #     while i > n_top:
        #         result.append(matrix[i][j])
        #         i -= 1
        #     m_left += 1
        
        # total_count = len(matrix) * len(matrix[0])
        # if len(result) < total_count:
        #     result.append(matrix[i][j])
        # return result

        result = []
        if matrix == []:
            return result
        result.extend(matrix[0])
        new = [reversed(i) for i in matrix[1:]]
        if new == []:
            return result
        r = self.spiralOrder([i for i in zip(*new)])
        result.extend(r)
        return result


sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
re_matrix = sol.spiralOrder(matrix)
print(re_matrix)