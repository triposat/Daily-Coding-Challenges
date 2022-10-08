# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         n = len(nums)
#         ans = set()
#         for i in range(n):
#             l = i+1
#             r = n-1
#             temp = -1*nums[i]
#             while l < r:
#                 add = nums[l]+nums[r]
#                 if add < temp:
#                     l += 1
#                 elif add > temp:
#                     r -= 1
#                 else:
#                     ans.add((nums[i], nums[l], nums[r]))
#                     l += 1
#                     r -= 1
#         return ans


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n<3:
            return []
        nums.sort()
        ans = []
        for i in range(n-2):
            if i == 0 or nums[i] != nums[i-1]:
                l = i+1
                r = n-1
                while l < r:
                    add = nums[i]+nums[l]+nums[r]
                    if add < 0:
                        l += 1
                    elif add > 0:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return ans