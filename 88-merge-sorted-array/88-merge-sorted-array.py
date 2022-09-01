class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if arr1[i] < arr2[j]:
                arr1[k] = arr2[j]
                j -= 1
            else:
                arr1[k] = arr1[i]
                i -= 1
            k -= 1
        while j >= 0:
            arr1[k] = arr2[j]
            k -= 1
            j -= 1
