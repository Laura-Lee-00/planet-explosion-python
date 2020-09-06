import turtle
import math

# f = ma
# f = -G m1 m2 / r

def mousePressed(x, y):
  G = 6.674 * (10 ** (-11))
  massPlanet = 3*(10**24)
  radiusPlanet = 5000000
  initialVelMag = 6500
  if(x == 0):
    if(y >= 0):
      initialDir = 3.14/2
    else:
      initialDir = 3.14 / 2 * -1
  elif (x<0):
    initialDir = math.atan(y/x) + 3.14
  else:
    initialDir = math.atan(y/x)
  intervalTime = 120
  scale = radiusPlanet / 50
  vX = initialVelMag*math.cos(initialDir)
  vY = initialVelMag*math.sin(initialDir)
  print('Initial Angle',initialDir * 360 / (3.14*2))
  print('InitialVelocity', vX, vY)
  
  turtle.color(1,1,1)
  turtle.pendown()

  positionX, positionY = turtle.position()
  posX = positionX * scale
  posY = positionY * scale
  screen = turtle.Screen()
  while(abs(positionX) < screen.window_width()/2 and abs(positionY) < screen.window_height()/2 and (positionX**2+positionY**2)**0.5 >= 50) :
    positionX, positionY = turtle.position()
    posX = positionX * scale
    posY = positionY * scale
    if(posX == 0):
      if(posY >= 0):
        angle = 3.14/2
      else:
        angle = 3.14 / 2 * -1
    elif (posX<0):
      angle = math.atan(posY/posX) + 3.14
    else:
      angle = math.atan(posY/posX)
    gravForce = G * massPlanet / (posX**2 + posY**2)
    gravX = gravForce*math.cos(angle)
    gravY = gravForce*math.sin(angle)
    vX -= gravX * intervalTime
    vY -= gravY * intervalTime
    posX += vX * intervalTime
    posY += vY * intervalTime
    turtle.goto(posX / scale, posY / scale)

  if (x ** 2 + y ** 2) ** (1/2) < 50 :
      turtle.goto(0,0)
      turtle.color('yellow')
      turtle.dot(100)
      turtle.color('orange')
      turtle.dot(120)
      turtle.color('yellow')
      turtle.dot(140)
      turtle.color('orange')
      turtle.dot(160)
      turtle.color('white')
      turtle.dot(200)
      turtle.dot(500)
      turtle.dot(1000)
      turtle.dot(2000)
      turtle.hideturtle()
      turtle.color('red')
      drawText('GAME OVER', 0, screen.window_height()//2 - 340, size = 50)
      turtle.appStarted()

def appStarted():
  turtle.color('white')
  screen = turtle.Screen()
  turtle.penup()
  winTop = screen.window_height()//2
  drawText('Planet Explosion!', 0, winTop - 40, size = 25)
  drawText('The turtle will orbit around the planet in the direction of your click.', 0, winTop - 65, size = 15)
  drawText('But be careful! If the turtle hits the ground, the planet will explode!', 0, winTop - 90, size = 14)
  turtle.goto(0,0)
  turtle.pensize(10)
  turtle.color('lightgreen')
  turtle.dot(100)
  turtle.goto(0,70)
  turtle.color(0,0,0)
  turtle.pensize(1)
  turtle.shape('turtle')
  #turtle.shearfactor(0.5)  


############################################
# Simple Turtle Framework
# (ignore code below here)
############################################

import string

def drawText(label, x, y, font='Arial', size=30, style='bold', align='center'):
    oldx, oldy = turtle.position()
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(label, font=(font, size, style), align=align)
    turtle.goto(oldx, oldy)
    turtle.pendown()

def main(winWidth, winHeight, bgColor):
    screen = turtle.Screen()
    turtle.speed(0)
    turtle.setup(width=winWidth, height=winHeight)
    screen.bgcolor(bgColor)
    appStarted()
    turtle.speed(10)
    def safeCall(fnName, *args):
        if (fnName in globals()):
            globals()[fnName](*args)
    def keyPressedWrapper(key):
        if (len(key) > 1): key = key.capitalize()
        safeCall('keyPressed', key)
    def bindKey(key):
        if (len(key) > 1) or (ord(key) > 32):
            screen.onkey(lambda: keyPressedWrapper(key), key)
    keys = (['Up', 'Down', 'Left', 'Right', 'space', 'Tab', 'Return'] + 
            list(string.ascii_letters + string.digits))
    for key in keys:
        bindKey(key)
    screen.listen()
    screen.onclick(lambda x, y: safeCall('mousePressed', x, y))
    screen.mainloop()

main(800, 600, 'purple')