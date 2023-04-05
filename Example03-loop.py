# 1 에서 100 사이의 값들 중 3의 제곱수들을 리스트에 저장하여 출력
#  - 1, 4, 9, 16, 25, 36 ....

start = 1
end = 100
exp = []

for n in range(start , end + 1) :
    # ** 연산자 : 제곱 연산자 / n의 4승 n ** 4
    # 제곱수가 end를 초과한 경우 더 이상 제곱수가 없기 때문에 반복문을 종료
    if(n ** 2 > end) : break

    exp.append(n ** 2)

