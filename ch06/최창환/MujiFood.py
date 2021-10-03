from operator import itemgetter

food_times = list(map(int, input("각 번호의 음식 수를 공백 단위로 입력 : ").split()))
k = int(input("네트워크 장애 발생 시각(초) 입력 : "))

def solution(food_times, k) :
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1))

    foods.sort()

    pretime = 0

    for i, food in enumerate(foods):
        diff = food[0] - pretime
        if diff != 0 :
            spend = diff * n

            if spend <= k:
                k-= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(food[i:], key = itemgetter(1))
                return sublist[k][1]

        n -= 1

    return -1

print(solution(food_times, k))

