node = int(input())         # 컴퓨터 개수
edge = int(input())         # 연결선 개수
graph = [[] for i in range(node+1)]     # 그래프 초기화
visited=[0] * (node+1)      # 방문한 표시
for i in range(edge):       # 그래프 생성
    a, b = map(int,input().split())
    graph[a] += [b]         # a에 b 연결
    graph[b] += [a]         # b에 a 연결 (index가 컴퓨터 번호, value는 연결된 컴퓨터 리스트)
def dfs(num):
    visited[num] = 1          # 방문 표시
    for i in graph[num]:      # graph[num]은 num번 컴퓨터에 연결된 컴퓨터의 리스트
        if visited[i] == 0:
            dfs(i)
dfs(1)
print(sum(visited)-1)         # 1번 컴퓨터를 제외하고, 1번 컴퓨터와 연결된 컴퓨터의 개수를 출력
