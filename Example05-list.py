# 리스트 내에 저장된 정수들 중에서 연속으로 저장된 중복된 값을
# 제거한 리스트를 생성하는 프로그램을 작성
# [1, 1, 3, 3, 0, 0, 1, 1]
#  → [1, 3, 0, 1]

list1 = [1, 1, 3, 3, 0, 0, 1, 1]


'''
result = []
result.append(list1[0])

# 두번째 요소부터 순차 탐색하여
for i in range(1, len(list1)) :
    # 이전 요소랑 다른 값이면 리스트에 저장
    if list1[i-1] != list1[i] :
        result.append(list1[i])
        '''

result = []
result.append(list1[0])

# 기존 리스트 result에 리스트 내포에 의해 만들어진 리스트를 추가
result.extend( [list1[1] for i in range(1, len(list1)) if list1[i-1] != list1[i]] )
print(f'{list1} > {result}')
