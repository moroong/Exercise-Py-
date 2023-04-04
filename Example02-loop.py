# 사용자로부터 자연수 N을 입력받고
# 1 부터 N 까지의 정수를 모두 출력하는 for 문을 작성
'''
N = int(input('정수를 입력하세요>>>'))

for num in range(1, N+1) :
    print(f'num={num}')
'''


# 사용자로부터 자연수 N을 입력받고
# 1부터 N 까지의 정수 중 3의 배수를 모두 출력하는 for 문을 작성
'''
N = int(input(' 정수를 입력하세요>>> '))

for num in range(1, N+1) :
    # num의 값이 3의 배수이면 출력
    if num % 3 == 0 :
        print(f'num = {num}')
'''


# 배열 numbers에서 5 보다 큰 요소들을 출력
'''
numbers = [10, 9, 6, 5, 7, 9, 1, 3, 6, 10]

for num in numbers :
    if num > 5 :
        print(f'num={num}')
'''

# 배열 numbers에서 3의 배수인 요소들을 인덱스와 같이 출력하는 for 문을 작성
numbers = [10, 9, 6, 5, 7, 9, 1, 3, 6, 10]

# 리스트 numbers의 인덱스의 범위만큼 반복
# 인덱스의 범위 : 0 <= index < 요소의 갯수
for i in range(len(numbers)) :
    # i 번째 요소가 3의 배수인지
    if numbers[i] % 3 == 0 :
        print(f'numbers[{i}] = {numbers[i]}')




