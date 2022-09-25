# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         n = len(gas)
#         for i in range(len(gas)):
#             j = i
#             fuel = 0
#             cnt = 0
#             while cnt < len(cost):
#                 fuel += gas[j % n]-cost[j % n]
#                 if fuel < 0:
#                     break
#                 j += 1
#                 cnt += 1
#             if cnt == n and fuel >= 0:
#                 return i
#         return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        fuel = 0
        start=0
        if sum(gas) < sum(cost):
            return -1
        for i in range(n):
            fuel += gas[i]-cost[i]
            if fuel < 0:
                start = i+1
                fuel = 0
        return start