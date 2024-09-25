#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# Data structures (lists) to store turtles and colors
#Changed 'turtle_shapes' and 'turtle_colors' to have one more element in them
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "turtle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "yellow"]
new_list = ["dog", "cat","mouse", "bird", "monkey"]

#Clone list so that the program can reference the original list's original length later on
turtle_shapes_clone = turtle_shapes.copy()

global increment_number
increment_number = 0

global original_list_length
original_list_length = len(turtle_shapes)

#public class that contains a loop that iterates through the data structure.
class turtleDrawings:
    def __init__(self, shape, colors, turtle_storage, new_list):
        self.shape = shape
        self.colors = colors
        self.new_list = new_list
        self.turtle_storage = turtle_storage
    def change_turtle_loc(self, increment_number):
        #Makes sure the turtle pen will create an equilateral n-gon.
        previous_turtle_degree = 360 / len(self.shape)
        move_by = 0
        move_by_2 = 0
        #Referencing cloned list
        for i in range(len(turtle_shapes_clone)):
            #Prevents IndexError from occurring.
            if len(self.shape) != 0 and len(self.colors) != 0:
                s = self.shape.pop()
                #Declares different pen shape everytime.
                t = trtl.Turtle(shape=s)
                #Changes pen size (larger)
                t.pensize(5)
                #Declares different color for pen to use everytime.
                new_color = self.colors.pop()
                t.pencolor(new_color)
                t.penup()
                #Makes sure next turtle object begins drawing where the last turtle left off
                t.goto(t.xcor() + move_by, t.ycor() + move_by_2)
                #Puts pen down (makes it visible again))
                t.pendown()
                #Makes sure same pen shape/color is used for six sides.
                for color in range(6):
                        increment_number += 10
                        #This code isn't of use, but, nonetheless, it's here.
                        #Puts pen up (makes it invisible; no visible markings while it's moving)
                        t.right(previous_turtle_degree)  
                        #Changed amount turtle pen moves forward before turning again.
                        t.forward(increment_number)
                #Makes sure pens pick up where the other pen left off
                move_by += 30
                move_by_2 += 52
    def __str__(self):
        #Output using self.new_list.
        return "While calling print(new_list) would output {}, iterating through each item in the list will make each item be printed out individually.".format(self.new_list)

#Calls turtleDrawings class with given lists as parameters.
turtle_drawing = turtleDrawings(turtle_shapes, turtle_colors, my_turtles, new_list)
#Actually draws the turtles.
turtle_drawing.change_turtle_loc(increment_number)

wn = trtl.Screen()
wn.mainloop()
