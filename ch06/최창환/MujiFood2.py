from queue import PriorityQueue

food_times = list(map(int, input("각 번호의 음식 수를 공백 단위로 입력 : ").split()))
k = int(input("네트워크 장애 발생 시각(초) 입력 : "))

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    q = PriorityQueue()
    for i in range(len(food_times)):
        q.put((food_times[i], i + 1))
    sum_value = 0
    previous = 0
    length = len(food_times)
    
    while sum_value + ((q.queue[0][0] - previous) * length) <= k:
        now = q.get()[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    # 남은 음식 중에서 몇 번째 음식인지 확인
    target = k - sum_value + 1
    length = len(q.queue)
    temp = (target - 1) // length
    result = sorted(q.queue, key=lambda x: x[1])
    target -= temp * length

    return result[target - 1][1]

