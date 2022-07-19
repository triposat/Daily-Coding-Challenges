class Solution:
    def __init__(self):
        self.cnt = 0

    def reversePairs(self, arr: List[int]) -> int:
        def merge(left, right):
            res = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    res.append(right[j])
                    j += 1
                else:
                    res.append(left[i])
                    i += 1
            res.extend(left[i:] or right[j:])
            return res

        def divide(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2
            left = divide(arr[:mid])
            right = divide(arr[mid:])
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] > 2*right[j]:
                    self.cnt += len(left)-i
                    j += 1
                else:
                    i += 1
            return merge(left, right)
        divide(arr)
        return self.cnt