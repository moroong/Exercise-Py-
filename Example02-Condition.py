'''
# 사용자로부터 양수를 입력받아 출력하는 프로그램을 작성
# 만약 사용자가 음수를 입력한 경우, 0 으로 출력하도록 작성

# 사용자로부터 숫자를 입력
value = int(input('양수를 입력하세요 >>>'))

# 입력된 값이 음수인 경우 0을 저장
if value < 0 :
    value = 0

print(f'value = {value}')
'''
'''
# 사용자로부터 두 개의 정수를 입력받고
# 두 정수의 차이를 절대 값으로 출력

value1, value2 = map( int, input( ' 두 개의 정수를 입력하세요 >>> ' ).split() )

if value1 > value2 :
    print(f'|{value1} - {value2}| = {value1-value2}')
else :
    print(f'|{value1} - {value2}| = {value2}-{value1}')

# 두 수의 차이
absolute = value1 - value2

if absolute < 0 :
    absolute = -absolute
    # absolute = -(-5) = 5

print(f'|{value1} - {value2}| = {absolute}') 
'''

# 사용자로부터 두 개의 정수를 입력 받아서
# 큰 수와 작은 수를 각각 출력하는 프로그램 작성

n1, n2 = map(int, input(' 두 개의 정수를 입력하세요>>> ').split())

if n1 > n2 :
    print(f'큰 수는 {n1}, 작은 수는 {n2}입니다.')
else :
    print(f'큰 수는 {n2}, 작은 수는 {n1} 입니다')
