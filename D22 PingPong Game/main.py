from turtle import Turtle, Screen 
from paddleclass import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

t = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.title("The Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_left.move_down, "s")
screen.onkey(paddle_left.move_up, "w")


ball = Ball()
score = Scoreboard()

t.penup()
t.color("white")
t.goto(0,-300)
t.setheading(90)
t.pendown()
t.forward(600)
t.hideturtle()




game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    

    #detect right paddle miss the ball
    if ball.xcor() > 380 :
        ball.reset()
        score.l_point()

    #detect left paddle miss the ball
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


    



screen.exitonclick()


# paddle.create_paddle()
# screen.update()




















