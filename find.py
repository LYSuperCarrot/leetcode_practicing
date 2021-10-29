import random
def linear_search(li, val):
    for ind, element in enumerate(li):
        if element == val:
            return ind
    return None

li = [x for x in range(10)]
random.shuffle(li)
print(li)
targ_ind = linear_search(li, 9)
print(targ_ind)