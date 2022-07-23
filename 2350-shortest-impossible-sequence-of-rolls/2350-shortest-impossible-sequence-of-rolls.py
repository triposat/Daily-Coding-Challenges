class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        s = set()
        hey = 0

        for r in rolls:
            s.add(r)
            if len(s) == k:        # All possible number has appeared once.
                # So you must "at least" use one more place to store it.
                hey += 1
                s.clear()          # Clear the set.

        return hey + 1
