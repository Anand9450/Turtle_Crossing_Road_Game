import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard


screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing Road Game")
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.go_up,"Up")
game = True
while game:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game = False
            score_board.game_over()
    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()