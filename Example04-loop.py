# 구구단 2단부터 9단까지 출력
MAX_NUM = 9
MAX_I = 9

for num in range(2,MAX_NUM+ 1) :
    print(f'{num}단')
    for i in range(1, MAX_I +1) :
        print(f'{num} * {i}={num*i}')
    print('-' * 10)