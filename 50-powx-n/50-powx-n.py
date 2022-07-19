class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        ans = 1
        while m:
            if m & 1:
                ans *= x
                m -= 1
            else:
                x *= x
                m //= 2
        if n < 0:
            ans = 1/ans
        return ans