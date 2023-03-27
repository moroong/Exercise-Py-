# 두 개의 정수를 사용자로부터 입력을 받아서
# 두 정수의 합과 두 정수의 곱을 출력

# 첫 번째 정수를 입력
first_value = int( input(' enter a first integer >>> ') )

# 두 번째 정수를 입력
second_value = int( input(' enter a second integer >>> ') )

sum_value = first_value + second_value
print(f'{first_value} + {second_value} = {sum_value}')

mul_value = first_value * second_value
print(f'{first_value} * {second_value} = {mul_value}')

first_value, second_value = 100, 500