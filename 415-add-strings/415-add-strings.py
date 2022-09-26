class Solution:
    def addStrings(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry = 0
        res = ""
        while a or b or carry:
            if a:
                carry += ord(a.pop())-ord('0')
            if b:
                carry += ord(b.pop())-ord('0')
            res += str(carry % 10)
            carry = carry//10
        return res[::-1]