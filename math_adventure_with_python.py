from turtle import *

# 1-1 Square Dance

shape('turtle')
speed(5)

# def square(sidelength = 100):
# 	for i in range(4):
# 		forward(sidelength)
# 		right(90)

# 1-2 A Circle of Squares

# for i in range(180):
# 	square(150)
# 	right(2)

# 1-3 Tri and Tri Again

# def triangle(sidelength):
# 	for i in range(3):
# 		forward(sidelength)
# 		right(120)

# triangle(450)


def polygon(sidelength = 100, sides = 6):
	for side in range(sides):
		forward(sidelength)
		right(360 / sides)

polygon(40, 4)


