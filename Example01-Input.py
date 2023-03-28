import turtle
turtle.shape('turtle')
turtle.speed(1)

# 도형을 그리기 위한 두 변의 길이를 입력

a, b = map(int, input(' 도형을 그리기 위한 두 변의 길이를 입력하세요. ').split()) # '300 250'
# a, b = map(int, '300 250'.split()) # '300 250'
# a, b = map(int, ['300', '250']) # '300 250'
# a, b - (300, 250) # '300 250'

angle_1 = int(input(' 도형을 그리기 위한 좌하단 각도를 입력하세요. ')) # '60'
# angle_1 = int('60')
# angle_1 = 60

angle_2 = 180 - angle_1

turtle.forward(a)
turtle.left(angle_1)

turtle.forward(b)
turtle.left(angle_2)

turtle.forward(a)
turtle.left(angle_1)

turtle.forward(b)
turtle.left(angle_2)

input('enter any key to exit')