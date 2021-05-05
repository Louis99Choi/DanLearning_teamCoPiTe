#숫자 카드 게임
N, M = input().split()
print('%d %d' %(int(N), int(M)))

matrix = []
for j in range(int(N)):
    matrix.append(list(map(int, input().split())))

min_list = []
for k in range(int(N)):
    min_list.append(min(matrix[k]))
print(max(min_list))
