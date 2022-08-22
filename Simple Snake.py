#Snake

#importing modules
from turtle import *
from time import sleep
from random import randint, choice
from math import sqrt


#creating window
wn = Screen()
wn.setup(600, 550)
wn.title("Simple Snake")
wn.tracer(0)
wn.register_shape("apple.gif")

#setting choice
setting = input("Select a colormode (black, white, blue, green): ")
if setting == "black":
    background_color = "black"
    border_color = "white"
    snake_color = "white"
    tail_color = "white"
    score_color = "white"

elif setting == "white":
    background_color = "white"
    border_color = "black"
    snake_color = "black"
    tail_color = "black"
    score_color = "black"

elif setting == "blue":
    background_color = "white"
    border_color = "black"
    snake_color = "blue"
    tail_color = "cyan"
    score_color = "black"

elif setting == "green":
    background_color = "white"
    border_color = "black"
    snake_color = "green"
    tail_color = "light green"
    score_color = "black"
    
wn.bgcolor(background_color)

#Game class
class Game:
    def __init__(self, FPS, state, score):
        self.FPS = FPS
        self.state = state
        self.score = score
        self.pen = Turtle()

    def start(self):
        if self.state == "static":
            self.state = "running"
            head.speed = 20

    def update_score(self):
        self.score += 1
        self.pen.clear()
        self.pen.up()
        self.pen.hideturtle()
        self.pen.color(score_color)
        self.pen.setpos(0, 204)
        self.pen.write(f"{self.score}", align="center", font=("arial", 42, "bold"))


#Border class
class Border(Turtle):
    def __init__(self, x, y, color, pensize):
        Turtle.__init__(self)
        self.up()
        self.color(color)
        self.hideturtle()
        self.pensize(pensize)
        self.setpos(x, y)
        self.down()

        for i in range(2):
            self.fd(510)
            self.rt(90)
            self.fd(430)
            self.rt(90)


#Snake class
class Snake(Turtle):
    def __init__(self, x, y, color, shape, radius, speed, direction):
        Turtle.__init__(self)
        self.penup()
        self.color(color)
        self.shape(shape)
        self.shapesize(radius)
        self.seth(0)
        self.speed = speed
        self.direction = direction

    def move(self):
        self.fd(self.speed)

    def left(self):
        if self.direction == "up" or self.direction == "down":
            self.seth(180)
            self.direction = "left"

    def right(self):
        if self.direction == "up" or self.direction == "down":
            self.seth(0)
            self.direction = "right"

    def up(self):
        if self.direction == "left" or self.direction == "right":
            self.seth(90)
            self.direction = "up"

    def down(self):
        if self.direction == "left" or self.direction == "right":
            self.seth(270)
            self.direction = "down"

    def distance_from(self, other):
        self.distance = sqrt(pow((self.xcor() - other.xcor()), 2) + pow((self.ycor() - other.ycor()), 2))

    def eat(self):
        if self.distance < 19:
            return True

    def bitten_itself(self):
        if self.distance < 15:
            print()
            return True

    def collision(self, other):
        if self.ycor() > 181:
            self.sety(181)
            game.state = "game over"
        elif self.ycor() < -221:
            self.sety(-221)
            game.state = "game over"
        elif self.xcor() > 241:
            self.setx(241)
            game.state = "game over"
        elif self.xcor() < -241:
            self.setx(-241)
            game.state = "game over"


#Segment class
class Tail(Turtle):
    def __init__(self, x, y, color, shape, radius):
        Turtle.__init__(self)
        self.penup()
        self.color(color)
        self.shape(shape)
        self.shapesize(radius)
        self.setpos(x, y)
            

#Food class
class Food(Turtle):
    def __init__(self, shape, radius):
        Turtle.__init__(self)
        self.penup()
        self.shape(shape)
        self.shapesize(radius)
        self.x = choice(food_xpos)
        self.y = choice(food_ypos)
        self.setpos(self.x, self.y)

    def pick_new_location(self):
        self.x = choice(food_xpos)
        self.y = choice(food_ypos)
        self.setpos(self.x, self.y)

    


#creating class objects
game = Game(13.5, "static", -1)
game.update_score()

border = Border(-255, 195, border_color, 5)

food_xpos = []
food_ypos = []

for i in range(-240, 241, 20):
    food_xpos.append(i)

for i in range(-220, 181, 20):
    food_ypos.append(i)


food = Food("apple.gif", 0.8)

snake = []
snake.append(Tail(0, 0, tail_color, "square", 0.8))

head = Snake(0, 0, snake_color, "square", 0.8, 0, "right")

#keybindings
listen()
onkey(game.start, "space")
onkey(head.left, "a")
onkey(head.right, "d")
onkey(head.up, "w")
onkey(head.down, "s")
onkey(head.left, "Left")
onkey(head.right, "Right")
onkey(head.up, "Up")
onkey(head.down, "Down")


#main game loop
while game.state == "running" or game.state == "static":
    wn.update()
    sleep(1/game.FPS)

    head.move()
    head.distance_from(food)
    head.collision(border)

    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].setpos(x, y)

    if len(snake) > 0:
        x = head.xcor()
        y = head.ycor()
        snake[0].setpos(x, y)
        
    if head.eat():
        food.pick_new_location()
        snake.append(Tail(0, 1000, tail_color, "square", 0.8))
        game.update_score()

    for tail in snake:
        if tail != snake[0]:
            head.distance_from(tail)
            if head.bitten_itself():
                game.state = "game over"

sleep(3)

