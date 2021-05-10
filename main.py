import turtle
import random

pen = turtle.Turtle()












































'''
# Exercise 1
num_of_sides = 5
length_of_side = 50
each_angle = 720.0 / num_of_sides
for i in range(num_of_sides):
	pen.forward(length_of_side)
	pen.right(each_angle)
'''


'''
# Exercise 2
def shape(radius, side):
	pen.circle(radius, 360, side)

shape(float(input("What is the radius: ")), int(input("How many side: ")))
'''


'''
# Exercise 3
colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']
for x in range(40):
	pen.color(colors[x % 6])
	pen.width(x / 5 + 1)
	pen.forward(x)
	pen.left(20)
'''


'''
# Exercise 4
pen.penup()
pen.home()
for a in range(40, -1, -1):
	pen.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	pen.stamp()
	pen.left(a)
	pen.forward(20)
'''

'''
# Exercise 5
wn = turtle.Screen() 
pen.shape("turtle")
pen.speed(0)
pen.pensize(10)

def up():
	pen.heading(90)
	pen.forward(10)
 
def down():
	pen.heading(270)
	pen.left(20)
 
def right():
	pen.heading(0)
	pen.right(20)
   
def left():
	pen.heading(180)
	pen.backward(10)

while (True):
	wn.onkey(up, "Up")
	wn.onkey(down, "Down")
	wn.onkey(right, "Right")
	wn.onkey(left, "Down")
	wn.listen()
	wn.mainloop()
	'''