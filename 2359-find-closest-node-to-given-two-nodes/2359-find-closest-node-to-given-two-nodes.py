class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start):
            n = len(edges)
            dist = [-1]*n
            q = [(start, 0)]
            seen = set([start])
            while q:
                ele, dis = q.pop(0)
                dist[ele] = dis
                newDis = dis+1
                if edges[ele] != -1 and edges[ele] not in seen:
                    q.append((edges[ele], newDis))
                    seen.add(edges[ele])
            return dist
        dist1 = bfs(node1)
        dist2 = bfs(node2)
        minDis = 1e9
        ans = -1
        for i in range(len(edges)):
            if min(dist1[i], dist2[i]) >= 0 and max(dist1[i], dist2[i]) < minDis:
                minDis = max(dist1[i], dist2[i])
                ans = i
        return ans