import random
import datetime
import sys
import math

def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def funk():
	x = random.randint(0,1)
	if x == 0: 
		for y in range(100):
			if y % 2 == 0:
				print(y, "")
	if x == 1: 
		for y in range(100):
			if y % 2 == 1:
				print(y, "")


def funk2():
	x = random.randint(-10, 10)
	result = math.log(x)
	print(result)
