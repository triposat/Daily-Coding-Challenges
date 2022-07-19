class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = nums[:]
        res = []
        nums.sort()
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i]+nums[j] == target:
                one = nums[i]
                two = nums[j]
                break
            elif nums[i]+nums[j] > target:
                j -= 1
            else:
                i += 1

        for i in range(len(arr)):
            if arr[i] == one:
                res.append(i)
            elif arr[i] == two:
                res.append(i)
        return res