#! /usr/env/python3

import math

p = 0

def pressure():
	print("Program will count pressure in a glass under chosen conditions.")
	press = float(input("Enter atmospheric pressure[bar]: "))
	height = float(input("Enter height[m]: "))
	temp = float(input("Enter temperature[K]: "))
	if height >= 0:
		p = press * math.exp(-0.003417 - height / temp)
		print(f"Pressure equals to {format(p, '.2f')}")
	else:
		p = press - 0.09682 * height
		print(f"Pressure ewuals to {format(p, '.2f')}")
pressure()
