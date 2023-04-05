# 영화 평점 1 점부터 5 점 까지 출력하는 프로그램을 작성
# 1 ~ 5 사이의 값을 입력 받고 입력한 값 만큼의 '★' 을 출력
# 만약 범위 밖의 값을 입력을 받은 경우 다시 입력을 받도록 요구(답은 아래로)


while True :
    score = int(input(' 영화의 평점을 입력하세요. '))
    if score < 1 or score > 5 :
        print('평점은 1~5 범위 내로 입력해야합니다.')

    elif score >= 1 or score <= 5 :
        print('영화 평점 : ', end='')
        print('★' * score)



'''방법1

rating = int( input( '이번 영화의 평점을 입력하세요 >>> '))

# 유효한 값이 입력될 때 까지 반복

while rating <= 0 or rating > 5 :
    print(' 평점은 1 ~ 5점 사이만 입력해야 합니다. ')
    rating = int( input( ' 이번 영화의 평점을 입력하세요>>> '))

# 출력
print('영화 평점 : ', end='')
print("★" * rating)
'''

'''방법2
# 유효한 값을 입력할 때 까지
while True :
    # 입력
    rating = int( input( '이번 영화의 평점을 입력하세요 >>> '))

    # 검사
    if rating > 0 and rating <= 5 :
        break
    print(' 평점은 1 ~ 5점 사이만 입력해야 합니다. ')

# 출력
print('영화 평점 : ', end='')
print("★" * rating)
'''

'''방법 3
# 유효한 값을 입력할 때 까지
while True :
    # 입력
    rating = int( input( '이번 영화의 평점을 입력하세요 >>> '))

    # 검사
    if rating <= 0 and rating > 5 :
        print(' 평점은 1 ~ 5점 사이만 입력해야 합니다. ')
        continue
    
    break # 반복문 종료

# 출력
print('영화 평점 : ', end='')
print("★" * rating)
'''