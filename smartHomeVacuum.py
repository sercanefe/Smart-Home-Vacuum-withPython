#!/usr/bin/env python
from roomrider_lib.roomrider import Robot
import time

robot = Robot("roomrider")
time.sleep(0.1)

#Your code starts here



dil = input("Choose your language (Eng or Tr)")

if dil == "Tr":
    print("DirtRider ile odanızı temizleyelim")
    isimRobot = input("Robotunuzunu adını ne koymak istersiniz?")

    while robot.is_ok():
        robot.move_forward()
        robot.turn_right()
        robot.move_forward()
        robot.move_forward()
        robot.move_forward()
        robot.turn_right()
        robot.move_forward()
        robot.turn_right()

    print("{} yorulmuş:) Biraz dinlenmek istiyor.".format(isimRobot))

else:
    print("Let's clean your room with DirtRider")
    nameRobot = input("What would you like to name your robot?")

    while robot.is_ok():
        robot.move_forward()
        robot.turn_right()
        robot.move_forward()
        robot.move_forward()
        robot.move_forward()
        robot.turn_right()
        robot.move_forward()
        robot.turn_right()

    print("{} is tired:) He wants to get some rest.".format(nameRobot))