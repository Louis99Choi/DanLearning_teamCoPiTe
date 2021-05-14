n, m = map(int, input('입력').split())
a, b, d = map(int, input('a, b, d입력 ').split())

went = [[0] * m for _ in range(n)]  # 한번이라도 가 본  적이 있다면 #1 -> 가본 것, 0-> 아직 안 가본 것
ground = [[0] * m for _ in range(n)]  # 육지, 바다

for i in range(n):  # 0~ n-1
    ground[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 북 동 남 서
# 0 1 2 3

def left(d):
    if d == 0:
        return 3
    else:
        return d - 1
went[a][b] = 1
value = 1 #방문한 칸의 수 
dlist = [-1] * 5
dlist[0] = d
i = 1
#=====
while(True):
    dlist[i] = left(dlist[i-1])
    newA = a + dx[dlist[i]]
    newB = b + dy[dlist[i]]
    i = i + 1
    if (ground[newA][newB] == 0 and went[newA][newB] == 0):
        a = newA
        b = newB
        value = value + 1
        went[a][b] = 1

        dlist[0] = dlist[i]
        i = 1
        continue
    
    if dlist[i-1] == dlist[0]:
        newA = a - dx[d]
        newB = b - dy[d]
        
        if ground[newA][newB] == 1:  # 만약 뒤가 바다라면
            break  # while반복문 빠져나옴
        else:
            a = newA
            b = newB
            
            dlist[0] = dlist[i-1]
            i = 1
    
     
print(value)
