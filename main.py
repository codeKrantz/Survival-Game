import random
import time
import turtle as t
print("""
Welcome to Survival!

Avoid the SQUARE OF DEATH and pick up turtles to earn points by using the up, down, left and right arrows.

Hit the space bar to begin in the output tab .""")

#background
canvas = t.Screen()
canvas.bgcolor('blue')

#create player
player = t.Turtle()
player.shape('circle')
player.color('red')
player.shapesize(1,1)
player.speed(0)
player.penup()
player.setx(0)
player.sety(0)
player.showturtle()

#create enemy
enemy = t.Turtle()
enemy.shape('square')
enemy.shapesize(3,3)
enemy.color('black')
enemy.speed(0)
enemy.penup()
enemy.hideturtle()

#Clone enemy
ETwo = t.Turtle()
ETwo = enemy.clone()


#create points
TurtlePoint = t.Turtle()
TurtlePoint.shape('turtle')  
TurtlePoint.color('green')
TurtlePoint.speed(0)
TurtlePoint.penup()
TurtlePoint.hideturtle()

#create score
player_score = t.Turtle()
player_score.speed()
player_score.hideturtle()

#enemy spawn
def EnemySpawn():
  enemy.hideturtle()
  enemy.setx(random.randint(-150,150))
  enemy.sety(200)
  enemy.showturtle()

def ETwoSpawn():
  ETwo.hideturtle()
  ETwo.setx(random.randint(-150,150))
  ETwo.sety(200)
  ETwo.showturtle()

#TurtlePoint spawn
def TurtlePointSpawn():
  TurtlePoint.hideturtle()
  TurtlePoint.setx(-200)
  TurtlePoint.sety(random.randint(-150,150))
  TurtlePoint.showturtle()

#create Enemy falling
def EnemyFall(EnemyFallSpeed):
  enemy.setheading(270)
  enemy.forward(EnemyFallSpeed)

def ETwoFall(ETwoFallSpeed):
  ETwo.setheading(270)
  ETwo.forward(ETwoFallSpeed)

#create TurtlePoint falling
def TurtlePointFall(TurtlePointFallSpeed):
  TurtlePoint.setheading(0)
  TurtlePoint.forward(TurtlePointFallSpeed)

#create player movment
def Up():
  player.setheading(90)
  player.forward(10)
def Left():
  player.setheading(180)
  player.forward(10)
def Down():
  player.setheading(270)
  player.forward(10)
def Right():
  player.setheading(0)
  player.forward(10)

def ScoreDisplay(currentScore):
	player_score.clear()
	player_score.penup()
	scoreXPosition = (t.window_width()/2)-50
	scoreYPosition = (t.window_height()/2)-50
	player_score.setpos(scoreXPosition,scoreYPosition)
	player_score.write(str(currentScore),align = 'right',font = ('Arial',40,'bold'))

#GAME OVER SCREEN
def gameOver():
  player.color("blue")
  enemy.color("blue")
  ETwo.color("blue")
  TurtlePoint.color("blue")
  t.penup()
  t.hideturtle()
  t.write("GAME OVER",align='center',font=("Arial",30,'bold'))

#GAME START
def StartGame():
  score = 0
  player.color('red')
  EnemySpawn()
  TurtlePointSpawn()
  ETwoSpawn()
  
  while True:
    ScoreDisplay(score)
    while True:
      if score <= 4.5 :
        TurtlePointFall(4)
        EnemyFall(5)
        ETwoFall(3)
      elif score >=11.5:
        TurtlePointFall(7)
        EnemyFall(8)
        ETwoFall(6)
      elif score >= 9.5:
        TurtlePointFall(6)
        EnemyFall(7)
        ETwoFall(5)
      elif score > 4.6:
        TurtlePointFall(5)
        EnemyFall(6)
        ETwoFall(4)
      if player.distance(TurtlePoint) < 20:
        score += 1
        TurtlePointSpawn()
        break
      elif TurtlePoint.pos()[0] > 190:
        TurtlePointSpawn()
        break
        
      if enemy.pos()[1] < -199:
        EnemySpawn()
        break
      elif player.distance(enemy) < 30:
        break

      if ETwo.pos()[1] <= -199:
        ETwoSpawn()
      elif player.distance(ETwo) < 30:
        break
    if player.distance(enemy) < 30:
      gameOver()
      break
    elif player.distance(ETwo) < 30:
      gameOver()
      break

#Movement and control
t.onkey(StartGame,"space")
t.onkey(Up,"Up")
t.onkey(Left,"Left")
t.onkey(Down,"Down")
t.onkey(Right,"Right")
t.listen()
t.mainloop()

