# p.359
# 국영수

# print("학생수를 입력하시오 : ") # 학생수 (1 <= n <= 100,000)
# n = int(input())

# gradeInfo = [[0] * 4 for _ in range(n)]

# for i in range(n) :
#     gradeInfo[i] = list(map(input().split()))

# for i in range(len(gradeInfo)) :
#     min_index = i # 가장 작은 원소의 인덱스
    
#     for j in range(i + 1, len(gradeInfo)) :
#         if gradeInfo[min_index] > gradeInfo

n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력 받기
for _ in range(n):
    students.append(input().split())
    print(students)

# '''
# [ 정렬 기준 ]
# 1) 두 번째 원소를 기준으로 내림차순 정렬
# 2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
# 3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
# 4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
# '''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])
