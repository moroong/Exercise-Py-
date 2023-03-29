# turtle 모듈을 이용
# 정 삼각형을 그리기 위한 한 변의 길이를 입력을 받고
# 정 삼각형을 그리는 프로그램을 작성

import turtle
turtle.shape('turtle')
turtle.speed(1)

# 정 삼각형 한 변의 길이( = 거북이가 이동하는 거리)
distance=int(input(' enter the length of triangle: '))
angle = 120

turtle.forward(distance)
turtle.left(angle)

turtle.forward(distance)
turtle.left(angle)

turtle.forward(distance)
turtle.left(angle)

input('enter any key to exit')