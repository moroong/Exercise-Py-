# turtle 모듈을 이용
# 직 사각형을 그리기 위한 사각형의 너비와 높이를 입력을 받고
# 직 사각형을 그리는 프로그램을 작성

import turtle
turtle.shape('turtle')
turtle.speed(1)

# width=int(input(' enter enter the width of rectangle:'))
# height=int(input(' enter enter the height of rectangle:'))
width, height = map(int, input('enter rectangle\'s widht and height : ').split())

angle = 90

turtle.forward(width)
turtle.left(angle)

turtle.forward(height)
turtle.left(angle)

turtle.forward(width)
turtle.left(angle)

turtle.forward(height)
turtle.left(angle)

input('enter any key to exit.')