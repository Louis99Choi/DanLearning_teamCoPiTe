#4-2 시각

N = int(input())

time = None
cnt = 0
for h in range(0, N+1):
    for m in range(0, 60):
        for s in range(0, 60):
            time = str(h) + str(m) + str(s)
            if time.find('3') != -1:
                cnt += 1
print(cnt)
