# from collections import deque

# # 链表
# linkedlist = deque()
# linkedlist.append(1)
# linkedlist.append(2)
# linkedlist.append(3)

# linkedlist.insert(2, 99)
# linkedlist.append(99)
# # del linkedlist[2]
# linkedlist.remove(99)
# print(linkedlist)
# print(len(linkedlist))

# li = [3,2,3,1,2,4,5,5,6]
# li.sort(reverse=True)
# print(li)

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# row = len(matrix)
# col = len(matrix[0])

# nums = [2,3,1,2,4,3]
# print(nums[5:6])
# class Solution:
#     def minSubArrayLen(self, target: int, nums) -> int:
#         window_left = 0
#         window_right = 0
#         n = len(nums) - 1
#         subarr_len = []
#         while window_left <= n and window_right <= n:
#             if sum(nums[window_left:window_right+1]) < target:
#                 window_right += 1
#             elif sum(nums[window_left:window_right+1]) > target:
#                 window_left += 1
#             else:
#                 window_left += 1
#                 subarr_len.append(window_right+2-window_left)
#         if len(subarr_len):
#             return min(subarr_len)
#         else:
#             return 0

# sol = Solution()

s = "12ere2"
def getstr(s):
    hash_table = {}
    for ch in s:
        if ch in hash_table:
            hash_table[ch] += 1
        else:
            hash_table[ch] = 1
    result = ""
    for key in hash_table:
        result += key
    return result

print(getstr(s))