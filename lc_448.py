def findDisappearedNumbers(nums):
    # method1
    # li = [i for i in range(1, len(nums)+1)]
    # return list(set(li) - set(nums))
    
    # method2
    # i, j = 0, 0
    # temp_pre = nums[0]
    # temp_cur = nums[0]
    # while j < len(nums):
    #     if nums[j]-1 != j:
    #         i = j
    #         while nums[i]-1 != i:
    #             temp_cur = nums[i]
    #             nums[i] = temp_pre
    #             i = temp_cur-1
    #             temp_pre = temp_cur
    #     j += 1

    # output = []
    # for i in range(len(nums)):
    #     if nums[i]-1 != i:
    #         output.append(i+1)
    # return output

    # method3 
    for i in range(len(nums)):
        nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i+1)
    return res

nums = [4,3,2,7,8,2,3,1]

print(findDisappearedNumbers(nums))