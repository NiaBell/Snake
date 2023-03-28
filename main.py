from turtle import Screen, Turtle

import scoreboard
from Snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#need to append new object coordinates to segments.

snake = Snake()
food = Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
   screen.update()
   time.sleep(0.1)

   snake.move()


#detect collision with food

   if snake.head.distance(food) < 15:
      food.refresh()
      snake.extend()
      scoreboard.scored()

   #detect collision with wall

   if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
      scoreboard.game_over()
      game_is_on=False

   #detect collision with tail
      #trigger game over

   for segment in snake.segments[1:]:
      if snake.head.distance(segment)<15:
         game_is_on=False
         scoreboard.game_over()
screen.exitonclick()