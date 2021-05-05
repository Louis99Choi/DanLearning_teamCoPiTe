import time

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())

result = 0 # 1을 빼거나 k로 나눈 횟수

start_time = time.time() # 측정 시작

while True:
    result += n % k # n을 k로 나눈 나머지는 1을 뺀 횟수이므로 그 만큼 증가.
    n //= k # n에 n을 k로 나눈 몫을 저장.

    if n >= 1 : result += 1 # 나눈 몫 n이 1이상일때, n을 k로 나눈 횟수 1 증가.
    
    if n <= 1: break # n이 1 이하면 반복문을 나감.

if n == 0 : result -= 1 #나눈 몫이 0일 경우, 'n이 1이 될때까지' 가 조건이므로 횟수 1감소.

print(result)

end_time = time.time() # 측정 종료
print("time :", end_time - start_time) # 수행 시간 출력


# 나눈 몫이, 0일 경우/ 1일 경우/ 2이상 k미만 일 경우/ k이상일 경우
