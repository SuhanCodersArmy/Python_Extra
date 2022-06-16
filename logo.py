# In this file we are going to create logos of different companies
# importing turtle to create logos
from turtle import Turtle, Screen
xyz = Turtle()

def netflix():
    """In this function we're going to create the logo of Netflix"""
    def square():
        """This function will create the background box"""
        xyz.begin_fill()
        xyz.left(90)
        xyz.forward(200)
        xyz.right(90)
        xyz.forward(200)
        xyz.right(90)
        xyz.forward(200)
        xyz.right(90)
        xyz.forward(200)
        xyz.end_fill()
    def n():
        """This function will create the 'N' letter"""
        def bar(): 
            xyz.begin_fill()
            xyz.color('red')
            xyz.left(90)
            xyz.forward(100)
            xyz.right(90)
            xyz.forward(20)
            xyz.right(90)
            xyz.forward(100)
            
            xyz.end_fill()
        
        bar()
        xyz.color('black')
        xyz.left(90)
        xyz.forward(40)
        xyz.color('red')
        bar()
        xyz.right(90)
        xyz.forward(20)
        xyz.begin_fill()
        xyz.right(90)
        xyz.forward(30)
        xyz.left(30)
        xyz.forward(80)
        xyz.left(150)
        xyz.forward(40)
        xyz.left(32)
        xyz.forward(80)
        xyz.end_fill()
        
    square()
    xyz.right(90)
    xyz.forward(50)
    xyz.right(90)
    xyz.forward(60)
    n()

netflix()
my_screen = Screen()
my_screen.exitonclick()
