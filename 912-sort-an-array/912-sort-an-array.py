class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        def conquer(arr, left, right):
            i, j, k = 0, 0, 0
            inv = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                    inv += len(left)-i
                k += 1
            arr[k:] = left[i:] if i < len(left) else right[j:]

        def divide(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
                divide(left)
                divide(right)
                conquer(arr, left, right)
        divide(arr)
        return arr