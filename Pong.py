import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.screensize(800,600,"black")
wn.tracer(0)

score_a = 0
score_b = 0
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") #normally 20x20 pixels
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1 ) #now 20x100 pixels
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1 )
paddle_b.penup()
paddle_b.goto(350,0)

 #Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .2
ball.dy = .2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24,"normal"))

def paddle_a_up():
    y= paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y= paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



#Keyboard Bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_a.ycor() < -250:
        paddle_b.sety(-250)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier",24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier",24,"normal"))

    #Collisions
    if ball.xcor() > 330 and ball.xcor() < 340 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() < -330 and ball.xcor() > -340 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.dx *= -1 
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)