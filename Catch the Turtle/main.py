import turtle
import random

#General Settings
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch the Turtle")
FONT = ("Arial", 25, "normal")
score = 0
game_over = False

#GRIDS
WIDTH, HEIGHT = 800, 600
screen.setup(WIDTH, HEIGHT)

#Turtle list
turtl_list = []

#Countdown turtle
countdown_turtle = turtle.Turtle()

#Score turtle
score_turtle = turtle.Turtle()

#Restart Button
restart_button = turtle.Turtle()
restart_button.hideturtle()
restart_text_turtle = turtle.Turtle()
restart_text_turtle.hideturtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score = 0", move = False, align = "center", font = FONT)

grid_size = 15

def make_turtle(x, y):
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.color("green")
    t.shapesize(2, 2)
    t.goto(x * grid_size, y * grid_size)
    t.hideturtle()

    def handle_click(x_click, y_click):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score = {score}", move=False, align="center", font=FONT)
        t.hideturtle()

    t.onclick(handle_click)
    turtl_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [10,0,-10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtle():
    for t in turtl_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtle()
        random.choice(turtl_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("blue")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(0, y - 45)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.write(arg=f"Time = {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)
        draw_restart_button()

def draw_background():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.color("white")

    half_w = WIDTH / 2
    half_h = HEIGHT / 2

    # Vertical Lines
    x = -half_w
    while x <= half_w:
        drawer.penup()
        drawer.goto(x, half_h)
        drawer.pendown()
        drawer.goto(x, -half_h)
        x += grid_size

    # Horizontal Lines
    y = -half_h
    while y <= half_h:
        drawer.penup()
        drawer.goto(-half_w, y)
        drawer.pendown()
        drawer.goto(half_w, y)
        y += grid_size

    drawer.penup()

def draw_restart_button():
    hide_turtle()

    restart_button.hideturtle()
    restart_button.penup()
    restart_button.goto(0, 0)
    restart_button.shape("square")
    restart_button.shapesize(2, 6)
    restart_button.color("white")
    restart_button.showturtle()
    restart_button.onclick(restart_game)

    restart_text_turtle.clear()
    restart_text_turtle.penup()
    restart_text_turtle.goto(0, -10)
    restart_text_turtle.color("black")
    restart_text_turtle.write("RESTART", align="center", font=("Arial", 12, "bold"))

def restart_game(x=None, y=None):
    global score, game_over
    score = 0
    game_over = False
    restart_button.hideturtle()
    restart_text_turtle.clear()

    score_turtle.clear()
    score_turtle.write(arg="Score = 0", move=False, align="center", font=FONT)
    countdown_turtle.clear()
    hide_turtle()
    show_turtles_randomly()
    countdown(10)

turtle.tracer(0)
draw_background()
setup_score_turtle()
countdown(10)
setup_turtles()
hide_turtle()
show_turtles_randomly()
turtle.tracer(1)

turtle.mainloop()