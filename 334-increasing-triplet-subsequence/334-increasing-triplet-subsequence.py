class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        res=[]
        for ele in nums:
            idx=bisect_left(res, ele)
            print(idx)
            if idx==len(res):
                res.append(ele)
                if len(res)==3:
                    return True
            else:
                res[idx]=ele
        return False