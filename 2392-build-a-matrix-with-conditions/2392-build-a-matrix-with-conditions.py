class Solution:
    def buildMatrix(self, k: int, row: List[List[int]], col: List[List[int]]) -> List[List[int]]:
        def topoSort(adj):
            indeg = [0]*k
            for node in range(k):
                for ele in adj[node]:
                    indeg[ele] += 1
            que = []
            for i in range(k):
                if indeg[i] == 0:
                    que.append(i)

            ans = []
            while que:
                curr = que.pop(0)
                ans.append(curr)
                for neigh in adj[curr]:
                    indeg[neigh] -= 1
                    if indeg[neigh] == 0:
                        que.append(neigh)
            return ans if len(ans) == k else []

        # Making Adj list
        above = [[] for _ in range(k)]
        for i, j in row:
            above[i-1].append(j-1)

        left = [[] for _ in range(k)]
        for i, j in col:
            left[i-1].append(j-1)

        aboveOrd, leftOrd = topoSort(above), topoSort(left)
        if not aboveOrd or not leftOrd:
            return []
        mat = [[0]*k for i in range(k)]
        for i in range(k):
            mat[aboveOrd.index(i)][leftOrd.index(i)] = i+1
        return mat