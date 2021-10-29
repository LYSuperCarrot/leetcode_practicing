# 设上店老板需要找零n元钱，钱币面额有：100,50,5,1，如何找零使得所需钱币的数量最少
# 先找面额最大的，找不开再找下一面额
from functools import cmp_to_key

t = [100, 50, 5, 1]
def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n

# print(change(t, 531))

# 背包问题
# 一个小偷在商店里发现有n个商品，第i个商品价值vi元，重wi千克
# 他希望拿走的价值尽量高，但是他的背包最多只能容纳W千克的东西。他应该拿走那些商品。
goods = [(60, 10),(100, 20),(120, 30)]	# 表示每个商品元组表示（价格， 重量）
goods.sort(key=lambda x: x[0]/x[1], reverse=True)	# 按照平均价格降序排序

def fractional_backpack(goods, w):
    total_v = 0
    m = [0 for _ in range(len(goods))]
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
            total_v += weight
        else:
            m[i] = w / weight
            total_v += m[i] * prize
            w = 0
            break
    return m, total_v


li = [32, 94, 128, 1286, 6, 71]
def xy_cmp(x, y):
	if x+y < y+x:
		return 1
	elif x+y > y+x:
		return -1
	else:
		return 0
def number_join(li):
	li = list(map(str, li))
	li.sort(key=cmp_to_key(xy_cmp))
	return "".join(li)

activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]
# 按活动结束时间排好序
activities.sort(key=lambda x:x[1])

def activity_selection(a):
	res = [a[0]]
	for i in range(1, len(a)):
		if a[i][0] >= res[-1][1]:	# 当前活动时间大于等于最后一个入选活动的结束时间
			# 时间不冲突
			res.append(a[i])
	return res


	


