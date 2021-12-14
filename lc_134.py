class Solution:
    def canCompleteCircuit(self, gas, cost):
        diff = [0] * len(gas)
        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
        if len(diff) == 1 and diff[0] >= 0:
            return 0
        if sum(diff) < 0:
            return -1
        for i in range(len(diff)):
            if diff[i] > 0:
                sum_gas = 0
                for j in range(i, i+len(diff)):
                    if sum_gas < 0:
                        break
                    else:
                        sum_gas += diff[j%len(diff)]
                if sum_gas >= 0:
                    return i
        return -1