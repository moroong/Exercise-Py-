# 사용자로부터 두 자리 정수(10~99)를 입력 받아 
# 십의 자리와 일의 자리를 각각 출력하는 프로그램을 작성

value = int(input(' 두 자리 정수(10~99)를 입력하세요>>> '))

# 십의 자리 = 두 번째 자리 숫자
second_digit = value // 10
first_digit = value % 10

print(f'십의 자리 = {second_digit}')
print(f'일의 자리 = {first_digit}')