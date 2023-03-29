# 두 변의 길이 a, b와 하나의 내각을 입력 받아 
# 평행사변형을 그리는 프로그램 작성

import turtle
turtle.shape('turtle')
turtle.speed(1)

length_a, lenght_b, angle = map(int, input('enter parallelogram\'s length_a and length_b and angle : ').split())


turtle.forward(length_a)
turtle.left(angle)

turtle.forward(lenght_b)
turtle.left(180-angle)

turtle.forward(length_a)
turtle.left(angle)

turtle.forward(lenght_b)
turtle.left(180-angle)

input('enter any key to exit.')