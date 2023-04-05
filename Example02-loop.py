# 사용자가 입력한 양수들을 리스트에 저장하는 프로그램을 작성
# 사용자가 0 을 입력할 때 까지 정수를 입력 받고
# 양수이면 리스트에 저장 한다.

numbers = list[]

# 사용자가 0 을 입력할 때 까지 반복

while True:
# 입력
     n = int( input('Enter an integer >>> '))
# 검사
     if n == 0 : break
     if n < 0 : continue
    #  검사 단계에서 모두 false 이면
    # 입력된 값은 연산하기에 유효한 값이다

    # 처리
numbers.append(n)
print(f'numbers = {numbers}')
