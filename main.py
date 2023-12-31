import turtle
import random

WIDTH = 800
HEIGHT = 600
DELAY = 200  # milli-seconds
FOOD_SIZE = 30

offsets = {
    'up': (0, 20),
    'down': (0, -20),
    'left': (-20, 0),
    'right': (20, 0)
}


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction('up'), 'Up')
    screen.onkey(lambda: set_snake_direction('down'), 'Down')
    screen.onkey(lambda: set_snake_direction('left'), 'Left')
    screen.onkey(lambda: set_snake_direction('right'), 'Right')


def set_snake_direction(direction):
    global snake_direction

    if direction == 'up':
        if snake_direction != 'down':
            snake_direction = 'up'
    elif direction == 'down':
        if snake_direction != 'up':
            snake_direction = 'down'
    elif direction == 'left':
        if snake_direction != 'right':
            snake_direction = 'left'
    elif direction == 'right':
        if snake_direction != 'left':
            snake_direction = 'right'


def reset():
    global score, snake, snake_direction, food_pos

    score = 0
    snake = [[0, 0], [20, 0]]
    snake_direction = 'up'
    food_pos = get_random_food_pos()
    food.goto(food_pos)

    game_loop()


def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
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
    global food_pos, score, DELAY
    if get_distance(snake[-1], food_pos) < 20:
        score += 1  # add score after fed
        # speed-up on score
        if DELAY > 90:
            DELAY -= 5

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
screen.bgcolor("yellow")
screen.tracer(0)  # disable-auto-animations

# Event Handlers
screen.listen()
bind_direction_keys()

# set-stamper (snake-indicator)
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("green")
stamper.penup()

# create snake list-representation

food = turtle.Turtle()
food.shape('triangle')
food.shapesize(FOOD_SIZE / 20)
food.color('red')
food.penup()


# set animation in motion
reset()

# Finish -
turtle.done()
