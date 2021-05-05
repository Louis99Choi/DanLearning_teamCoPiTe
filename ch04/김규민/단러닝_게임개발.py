
n, m = map(int, input('입력').split())

a, b, d = map(int, input('a, b, d입력 ').split())


went = [[0] * m for _ in range(n)] #한번이라도 가 본  적이 있다면 #1 -> 가본 것, 0-> 아직 안 가본 것
ground = [[0] * m for _ in range(n)] #육지, 바다

for i in range(n): #0~ n-1
    ground[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy  =[0, 1, 0, -1]

#북 동 남 서
#0 1 2 3

def left(d):
    if(d == 0):
        return 3
    else:
        return d-1
count = 1
went[a][b] = 1
#=========
while(True):
    newd = left(d)
    newA = a + dx[newd]
    newB = b + dy[newd]
    print(newA, newB)
    '''
    if(newA > m and newB > n):
        break
    '''
    if(newd = d):
        newA = a - dx[newd]
        newB = b - dy[newd]
        if (ground[newA][newB] == 1):  # 만약 뒤가 바다라면
            break  # while반복문 빠져나옴
        else:
            a = newA
            b = newB
        
    if(ground[newA][newB] == 0 and went[newA][newB] == 0): #한번도 안 가고, 육지라면
        a = newA
        b = newB
        went[a][b] = 1
        count = count + 1
        continue
    else:  # 바다거나, 이미가 본 적이 있다면
        turn += 1
        
print(count)

#count += 1




