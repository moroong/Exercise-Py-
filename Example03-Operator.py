# 사용자로부터 정수를 입력받아 3의 배수인지 출력하는 프로그램 작성

value = int(input('정수를 입력하세요 >>>'))

# 3의 배수 = 3으로 나눴을 때 나머지가 0 인 수
is_multiple = (value % 3) == 0

# 3의 배수가 아닌 경우
# 3으로 나눴을 때 나머지가 0이 아닌 수
is_not_multiple = value % 3 !=0

print(f'Is {value} multiple of 3 : {is_multiple}')