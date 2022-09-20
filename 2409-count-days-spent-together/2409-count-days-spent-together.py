class Solution:
    def countDaysTogether(self, arAl: str, lAl: str, arBo: str, lBo: str) -> int:
        months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        start = max(arAl, arBo)
        end = min(lAl, lBo)

        startDay = int(start[3:])
        startMonth = int(start[:2])
        endDay = int(end[3:])
        endMonth = int(end[:2])
        
        if start > end:
            return 0
        if startMonth == endMonth:
            return endDay-startDay+1
        elif startMonth < endMonth:
            return months[startMonth]-startDay + endDay + 1 + sum(months[m] for m in range(startMonth+1, endMonth))
