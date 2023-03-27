# 사용자로부터 이름과 나이를 입력을 받아
# 출력하는 프로그램을 작성

name=input(' 이름을 입력하세요>>> ')
age=input('나이를 입력하세요>>> ')

print(f'입력된 이름은 {name} 입니다.')
print(f'입력된 나이는 {age}세 입니다')

# print('입력된 이름은 {}입니다.'.format(name))
# print('입력된 나이는 {}세 입니다.'.format(age))

# 10년 뒤의 나이를 출력
after10 = int(age) + 10
print(f'10년 뒤의 나이는 {after10}세 입니다.')