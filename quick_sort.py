import random

def partation(li, left, right):
    pivot = li[left]
    while left < right:
        while left < right and li[right] > pivot:
            right -= 1
        li[left] = li[right]

        while left < right and li[left] < pivot:
            left += 1
        li[right] = li[left]
    li[left] = pivot
    return left

def _quick_sort(li, left, right):
    if left < right:
        mid = partation(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)

def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)
        



li = [x for x in range(10)]
random.shuffle(li)
print(li)
quick_sort(li)
print(li)