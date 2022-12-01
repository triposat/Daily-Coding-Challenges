class Solution:
    def findMinDiff(self, arr, n, m):
        ans=float("inf")
        arr.sort()
        for i in range(n-m+1):
            min=arr[i]
            maxi=arr[i+m-1]
            gap=maxi-min
            if gap<ans:
                ans=gap
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends