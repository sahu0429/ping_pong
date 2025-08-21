import turtle
import winsound

# Window Setup
window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle One
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.color("white")
paddle_one.shape("square")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350, 0)

# Paddle Two
paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.color("white")
paddle_two.shape("square")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Scoreboard
score_one = 0
score_two = 0

write_score = turtle.Turtle()
write_score.speed(0)
write_score.color("white")
write_score.penup()
write_score.hideturtle()
write_score.goto(0, 260)
write_score.write("Player One: 0        Player Two: 0", align="center", font=("Courier", 24, "normal"))

# Pause Flag
is_paused = False 

status_writer = turtle.Turtle()
status_writer.speed(0)
status_writer.color("yellow")
status_writer.penup()
status_writer.hideturtle()
status_writer.goto(0, 230)

def update_status_message():
    status_writer.clear()
    if is_paused:
        status_writer.write("Game Paused - Press 'R' to Resume | 'Space' to Reset", align="center", font=("Courier", 16, "italic"))
    else:
        status_writer.write("Press 'P' to Pause | 'Space' to Reset", align="center", font=("Courier", 16, "italic"))

update_status_message()

# Movement Functions
def paddle_one_up():
    y = paddle_one.ycor()
    y += 50
    paddle_one.sety(y)

def paddle_one_down():
    y = paddle_one.ycor()
    y -= 50
    paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y += 50
    paddle_two.sety(y)

def paddle_two_down():
    y = paddle_two.ycor()
    y -= 50
    paddle_two.sety(y)

def pause_game():
    global is_paused
    is_paused = True
    update_status_message()

def resume_game():
    global is_paused
    is_paused = False
    update_status_message()

def reset_game():
    global score_one, score_two
    score_one = 0
    score_two = 0
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = -0.2
    paddle_one.goto(-350, 0)
    paddle_two.goto(350, 0)
    write_score.clear()
    write_score.write("Player One: 0        Player Two: 0", align="center", font=("Courier", 24, "normal"))
    update_status_message() 


# Keyboard Bindings
window.listen()
window.onkeypress(paddle_one_up, 'w')
window.onkeypress(paddle_one_down, 's')
window.onkeypress(paddle_two_up, 'Up')
window.onkeypress(paddle_two_down, 'Down')
window.onkeypress(pause_game, 'p')
window.onkeypress(resume_game, 'r') 
window.onkeypress(reset_game, 'space') 


while True:
    window.update()

    if is_paused:
        continue  # Skip frame if game is paused

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Right Wall — Player One Scores
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -0.2
        ball.dy = 0.2 if ball.dy > 0 else -0.2
        score_one += 1
        write_score.clear()
        write_score.write(f"Player One: {score_one}        Player Two: {score_two}", align="center", font=("Courier", 24, "normal"))

    # Left Wall — Player Two Scores
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 0.2
        ball.dy = 0.2 if ball.dy > 0 else -0.2
        score_two += 1
        write_score.clear()
        write_score.write(f"Player One: {score_one}        Player Two: {score_two}", align="center", font=("Courier", 24, "normal"))

    # Paddle Collisions
    if (340 < ball.xcor() < 350) and (paddle_two.ycor() + 40 > ball.ycor() > paddle_two.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.05
        ball.dy *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (-350 < ball.xcor() < -340) and (paddle_one.ycor() + 40 > ball.ycor() > paddle_one.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.05
        ball.dy *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
