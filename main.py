import turtle

WIDTH = 500
HEIGHT = 500
DELAY = 400  # milli-seconds

offsets = {
    'up': (0, 20),
    'down': (0, -20),
    'left': (-20, 0),
    'right': (20, 0)
}


def go_up():
    global snake_direction

    if snake_direction != 'down':
        snake_direction = 'up'


def go_down():
    global snake_direction

    if snake_direction != 'up':
        snake_direction = 'down'


def go_left():
    global snake_direction

    if snake_direction != 'right':
        snake_direction = 'left'


def go_right():
    global snake_direction

    if snake_direction != 'left':
        snake_direction = 'right'


def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

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

# Event Handlers
screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')


# set-stamper (snake-indicator)
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# create snake list-representation
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = 'up'

for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# set animation in motion
move_snake()

# Finish -
turtle.done()
