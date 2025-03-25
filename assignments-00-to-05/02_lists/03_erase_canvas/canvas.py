import turtle

CANVAS_SIZE = 400
CELL_SIZE = 40
ERASER_SIZE = 25
BG_COLOR = "cyan"
ERASER_COLOR = "grey"


screen = turtle.Screen()
screen.setup(CANVAS_SIZE, CANVAS_SIZE)
screen.bgcolor(BG_COLOR)
screen.tracer(1) 


cells = []
for x in range(-CANVAS_SIZE//2, CANVAS_SIZE//2, CELL_SIZE):
    for y in range(-CANVAS_SIZE//2, CANVAS_SIZE//2, CELL_SIZE):
        cell = turtle.Turtle()
        cell.speed(0)
        cell.penup()
        cell.goto(x, y)
        cell.pendown()
        cell.fillcolor(BG_COLOR)
        cell.begin_fill()
        for _ in range(4):
            cell.forward(CELL_SIZE)
            cell.right(90)
        cell.end_fill()
        cells.append((cell, x, y))


eraser = turtle.Turtle()
eraser.shape("square")
eraser.shapesize(ERASER_SIZE/20)
eraser.color(ERASER_COLOR)
eraser.penup()


def erase_objects(x, y):
    for cell, cx, cy in cells:
        if (cx - ERASER_SIZE/2 <= x <= cx + CELL_SIZE + ERASER_SIZE/2 and
            cy - ERASER_SIZE/2 <= y <= cy + CELL_SIZE + ERASER_SIZE/2):
            cell.fillcolor("white")


def move_eraser(x, y):
    eraser.goto(x, y)
    erase_objects(x, y)


screen.onscreenclick(move_eraser)


screen.mainloop()