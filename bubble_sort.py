import random

def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


def bubble_sort_change(li):
    exchanged = False
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchanged = True
        
        if exchanged == False:
            return


li = [x for x in range(10)]
random.shuffle(li)
print(li)
bubble_sort(li)
print(li)