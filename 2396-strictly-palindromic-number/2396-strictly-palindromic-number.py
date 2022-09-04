class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def hey(n, b):
            if n ==0:
                return [0]
            ans=[]
            while n:
                ans.append(int(n%b))
                n//=b
            return ans

        for i in range(2, n-1):
            bina = str(hey(n, i))
            if bina!=bina[::-1]:
                return False
        return True