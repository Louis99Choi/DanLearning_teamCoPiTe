from collections import deque

#도시개수, 도로개수, 거리정보, 출발도시번호
n, m, k, x = map(int, input().split())

#village list 생성
village = [[] for _ in range(n+1)]
for i in range(m):
    #a, b 주어짐 -> a에서 b로 이동하는 단방향 도로가 존재한다
    a, b = map(int, input().split())
    village[a].append(b)

went = [-1 for _ in range(n+1)] #-1 -> 가지 않음 

#가지 않은 장소를 가는데(went=-1인 곳을 간다),
#went의 정보를 새롭게 정의한다 -> -1인 곳만 가니까 굳이 0또는 -1이 아니어도 됨 
#큐가 비게 되면 went리스트를 반환한다

def find(n): #출발도시번호 n, 최대거리 p #p는 사용하지 않는다 
    queue = deque()
    queue.append(n)
    went[n] = 0 #(처음 위치) 갔다는 것을 표현
    while queue: #queue가 비지 않을 동안
        vNum = queue.popleft() #queue에서 가장 먼저 들어간 값 꺼내
        for i in village[vNum]:
            if went[i] == -1: # and i > 0: #가지 않았다면, 값을 가진다면 (마을 1~)
                went[i] = went[vNum] + 1
                queue.append(i)
    #return went

find(x)

for i in range(n+1):
    if went[i] == k:
        print(i)
if k not in went: #went 리스트에 k가 없다면 -1 반환 
    print(-1)

