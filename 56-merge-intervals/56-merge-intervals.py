class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans=[]
        for inter in intervals:
            if not ans or ans[-1][-1]<inter[0]:
                ans.append(inter)
            else:
                ans[-1][-1]=max(ans[-1][-1], inter[1])
        return ans