from gpiozero import MCP3008, DistanceSensor 
from time import sleep 
from datetime import datetime

pot = MCP3008(7)
ultrasonic = DistanceSensor (echo = 21, trigger = 20)
file = open("D:/Users/Aruzhan/Desktop/distance_log.txt", "w")