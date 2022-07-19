class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        m=len(matrix[0])
        n=len(matrix)
        high=(m*n)-1
        while low<=high:
            mid = (low+high)>>1
            if matrix[mid//m][mid%m]==target:
                return True
            elif matrix[mid//m][mid%m]<target:
                low = mid+1
            else:
                high = mid-1
        