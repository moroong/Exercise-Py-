'''
# 사용자로부터 정수를 하나 입력받고
# 입력받은 정수가 양수이면 'positive number'를 출력
# 입력받은 정수가 음수이면 'negative number'를 출력
# 입력받은 정수가 0이면 'zero'를 출력

n1 = int(input(' 정수를 입력하세요 >>> '))
if n1 >= 1 :
    print('positive number')
elif n1 <= -1 :
    print('negative number')
else :
    print('zero')
'''
'''
# 사용자로부터 정수를 하나 입력받고
# 입력받은 정수가 짝수이면 'even number'를 출력
# 입력받은 정수가 홀수이면 'odd number'를 출력
# 입력받은 정수가 0이면 'zero'를 출력

n1 = int(input(' 정수를 입력하세요>>> '))

# case1
if n1 % 2 == 0 and n1 > 0 : 
    # n1 > 0 추가하여 n1 == 0 과 중복되지 않게 함
    print('even number')
elif n1 % 2 != 0 :
    print('odd number')
elif n1 == 0 :
    print('zero')
    
# case2
if n1 == 0 :
    print('zero')
elif n1 % 2 == 0 : # 0을 제외한 짝수가 출력
    print('even number')
elif n1 % 2 != 0 :
    print('odd number')
'''

# 사용자로부터 정수를 하나 입력받고
# 입력받은 정수가
#   3의 배수인 경우 : 'Fizz'
#   5의 배수인 경우 : 'Buzz'
#   3의 배수이면서 5의 배수인 경우 : FizzBuzz'
#   그 외인 경우 : 정수 값 

n1 = int(input(' 정수를 입력하세요>>> '))

# case1
if n1%3 == 0 and n1%5 != 0 :
    print('Fizz')
elif n1%3 != 0 and n1%5 == 0 :
    print('Buzz')
elif n1%3 == 0 and n1%5 == 0 :
    print('FizzBuzz')
else :
    print(f'{n1}')

# case2
if n1 % 3 == 0 and n1 % 5 == 0 :
    print('FizzBuzz')
elif n1 % 3 == 0 :
    print('Fizz')
elif n1 % 5 == 0 :
    print('Buzz')
else :
    print(n1)