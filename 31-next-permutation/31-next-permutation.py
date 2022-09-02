class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        if n <= 1:
            return
        j = n-2
        while j >= 0 and arr[j] >= arr[j+1]:
            j -= 1
        if j < 0:
            arr[:] = arr[::-1]
        else:
            i = n-1
            while arr[i] <= arr[j]:
                i -= 1
            arr[j], arr[i] = arr[i], arr[j]
            arr[j+1:] = sorted(arr[j+1:])