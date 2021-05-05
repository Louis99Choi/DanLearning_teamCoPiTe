import time

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())

result = 0 # 1을 빼거나 k로 나눈 횟수

start_time = time.time() # 측정 시작

while True:
    # (N == K로 나누어 떨어지는 수) 가 될때까지 1씩 빼기
    target = (n //k) * k
    result += (n - target)
    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출.
    if n < k: break

    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대해 1씩 빼기
result += (n-1)
print(result)

end_time = time.time() # 측정 종료
print("time :", end_time - start_time) # 수행 시간 출력
