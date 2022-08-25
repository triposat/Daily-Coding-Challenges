# Time: O(n)
# Space: O(1)
class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        low, mid, high = 0, 0, n-1
        while mid<=high:
            if arr[mid]==0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid+=1
                low+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high-=1
            