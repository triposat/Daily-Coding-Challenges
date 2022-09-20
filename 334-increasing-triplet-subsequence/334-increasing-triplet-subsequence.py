class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, big =(1<<31), (1<<31)
        for ele in nums:
            if ele<=small:
                small=ele
            elif ele<=big:
                big=ele
            else:
                return True
        return False