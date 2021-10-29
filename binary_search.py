def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left < right:
        mid = (left + right) // 2
        if li[mid] > val:
            right = mid - 1
        elif li[mid] < val:
            left = mid + 1
        else:
            return mid
    else:
        return None

li = [x for x in range(100)]
print(li)
ind = binary_search(li, 9)
print(ind)

