class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        left = mat[0][0]
        right = mat[-1][-1]
        ans = -1

        def countLE(mid):
            col = len(mat[0])-1
            cnt = 0
            for row in range(len(mat)):
                while col >= 0 and mat[row][col] > mid:
                    col -= 1
                cnt += (col+1)
            return cnt

        while left <= right:
            mid = (left+right) >> 1
            if countLE(mid) >= k:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans