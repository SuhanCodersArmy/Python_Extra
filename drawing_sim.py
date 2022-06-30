# In this file we make a drawing simulator 
# Developed by Suhan Munjal 
# instagram:- https://www.instagram.com/suhan.mj_28/
# facebook:- https://www.facebook.com/profile.php?id=100058785083032
# github:- https://github.com/SuhanCodersArmy
# follow for more
from turtle import Turtle, Screen

xyz = Turtle()
abc = Screen()

def func0():
    """This function will allow user to go forward 20 px"""
    xyz.forward(20)

def func1():
    """This function will allow user to go right"""
    xyz.right(5)

def func2():
    """This function will allow user to go left"""
    xyz.left(5)

def func3():
    """This function will allow user to go backward 20 px"""
    xyz.backward(20)

abc.onkey(func0, 'Up')
abc.onkey(func1, 'Right')
abc.onkey(func2, 'Left')
abc.onkey(func3, 'Down')
abc.listen()
abc.exitonclick()