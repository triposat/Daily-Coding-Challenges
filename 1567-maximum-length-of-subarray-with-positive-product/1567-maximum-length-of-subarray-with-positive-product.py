class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        mx=0
        i=0
        # j=0
        while i<len(nums):
            negS=-1
            negE=-1
            p=0
            n=0
            j=i
            while j<len(nums):
            # for j in range(i, len(nums)):
                if nums[j]>0:
                    p+=1
                if nums[j]<0:
                    n+=1
                    negE=j
                if nums[j]<0 and negS==-1:
                    negS=j
                if nums[j]==0:
                    break
                j+=1
            if not n&1:
                mx=max(mx, n+p)
            if n&1:
                mx=max(mx, j-negS-1)
                mx=max(mx, negE-i)
            i=j+1
        return mx
    