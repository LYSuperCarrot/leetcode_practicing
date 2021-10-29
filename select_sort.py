import random

def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i,len(li)):
            if li[j] <= li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

li = [x for x in range(10)]
random.shuffle(li)
print(li)
select_sort(li)
print(li)
        
