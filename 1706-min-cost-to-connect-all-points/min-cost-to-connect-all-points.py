class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n

        min_dist[0] = 0
        cost = 0

        for _ in range(n):
            u = -1

            for i in range(n):
                if not visited[i] and (
                    u == -1 or min_dist[i] < min_dist[u]
                ):
                    u = i

            visited[u] = True
            cost += min_dist[u]

            for v in range(n):
                if not visited[v]:
                    distance = (
                        abs(points[u][0] - points[v][0])
                        + abs(points[u][1] - points[v][1])
                    )

                    min_dist[v] = min(min_dist[v], distance)

        return cost
        