# class Solution:
#     def clumsy(self, n: int) -> int:
#         stack=[n]
#         for i in range(1, n):
#             if i%4==1:
#                 stack.append(stack.pop()*(n-i))
#             elif i%4==2:
#                 stack.append(int(stack.pop()/(n-i)))
#             elif i%4==3:
#                 stack.append(n-i)
#             else:
#                 stack.append(-n+i)
#         return sum(stack)

class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n == 4:
            return 7
        if n % 4 == 0:
            return n+1
        if n % 4 == 1 or n % 4 == 2:
            return n+2
        if n % 4 == 3:
            return n-1