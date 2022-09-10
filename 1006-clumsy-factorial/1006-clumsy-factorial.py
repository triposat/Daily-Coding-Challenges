class Solution:
    def clumsy(self, n: int) -> int:
        stack=[n]
        for i in range(1, n):
            if i%4==1:
                stack.append(stack.pop()*(n-i))
            elif i%4==2:
                stack.append(int(stack.pop()/(n-i)))
            elif i%4==3:
                stack.append(n-i)
            else:
                stack.append(-n+i)
        return sum(stack)