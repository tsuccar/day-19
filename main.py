from turtle import Turtle, Screen
import random
############################
# Challenge 1 -Etch-A-Sketch
############################

# tim=Turtle()
# screen=Screen()
# tim.speed('fast')
# def move_forward():
# 	tim.fd(5)
# def move_backward():
# 	tim.bk(5)
# def clockwise():
# 	new_heading=tim.heading() + 10
# 	tim.setheading(new_heading)
# def counter_clockwise():
# 	new_heading=tim.heading() - 10
# 	tim.setheading(new_heading)
# def clear():
# 	tim.clear()
# 	tim.penup()
# 	tim.home()
#
# screen.onkey(fun=move_forward,key="w")
# screen.onkey(fun=move_backward,key="s")
# screen.onkey(fun=clockwise,key="d")
# screen.onkey(fun=counter_clockwise,key="a")
# screen.onkey(fun=clear,key="c")
# screen.listen()


#############################
# Challenge 2 - Turtle Race
#############################
screen=Screen()
screen.setup(width=500,height=400)
user_guess=screen.textinput(title="Turtle-Chase",prompt="which color will win :").lower()
colors=["red","orange","yellow","green","blue","purple"]
distances=[1,5,8,6,4,3]

list_of_turtle_objects=[]
for index in range(0,5):
	starting_index = -100
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colors[index])
	new_turtle.penup()
	new_turtle.goto(x=-230, y= (starting_index+(index *50)))
	list_of_turtle_objects.append(new_turtle)

def set_go(obj):
	if obj.xcor() == 230.0:
		print(obj.xcor())
		return obj.xcor()
	else:
		obj.forward(random.randint(0,10))
		print(obj.xcor())
		return obj.xcor()
GAME=False
if user_guess:
	GAME=True

while GAME:
	for turtle in list_of_turtle_objects:
		distance = set_go(turtle)
		if distance >= 230.0:
			GAME=False
			winnig_color = turtle.pencolor()
			print(f" {winnig_color} wins !")

if winnig_color == user_guess:
	print(" you win ")
else:
	print("you lose !")
	 

screen.exitonclick()