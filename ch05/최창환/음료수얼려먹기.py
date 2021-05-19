# n, m을 공백으로 구분해 입력
n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드를 방문한 뒤 연결된 모든 노드 방문
def dfs(x, y):
    # 범위 벗어나는 경우 함수 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False

    # 현재 노드를 방문하지 않았다면 방문 표시 후 인접 노드에 대해 재귀함수 호출
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1

        # 인접 노드 재귀 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    
    # 위의 if문을 pass 했을 경우 함수 종료
    return False

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 노드에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
