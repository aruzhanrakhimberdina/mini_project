from gpiozero import MCP3008, DistanceSensor 
from time import sleep 
from datetime import datetime

pot = MCP3008(7)
ultrasonic = DistanceSensor (echo = 21, trigger = 20)
file = open("D:/Users/Aruzhan/Desktop/distance_log.txt", "w")

while True:
    dist = ultrasonic.distance * 100
    span = pot.value * 100
    dist, span = round (dist, 3), round (span, 3)

file.close()