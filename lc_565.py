class Solution:
    def arrayNesting(self, nums):
        max_len = 0
        candate = []
        for i in range(len(nums)):
            flag = False
            count = 0
            j = i
            length = len(candate)
            if length > 0:
                for k in range(length):
                    if nums[i] in candate[k]:
                        count = len(candate[k])
                        max_len = max(count, max_len)
                        flag = True
                        break
                if flag:
                    continue
                
            temp = []
            while nums[j] not in temp:
                count += 1
                temp.append(nums[j])
                j = nums[j]
            candate.append(temp)
            max_len = max(count, max_len)
            if max_len > len(nums):
                return max_len
        return max_len

A = [5,4,0,3,1,6,2]
sol = Solution()
print(sol.arrayNesting(A))