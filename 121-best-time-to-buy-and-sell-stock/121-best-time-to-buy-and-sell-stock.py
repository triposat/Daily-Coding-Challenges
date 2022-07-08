# Time: O(n^2)
# Space: O(1)
# Time Limit Exceeded 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    maxSoFar = max(maxSoFar, prices[j]-prices[i])
        return maxSoFar
    
# Kadane's Algo
# Time: O(n), Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxCur = 0
        maxSo = 0
        for i in range(1, len(prices)):
            maxCur += prices[i]-prices[i-1]
            if maxCur < 0:
                maxCur = 0
            maxSo = max(maxSo, maxCur)
        return maxSo