# turtle 모듈을 사용하여 한 변의 길이가
# 150인 정삼각형을 그리는 파이썬 프로그램을 작성

import turtle
turtle.shape('turtle')

# 이동할 거리
distance = 250

# 회전할 각도
angle = 120

turtle.forward(distance)
turtle.left(angle)

turtle.forward(distance)
turtle.left(angle)

turtle.forward(distance)
turtle.left(angle)

input()