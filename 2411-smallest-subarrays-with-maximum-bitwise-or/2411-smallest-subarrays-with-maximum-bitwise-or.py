class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = defaultdict(deque)
        for i in range(len(nums)):
            for bit in range(31):
                if nums[i] & (1 << bit):
                    ans[bit].append(i)
        res = []
        for i in range(len(nums)):
            end = i
            for idx, arr in ans.items():
                if arr and i > arr[0]:
                    arr.popleft()
                if arr:
                    end = max(end, arr[0])
            res.append(end-i+1)
        return res