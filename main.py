import turtle
import math

def generate_commands(limit: int) -> list[str]:
    commands = []
    for n in range(limit):
        ones = bin(n).count("1")
        command = "F" if ones % 2 == 0 else "T"
        commands.append(command)
    return commands

def compute_bounds(commands):
    x, y, angle = 0, 0, 0
    xs, ys = [0], [0]
    for cmd in commands:
        if cmd == "F":
            x += math.cos(math.radians(angle))
            y += math.sin(math.radians(angle))
            xs.append(x)
            ys.append(y)
        elif cmd == "T":
            angle += 60
    return min(xs), max(xs), min(ys), max(ys)

def get_primes(limit: int) -> list[int]:
    primes = []
    for n in range(2, limit):
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break 
        if is_prime:
            primes.append(n)
    return primes

def draw(commands):
    width_margin = 1100
    height_margin = 700

    min_x, max_x, min_y, max_y = compute_bounds(commands)  # step=1 always
    bounds_w = max_x - min_x
    bounds_h = max_y - min_y

    step = min(width_margin / bounds_w, height_margin / bounds_h)  # now step is defined

    start_x = -(min_x + max_x) / 2 * step
    start_y = -(min_y + max_y) / 2 * step

    turtle.setup(width=1200, height=800)
    turtle.bgcolor("black")

    t = turtle.Turtle()
    t.color("white")
    t.speed(0)
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(0)
    t.pendown()

    for cmd in commands:
        if cmd == "F":
            t.forward(step)
        elif cmd == "T":
            t.left(60)

    turtle.done()

cmds = generate_commands(4096)
draw(cmds)