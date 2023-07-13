import turtle
import random

WIDTH = 500
HEIGHT = 500
DELAY = 70  # milli-seconds
FOOD_SIZE = 10

offsets = {
    'up': (0, 20),
    'down': (0, -20),
    'left': (-20, 0),
    'right': (20, 0)
}
score = 0


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


def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        turtle.bye()
    else:
        # add new-head to snake body
        snake.append(new_head)

        # check food-collision
        if not food_collision():
            snake.pop(0)

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
        # refresh screen
        screen.title(f"Snake Game. score {score}")
        screen.update()

        # repeat-func
        turtle.ontimer(game_loop, DELAY)


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1  # add score after fed
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True

    return False


def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)

    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** .5
    return distance


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

food = turtle.Turtle()
food.shape('circle')
food.shapesize(FOOD_SIZE / 20)
food.color('red')
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

# set animation in motion
game_loop()

# Finish -
turtle.done()
