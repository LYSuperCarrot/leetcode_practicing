class Solution:
    def leastBricks(self, wall) -> int:
        res = {0: 0}
        for lvl in wall:
            pos = 0
            for brick in lvl[:-1]:
                pos += brick
                res[pos] = res.get(pos, 0) +1
        return len(wall)-max(res.values())

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]

sol = Solution()
sol.leastBricks(wall)