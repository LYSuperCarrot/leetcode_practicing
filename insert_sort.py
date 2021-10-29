import random

def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        while j >= 0:
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1],li[j]
                j -= 1
            else:
                break

li = [x for x in range(10)]
random.shuffle(li)
print(li)
insert_sort(li)
print(li)