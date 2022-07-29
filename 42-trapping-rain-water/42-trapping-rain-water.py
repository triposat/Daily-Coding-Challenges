# Most Optimal Solution
# Time: O(n)
# Space: O(1)

class Solution:
    def trap(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n-1
        leftbar = arr[0]
        rightbar = arr[n-1]
        ans = 0
        while left < right:
            if leftbar < rightbar:
                if arr[left] > leftbar:
                    leftbar = arr[left]
                else:
                    ans += leftbar-arr[left]
                    left += 1
            else:
                if arr[right] > rightbar:
                    rightbar = arr[right]
                else:
                    ans += rightbar-arr[right]
                    right -= 1
        return ans