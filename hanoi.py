
# 一共有n个盘子，有abc三根柱子
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" %(a, c))
        hanoi(n-1, b, a, c)

hanoi(3, "A", "B", "C")