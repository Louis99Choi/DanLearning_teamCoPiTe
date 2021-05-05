#4-1 상하좌우

N = int(input())
move = input()
move.split()

x = 1
y = 1

for i in range(len(move)):
    if move[i] == 'R':
        if x == 5:
            continue
        x += 1
    elif move[i] == 'L':
        if x == 1:
            continue
        x -= 1
    elif move[i] == 'U':
        if y == 1:
            continue
        y -= 1
    elif move[i] == 'D':
        if y == 5:
            continue
        y += 1
print('%d %d' %(y, x))
