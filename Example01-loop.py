# 사용자로부터 자연수 n1 을 입력 받고
# 1 부터 n1 까지의 정수를 모두 출력하는 while문을 작성

'''
n1 = int(input('정수를 입력하세요>>>'))

num = 1

while num <= n1 :
    print(f'num={num}')
    num += 1
'''

# 사용자로부터 자연수 M과 N을 입력을 받고
# M 부터 N 까지의 모든 정수를 출력하는 while 문을 작성
#  입력 시 : N > M

M, N = map(int, input('정수 2개를 입력하세요>>>').split() )

num = M

while num <= N :
    print(f'num={num}')
    num += 1

# 사용자로부터 자연수 n1 을 입력을 받아 1 부터 n1 까지 출력
# 만약 사용자가 음수를 입력한 경우 자연수 입력받도록 해야한다.

n1 = int(input(' 자연수를 입력하세요 >>> '))


while n1 < 0 :
    print('The value entered is not positive number.')
    n1 = int( input('자연수를 입력하세요 >>> '))

# 1 부터 입력받은 n1 까지의 모든 정수를 출력
num = 1 # 1 부터 n1 까지의 정수를 출력할 변수

# num의 값이 n1이 될 때 까지 
while num <= n1 :
    print(f'num={num}')
    num += 1
    