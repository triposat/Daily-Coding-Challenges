class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def bise(arr, q):
            st=0
            end=len(arr)
            while st<end:
                mid=(st+end)>>1
                if arr[mid]==q:
                    return mid+1
                elif arr[mid]<q:
                    st=mid+1
                else:
                    end=mid
            return st
        nums.sort()
        for i in range(1, len(nums)):
            nums[i]=nums[i-1]+nums[i]
        return [bise(nums, q) for q in queries]