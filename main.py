import turtle

WIDTH = 500
HEIGHT = 500

# Create a window to draw on
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Python Snake (Game)")
screen.bgcolor("cyan")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")

my_turtle.forward(100)

turtle.done()
