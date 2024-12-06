import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 10억

students, road, time = map(int, input().split())
graph = [[] for _ in range(students+1)]

for _ in range(road):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))
    return distance

# 다익스트라 실행
result = [[]]
cost_lst = []
for i in range(1, students + 1):
    distance = [INF] * (students + 1)
    result.append(dijkstra(i))
for i in range(1, students + 1):
    cost_lst.append(result[i][time] + result[time][i])
print(max(cost_lst))
