import random
import heapq

# li = list(range(10))
# random.shuffle(li)
# heapq.heapify(li)
# heapq.heappop(li)
# print(li)

# 父节点和子节点：i -> 2*i+1, 2*i+2
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    # tmp = li[low]
    while j <= high:
        if j+1 <= high and li[j+1] < li[j]:
            j = j + 1
        if li[j] < li[i]:
            li[i], li[j] = li[j], li[i]
            i = j
            j = 2 * i + 1
        else:
            break

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        sift(li, i, n-1)
    
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)

def topk(li, k):
    heap = li[0:k]
    # 建堆
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    
    # 遍历
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    
    # 出数
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    
    return heap



# topk    
li = [x for x in range(10)]
random.shuffle(li)
print(li)
heap = topk(li, 5)
print(heap)


# 堆排序
# li = [x for x in range(10)]
# random.shuffle(li)
# print(li)
# heap_sort(li)
# print(li)