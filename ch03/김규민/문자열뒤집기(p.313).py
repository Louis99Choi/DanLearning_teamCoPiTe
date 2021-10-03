import time

s = input("0또는1로 이루어진 문자열 입력: ")
now = time.time()
n = s[0]
cnt = 0
number = []
number.append(n)
for i in s:
    if(i != n):
        cnt += 1
        number.append(i)
    n = i
    cnt = cnt + 1
now2 = time.time()
print(now2 - now)
print(min(number.count('1'), number.count('0')))
