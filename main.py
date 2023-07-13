import turtle

WIDTH = 500
HEIGHT = 500
DELAY = 400  # milli-seconds


def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += 20

    # add new-head to snake body
    snake.append(new_head)

    # remove last-segment of snake
    snake.pop(0)

    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    # refresh screen
    screen.update()

    # repeat-func
    turtle.ontimer(move_snake, DELAY)


# Create a window to draw on
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Python Snake")
screen.bgcolor("pink")
screen.tracer(0)  # disable-auto-animations

# set-stamper (snake-indicator)
stamper = turtle.Turtle()
stamper.shape("square")

stamper.penup()

# create snake list-representation
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()
    stamper.penup()

# set animation in motion
move_snake()

# Finish -
turtle.done()
