#1이 될 때까지
import math

N, K = map(int, input().split())

i = 0
while True:
    if math.pow(K, i) <= N < math.pow(K, i + 1):
        break
    i += 1

result = N - math.pow(K, i) + i
print(int(result))
