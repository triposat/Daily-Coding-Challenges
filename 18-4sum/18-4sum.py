# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         def binaryS(arr, ele):
#             l = 0
#             r = len(arr)-1
#             while l <= r:
#                 mid = (l+r) >> 1
#                 if arr[mid] == ele:
#                     return True
#                 elif arr[mid] > ele:
#                     r = mid-1
#                 else:
#                     l = mid+1
#             return False
#         nums.sort()
#         res = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     x = target-(nums[i]+nums[j]+nums[k])
#                     if binaryS(nums[k+1:], x):
#                         temp = [nums[i], nums[j], nums[k], x]
#                         temp.sort()
#                         res.append(temp)
        # new_res=[]
        # for arr in res:
        #     if arr not in new_res:
        #         new_res.append(arr)
        # return new_res

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x = target-nums[i]-nums[j]
                left = j+1
                right = len(nums)-1
                while left < right:
                    twoSum = nums[left]+nums[right]
                    if twoSum < x:
                        left += 1
                    elif twoSum > x:
                        right -= 1
                    else:
                        res = [nums[i], nums[j], nums[left], nums[right]]
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        while left < right and nums[left] == res[2]:
                            left += 1
                        while left < right and nums[right] == res[3]:
                            right -= 1
                while j+1 < n and nums[j+1] == nums[j]:
                    j += 1
            while i+1 < n and nums[i+1] == nums[i]:
                i += 1
        return list(ans)