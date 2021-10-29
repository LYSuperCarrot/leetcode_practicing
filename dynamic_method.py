# 斐波那契数列：Fn = Fn-1 + Fn-2
# F1 = 1, F2 = 1

def fibnacci(n):
    if n == 1 and n == 2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)

def fibnacci_no_rec(n):
    li = [0, 1, 1]
    if n > 2:
        for i in range(n-2):
            num = li[-1] + li[-2]
            li.append(num)
    return li[n]


# 钢条切割问题
p = [0,1,5,8,9,10,17,17,20,24,30]
def cut_rod_recurision_1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(n):
            res = max(res, cut_rod_recurision_1(p, i) + cut_rod_recurision_1(p, n-i))
    return res

def cut_rod_recurision_2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n+1):
            res = max(res + cut_rod_recurision_2(p, n-i))
    return res

def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res, p[j] + r[i-j])
            r.append(res)
    return r[n]


        


