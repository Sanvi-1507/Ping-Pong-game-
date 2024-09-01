from os import environ

import turtle
import pygame,sys,time
obj=turtle.Screen()
obj.title("Pong Game")
obj.bgcolor("blue")
obj.setup(width=800,height=600)
pygame.mixer.init()
pygame.mixer.music.load("The fall of marley.mp3")

pygame.mixer.music.play(loops=-1,start=5,fade_ms=2000)
#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("yellow")
paddle_a.penup()
paddle_a.goto(-350,0)
#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("yellow")
paddle_b.penup()
paddle_b.goto(350,0)
#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("pink")
ball.penup()
ball.goto(0,0)
ball.dx=4
ball.dy=-4
#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Paradise Island:0 Marley:0",align='center',font=("Courier",24,'normal'))
#Defining functions
#Paddle A
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    if y<300:
        paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    if y>-300:
        paddle_a.sety(y)
#Paddle B
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    if y<300:
        paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    if y>-300:
        paddle_b.sety(y)

    
#Keyboard binding
obj.listen()
#Paddle A
obj.onkeypress(paddle_a_up,"w")
obj.onkeypress(paddle_a_down,"s")
#Paddle B
obj.onkeypress(paddle_b_up,"Up")
obj.onkeypress(paddle_b_down,"Down")

score_a=0
score_b=0


#Main game loop
try:
    while True:
        obj.update()
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1.1
            score_a+=1
            pen.clear()
            pen.write("Paradise Island:{} Marley:{}".format(score_a,score_b),align='center',font=("Courier",24,'normal'))
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx*= -1.1
            score_b+=1
            pen.clear()
            pen.write("Paradise Island:{} Marley:{}".format(score_a,score_b),align='center',font=("Courier",24,'normal'))

    #Paddle and ball collisons
        if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+60 and ball.ycor()>paddle_b.ycor()-60):
            ball.dx*=-1
        if (ball.xcor()>-350 and ball.xcor()<-340) and (ball.ycor()<paddle_a.ycor()+60 and ball.ycor()>paddle_a.ycor()-60):
            ball.dx*=-1
    pygame.mixer.music.unload()
 
except turtle.Terminator:
    print("Turtle graphics window closed. Exiting the game.")



