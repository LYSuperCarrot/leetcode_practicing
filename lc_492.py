class Solution:
    def constructRectangle(self, area):
        diff = float('inf')
        result = [0, 0]
        if area == 0:
            return result
        for width in range(1, area//2+2):
            length = area / width
            if int(length) == length and abs(length-width) < diff:
                diff = abs(length-width)
                result[0] = max(int(length), width)
                result[1] = min(int(length), width)
        return result

# area = 1
# sol = Solution()
# print(sol.constructRectangle(area))
a = "-2"
print(int(a))