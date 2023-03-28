# 사용자로부터 정수를 입력 받아 입력 받은 정수가 20 이상의 짝수인지 출력하는 프로그램을 작성

value=int(input('정수를 입력하세요>>>'))

Result = (value >= 20) and (value % 2 == 0)
print(f'{value}가 20 이상의 짝수? : {Result}')