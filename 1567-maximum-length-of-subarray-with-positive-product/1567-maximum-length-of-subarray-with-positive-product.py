# Sliding window approach
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        mx = 0
        n = len(nums)
        i = 0
        while i < n:
            negS = -1  # It will store the index of first negative number
            negE = -1  # It will store the last index of negative number
            pos = 0
            neg = 0
            j = i
            while j < n:
                if nums[j] > 0:
                    pos += 1
                elif nums[j] < 0:
                    neg += 1
                    negE = j
                if nums[j] < 0 and negS == -1:
                    negS = j
                elif nums[j] == 0:  # End the subrray, because after that all the product will be 0
                    break
                j += 1
            if not neg & 1:  # If negative numbers are even
                mx = max(mx, neg+pos)
            else:
                mx = max(mx, j-negS-1)  # Ignore the first negative number
                mx = max(mx, negE-i)  # Ingnore the last negative number
            i = j+1  # Now, start from the new subarray
        return mx
