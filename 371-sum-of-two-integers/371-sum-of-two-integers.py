class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffffff
        while b&mask:
            sum_=(a^b)
            carry=((a&b)<<1)
            a=sum_
            b=carry
        return a&mask if b>0 else a