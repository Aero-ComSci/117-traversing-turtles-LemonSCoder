#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# Data structures (lists) to store turtles and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "turtle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "yellow"]
new_list = ["dog", "cat","mouse", "bird", "monkey"]

#public class that contains a loop that iterates through the data structure.
class turtleDrawings:
    def __init__(self, shape, colors, turtle_storage, new_list):
        self.shape = shape
        self.colors = colors
        self.new_list = new_list
        self.turtle_storage = turtle_storage
    def change_turtle_loc(self):
        #Makes sure the turtle pen will create an equilateral n-gon.
        previous_turtle_degree = 360 / len(self.shape)
        for t in self.turtle_storage:
            #This code isn't of use, but, nonetheless, it's here.
            #Puts pen up (makes it invisible; no visible markings while it's moving)
            t.penup()
            #Makes sure next turtle object begins drawing where the last turtle left off
            t.goto(t.xcor(), t.ycor())
            #Puts pen down (makes it visible again))
            t.pendown()
            t.right(previous_turtle_degree)  
            #Changed amount turtle pen moves forward before turning again.
            t.forward(45)
    def draw_turtle(self):
        for s in self.shape:
            t = trtl.Turtle(shape=s)
            #Changed turtle pen's size (bigger now)
            t.pensize(5)
            #Stores which shapes used in the program in a list.
            self.turtle_storage.append(t)
            #Makes sure each turtle is a different color
            new_color = self.colors.pop()
            t.pencolor(new_color)
            #Able to call change_turtle_loc() without any errors.
            self.change_turtle_loc()
    def __str__(self):
        #Output using self.new_list.
        return "While calling print(new_list) would output {}, iterating through each item in the list will make each item be printed out individually.".format(self.new_list)

#Calls turtleDrawings class with given lists as parameters.
turtle_drawing = turtleDrawings(turtle_shapes, turtle_colors, my_turtles, new_list)
#Actually draws the turtles.
turtle_drawing.draw_turtle()

wn = trtl.Screen()
wn.mainloop()
