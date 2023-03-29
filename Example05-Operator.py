
# 참고 사이트 
#   - 백준 알고리즘 저지
#   - 프로그래머스


#  사용자로부터 두 개의 점수를 입력 받아
#  두 점수가 각각 40점 이상이거나, 두 점수의 평균이 50점 이상이면 "Pass"를 출력
#  그렇지 않으면 "Fail"을 출력하는 프로그램 작성

score1, score2 = map(int, input(' 두 개의 점수를 입력하세요>>> ').split())
above = (score1 >= 40) and (score2 >= 40)
average = ((score1+score2)/2) >= 50
Result = 'Pass' if above or average else 'Fail'

print(f'score1 : {score1}')
print(f'score2 : {score2}')
print(f'average : {average}')
print(f'Result : {Result}')

