class Solution:
    def smallestRangeII(self, arr: List[int], k: int) -> int:
            arr.sort()
            maxo = arr[-1]
            mino = arr[0]
            out = maxo-mino
            for i in range(1, len(arr)):
                maxo = max(arr[i-1]+k, arr[-1]-k)
                mino = min(arr[i]-k, arr[0]+k)
                out = min(out, maxo-mino)
            return out