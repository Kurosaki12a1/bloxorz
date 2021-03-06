#!/usr/bin/python

import sys, pygame

########################################################################################################################
# Map description:
# 1 is putable, 0 is abyss, 4 is goal (So far so well)
# LEVEL_ARRAY = np.array([
# [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
# ])
# State: (x0,y0), (x1,y1)
# Horizontal object: (x, y), (x+1, y) or (x, y), (x, y+1).
# Vertical object: (x,y),(x,y)
# Goal state: isStand and map(y,x) = 4
########################################################################################################################

# LEVEL_ARRAY = np.array([
#     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
#     [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
# ])

import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

LEVEL1_ARRAY = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 4, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
]
LEVEL2_ARRAY = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 2, 1, 0, 0, 1, 4, 1],
    [1, 1, -2, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
]
LEVEL3_ARRAY = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]
LEVEL4_ARRAY = [
    [0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0],
    [0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 5, 5, 5, 5, 5],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 5, 5, 5, 5, 5],
    [0, 0, 0, 0, 0, 1, 4, 1, 0, 0, 5, 5, 1, 5],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 5, 5, 5, 5]
]
LEVEL5_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, -2, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, -2, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, -2],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

LEVEL6_ARRAY = [
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 4, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]
LEVEL7_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 4, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]
LEVEL25_ARRAY = [
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, -2, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 4, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]

LEVEL11_ARRAY = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, -2, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
]

LEVEL12_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 4, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]

LEVEL13_ARRAY = [
    [1, 1, 1, 5, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 5, 5, 5, 1, 4, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 5, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 5, 5, 5, 5, 5, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 5, 5, 1, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0]
]

LEVEL14_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 4, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 2]
]

LEVEL17_ARRAY = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 4, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, -2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]
]

LEVEL18_ARRAY=[
    [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0],
	[1,1,-2,1,0,0,0,1,0,0,0,0,0,0,0],
	[1,1,1,1,1,0,0,1,0,0,0,0,0,0,0],
	[1,10,1,1,1,1,1,1,0,0,1,1,0,0,1],
	[1,1,1,1,1,0,0,0,1,0,0,0,1,0,0],
	[1,1,-2,1,0,0,0,0,1,0,0,0,1,0,0],
	[1,0,0,0,0,0,0,0,-2,0,0,1,1,1,1],
	[1,0,0,0,0,0,0,0,0,0,1,1,1,4,1],
	[1,0,0,2,0,0,0,0,0,0,1,1,1,1,1]
]

LEVEL19_ARRAY = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, -2, 1, 1, 1, 1],
    [1, 4, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2, 1, 1, 1, 0]
]

LEVEL21_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 4, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
]

LEVEL22_ARRAY= [
    [0,0,0,0,0,1,1,0,0,0,0,1,1,1],
	[0,0,0,1,1,1,1,1,1,0,0,1,4,1],
	[1,1,1,1,1,1,-2,1,1,1,1,1,1,1],
	[1,1,1,1,-2,0,0,1,1,1,1,1,0,0],
	[1,1,1,0,0,0,0,0,0,1,1,1,0,0],
	[0,1,0,0,0,0,0,0,0,0,1,0,0,0],
	[0,1,0,0,0,0,0,0,0,0,1,0,0,0],
	[0,1,0,0,0,0,0,0,0,1,1,0,0,0],
	[0,1,1,0,0,0,0,0,0,1,1,0,0,0],
	[0,0,2,0,0,0,0,0,0,2,0,0,0,0]
]

LEVEL27_ARRAY=[
    [1,1,1,0,0,0,0,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1,1,0,0,1,1],
	[1,1,1,0,0,0,0,1,1,0,0,0,0,1,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,1,2,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
	[1,1,1,0,0,5,5,5,5,1,0,0,-2,-2,0],
	[1,4,1,5,5,5,5,5,5,5,0,0,1,1,1],
	[1,1,1,5,5,5,5,5,5,5,5,5,1,1,1],
	[0,0,0,0,0,5,5,5,5,5,5,5,1,1,1],
	[0,0,0,0,0,0,1,1,1,1,0,0,0,0,0]

]

LEVEL29_ARRAY=[
    [0,0,2,1,1,1,0,0,0,1,0,0,2,0,0],
	[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
	[0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
	[-2,0,0,1,1,1,1,1,1,1,1,1,0,0,2],
	[0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
	[0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
	[0,0,0,0,0,0,1,0,0,1,1,1,-2,0,0],
	[1,1,1,0,0,1,1,0,0,1,0,0,0,0,0],
	[1,4,1,0,0,1,0,0,0,1,0,0,0,0,0],
	[1,1,1,0,0,0,0,0,0,1,1,1,-2,0,0]
]

LEVEL30_ARRAY=[
    [0,0,0,1,1,1,1,1,5,5,1,1,1,1,0],
	[0,0,0,1,4,1,1,0,0,0,0,0,5,1,0],
	[0,0,0,1,1,1,0,0,0,0,0,0,5,1,2],
	[0,0,0,0,0,0,0,5,1,1,1,1,1,1,1],
	[0,0,1,0,0,0,0,5,5,0,0,0,0,0,1],
	[0,2,1,5,0,0,0,5,5,0,0,0,0,0,1],
	[5,5,5,5,0,0,0,1,1,0,0,0,0,1,1],
	[5,5,5,1,5,1,5,5,1,5,0,0,2,1,0],
	[1,5,5,5,5,5,5,5,5,5,5,5,1,0,0],
	[0,5,1,5,5,5,0,0,5,5,5,5,1,0,0]
]

LEVEL31_ARRAY=[
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
	[0,1,1,1,0,0,0,0,2,0,0,1,4,1,0],
	[0,1,1,1,1,1,1,1,1,0,0,1,1,1,0],
	[0,1,1,1,0,0,1,1,1,0,0,0,1,0,0],
	[0,5,5,5,0,0,-2,1,1,0,0,0,5,0,0],
	[0,0,5,0,0,0,1,1,1,0,0,5,5,5,0],
	[0,0,1,0,0,0,1,1,1,0,0,1,1,1,0],
	[1,1,1,1,0,0,1,-2,1,1,1,1,1,1,0],
	[1,1,2,1,0,0,2,0,0,0,0,1,1,1,0],
	[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
]
LEVEL32_ARRAY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 2, 1, 1],
    [0, 1, 4, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 2, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
]

LEVEL33_ARRAY=[
    [0,0,0,0,0,1,1,-2,1,1,1,0,0,0,0],
	[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
	[1,1,1,0,0,-2,1,1,-2,1,1,1,1,1,0],
	[1,1,1,1,1,1,1,1,1,-2,-2,1,1,-2,0],
	[0,0,0,0,0,1,1,-2,1,1,-2,1,1,1,0],
	[0,0,0,0,0,1,1,1,1,1,1,-2,1,1,0],
	[1,1,1,0,0,1,1,1,1,1,1,-2,1,1,1],
	[1,4,1,1,1,1,-2,1,0,0,1,1,1,-2,2],
	[1,1,1,0,0,1,1,1,0,0,0,1,1,1,1],
	[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
]


########################################################################################################################
# Function map_copy. (Because python's deepcopy is extremely slow so I implement my own deepcopy)
########################################################################################################################
def map_copy(map):
    return [list(x) for x in map]


########################################################################################################################
# Data structure to store object's place, as well as its previous place and the action (up, down, left, right) to achieve it
# data: tuple (place)
# prev: Node (previous place)
# action: string (up, down, left, right)
# Created: SonPhan 23/04/2018
########################################################################################################################
class Node:
    def __init__(self, data=(0, 0, 0, 0), prev_node=None, action="", map=[], xo_objects_states={}):
        if not ((data[0] < data[2]) or ((data[0] == data[2]) and data[1] < data[3])):
            temp_data = (data[2], data[3], data[0], data[1])
            self.data = temp_data
        else:
            self.data = data
        self.prev_node = prev_node
        self.action = action
        self.map = map_copy(map)
        self.xo_objects_states = dict(xo_objects_states)

    def is_stand(self):
        return self.data[0] == self.data[2] and self.data[1] == self.data[3]


########################################################################################################################

class State:
    def __init__(self, start, board=LEVEL1_ARRAY, xo_objects=None):
        if xo_objects is None:
            xo_objects = []
        self.x0, self.y0, self.x1, self.y1 = start.data
        self.board = map_copy(board)
        self.states = [start]
        self.xo_objects = xo_objects
        self.visited = [start]
        self.start = start

    # self.all_moves = self.next_position()

    ####################################################################################################################
    # Function to find all moves which can be reach from prev_node's move
    ####################################################################################################################
    def next_position(self, prev_node):
        rv = []
        if self.is_stand():
            self.add_move(rv, (self.x0, self.y0 + 1, self.x1, self.y1 + 2), prev_node, "down")
            self.add_move(rv, (self.x0, self.y0 - 1, self.x0, self.y0 - 2), prev_node, "up")
            self.add_move(rv, (self.x0 + 1, self.y0, self.x0 + 2, self.y0), prev_node, "right")
            self.add_move(rv, (self.x0 - 1, self.y0, self.x0 - 2, self.y1), prev_node, "left")
        elif self.x0 == self.x1:
            self.add_move(rv, (self.x0 + 1, self.y0, self.x1 + 1, self.y1), prev_node, "right")
            self.add_move(rv, (self.x0 - 1, self.y0, self.x1 - 1, self.y1), prev_node, "left")
            self.add_move(rv, (self.x0, self.y0 - 1, self.x1, self.y1 - 2), prev_node, "up")
            self.add_move(rv, (self.x0, self.y0 + 2, self.x1, self.y1 + 1), prev_node, "down")
        elif self.y0 == self.y1:
            self.add_move(rv, (self.x0, self.y0 + 1, self.x1, self.y1 + 1), prev_node, "down")
            self.add_move(rv, (self.x0, self.y0 - 1, self.x1, self.y1 - 1), prev_node, "up")
            self.add_move(rv, (self.x0 - 1, self.y0, self.x1 - 2, self.y1), prev_node, "left")
            self.add_move(rv, (self.x0 + 2, self.y0, self.x1 + 1, self.y1), prev_node, "right")
        else:
            return []
        return rv

    def add_move(self, rv, data, prev_node, direction):
        for xo_object in self.xo_objects:
            if (data[0] == xo_object.position[0] and data[1] == xo_object.position[1]) or (
                            data[2] == xo_object.position[0] and data[3] == xo_object.position[1]):
                for m in xo_object.managed_position:
                    if (xo_object.type == XOObject.TYPE_O) or (
                                        xo_object.type == XOObject.TYPE_X and data[0] == data[2] and data[1] == data[
                                3]):
                        if m.type == ManagedPosition.BOTH:
                            xo_objects_states = dict(prev_node.xo_objects_states)
                            xo_objects_states[(m.x, m.y)] = not xo_objects_states[(m.x, m.y)]
                            rv.append(Node(data, prev_node, direction, prev_node.map, xo_objects_states))
                        elif m.type == ManagedPosition.ONLY_ENABLE:
                            xo_objects_states = dict(prev_node.xo_objects_states)
                            xo_objects_states[(m.x, m.y)] = True
                            rv.append(Node(data, prev_node, direction, prev_node.map, xo_objects_states))
                        elif m.type == ManagedPosition.ONLY_DISABLE:
                            xo_objects_states = dict(prev_node.xo_objects_states)
                            xo_objects_states[(m.x, m.y)] = False
                            rv.append(Node(data, prev_node, direction, prev_node.map, xo_objects_states))
                    else:
                        rv.append(Node(data, prev_node, direction, prev_node.map, prev_node.xo_objects_states))
                return
        rv.append(Node(data, prev_node, direction, prev_node.map, prev_node.xo_objects_states))

    ####################################################################################################################
    # Function to check if the object repeated previous move (which could lead to infinite loop)
    # Created: SonPhan 23/04/2018
    ####################################################################################################################
    def notContain(self, node):
        for n in self.visited:
            if n.data[0] == node.data[0] and n.data[1] == node.data[1] and n.data[2] == node.data[2] \
                    and n.data[3] == node.data[3]:
                if n.xo_objects_states == node.xo_objects_states:
                    return False
        return True

    ####################################################################################################################
    # Function to check valid move
    ####################################################################################################################
    # @staticmethod
    def is_valid(self, node):
        height = len(self.board)
        width = len(self.board[0])
        if node.data[0] < 0 or node.data[0] >= width or node.data[1] < 0 or node.data[1] >= height \
                or node.data[2] < 0 or node.data[2] >= width or node.data[3] < 0 or node.data[3] >= height:
            return False
        if node.map[node.data[1]][node.data[0]] == 0 or node.map[node.data[3]][
            node.data[2]] == 0:
            return False
        if node.data[0] == node.data[2] and node.data[1] == node.data[3] and node.map[node.data[1]][node.data[0]] == 5:
            return False
        return True

    def add_state(self, node):
        if self.notContain(node):
            self.visited.append(node)
            self.states.append(node)
            return True
        return False

    def add_valid_state(self, prev_node):
        list_node = self.next_position(prev_node)
        if not list_node:
            return False
        else:
            for node in list_node:
                if self.is_valid(node):
                    self.add_state(node)

    def is_goal(self, x, y):
        return self.board[y][x] == 4

    def is_stand(self):
        return self.x0 == self.x1 and self.y0 == self.y1

    def check_goal(self):
        return self.is_stand() and self.is_goal(self.x0, self.y0)

    def set_player_position(self, node):
        self.x0, self.y0, self.x1, self.y1 = node.data
        for xo_object in self.xo_objects:
            if (self.x0 == xo_object.position[0] and self.y0 == xo_object.position[1]) or (
                            self.x1 == xo_object.position[0] and self.y1 == xo_object.position[1]):
                for m in xo_object.managed_position:
                    if xo_object.type == XOObject.TYPE_O or (xo_object.type == XOObject.TYPE_X and self.is_stand()):
                        if m.type == ManagedPosition.BOTH:
                            node.map[m.y][m.x] = abs(node.map[m.y][m.x] - 1)
                        elif m.type == ManagedPosition.ONLY_ENABLE:
                            node.map[m.y][m.x] = 1
                        elif m.type == ManagedPosition.ONLY_DISABLE:
                            node.map[m.y][m.x] = 0


class XOObject:
    TYPE_O = -1000
    TYPE_X = 1000

    def __init__(self, type, position=(0, 0), managed_position=[]):
        self.type = type
        self.position = position
        self.managed_position = managed_position


class ManagedPosition:
    ONLY_ENABLE = 123
    ONLY_DISABLE = -123
    BOTH = 12

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type


########################################################################################################################
# Function to solve by bfs
########################################################################################################################
def bfs(state):
    # start = time.time()
    current_state = Node
    # BFS operation
    while len(state.states) != 0:

        current_state = state.states.pop(0)
        state.set_player_position(current_state)
        if state.check_goal():
            break
        state.add_valid_state(current_state)
    pointer = current_state
    path = []
    # Backtracking all the previous moves to reach this goal state
    while pointer:
        path.insert(0, pointer)
        pointer = pointer.prev_node
    # And print them out
    for p in path:
        print(p.action)
    return path


def draw_map(screen, node, resolution_width, resolution_height):
    # height = len(map)
    # width = len(map[0])
    # for row in map:
    #     for col in row:
    #         if col == 1:
    #             pygame.draw.rect(screen, WHITE, [30 + rect_size * row.index(col), 30 + rect_size * map.index(row), rect_size, rect_size], 0)
    #             pygame.draw.rect(screen, BLACK, [30 + rect_size * row.index(col), 30 + rect_size * map.index(row), rect_size, rect_size], 1)
    map = node.map
    rect_size = 0
    if resolution_width < resolution_height:
        rect_size = int(resolution_width / 20)
    else:
        rect_size = int(resolution_height / 20)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i == node.data[1] and j == node.data[0]) or (i == node.data[3] and j == node.data[2]):
                pygame.draw.rect(screen, BLUE, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 0)
                pygame.draw.rect(screen, BLACK, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 1)
            elif map[i][j] == 1:
                pygame.draw.rect(screen, WHITE, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 0)
                pygame.draw.rect(screen, BLACK, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 1)
            elif map[i][j] == -2:
                pygame.draw.rect(screen, WHITE, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 0)
                pygame.draw.rect(screen, BLACK, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 1)
                pygame.draw.circle(screen, RED,
                                   [30 + rect_size * j + int(rect_size / 2), 30 + rect_size * i + int(rect_size / 2)],
                                   int(rect_size / 2))
            elif map[i][j] == 2:
                pygame.draw.rect(screen, WHITE, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 0)
                pygame.draw.rect(screen, BLACK, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 1)
                pygame.draw.aaline(screen, RED, [30 + rect_size * j, 30 + rect_size * i],
                                   [30 + rect_size * j + rect_size, 30 + rect_size * i + rect_size], 1)
                pygame.draw.aaline(screen, RED, [30 + rect_size * j, 30 + rect_size * i + rect_size],
                                   [30 + rect_size * j + rect_size, 30 + rect_size * i], 1)
            elif map[i][j] == 5:
                pygame.draw.rect(screen, YELLOW, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 0)
                pygame.draw.rect(screen, BLACK, [30 + rect_size * j, 30 + rect_size * i, rect_size, rect_size], 1)


class Level:
    def __init__(self, state):
        self.state = state


def init_levels():
    levels_array = []
    for i in range(33):
        levels_array.append(None)
    # LEVEL1 SOLVER:
    state1 = State(Node((1, 1, 1, 1), None, "", LEVEL1_ARRAY), LEVEL1_ARRAY)
    levels_array[0] = Level(state1)

    # LEVEL2 SOLVER:
    xo_objects2 = [
        XOObject(XOObject.TYPE_O, (2, 2),
                 [ManagedPosition(4, 4, ManagedPosition.BOTH), ManagedPosition(5, 4, ManagedPosition.BOTH)]),
        XOObject(XOObject.TYPE_X, (8, 1),
                 [ManagedPosition(10, 4, ManagedPosition.BOTH), ManagedPosition(11, 4, ManagedPosition.BOTH)])]
    state2 = State(
        Node((1, 4, 1, 4), None, "", LEVEL2_ARRAY, {(4, 4): False, (5, 4): False, (10, 4): False, (11, 4): False}),
        LEVEL2_ARRAY, xo_objects2)
    levels_array[1] = Level(state2)

    # LEVEL3 SOLVER:
    state3 = State(Node((1, 3, 1, 3), None, "", LEVEL3_ARRAY), LEVEL3_ARRAY)
    levels_array[2] = Level(state3)

    # LEVEL4 SOLVER:
    state4 = State(Node((1, 5, 1, 5), None, "", LEVEL4_ARRAY), LEVEL4_ARRAY)
    levels_array[3] = Level(state4)

    # Level 5 Solver :
    xo_objects5 = [XOObject(XOObject.TYPE_O, (8, 1),
                            [ManagedPosition(5, 1, ManagedPosition.BOTH), ManagedPosition(6, 1, ManagedPosition.BOTH)]),
                   XOObject(XOObject.TYPE_O, (3, 3), [ManagedPosition(5, 8, ManagedPosition.ONLY_ENABLE),
                                                      ManagedPosition(6, 8, ManagedPosition.ONLY_ENABLE)]),
                   XOObject(XOObject.TYPE_O, (6, 5), [ManagedPosition(5, 8, ManagedPosition.ONLY_DISABLE),
                                                      ManagedPosition(6, 8, ManagedPosition.ONLY_DISABLE)]),
                   XOObject(XOObject.TYPE_O, (14, 6), [
                       ManagedPosition(5, 8, ManagedPosition.BOTH), ManagedPosition(6, 8, ManagedPosition.BOTH)])]
    state5 = State(
        Node((13, 1, 13, 1), None, "", LEVEL5_ARRAY, {(5, 1): True, (6, 1): True, (5, 8): True, (6, 8): True}),
        LEVEL5_ARRAY, xo_objects5)
    levels_array[4] = Level(state5)

    # LEVEL6 SOLVER:
    state6 = State(Node((0, 3, 0, 3), None, "", LEVEL6_ARRAY), LEVEL6_ARRAY)
    levels_array[5] = Level(state6)

    # LEVEL7 SOLVER
    xo_objects7 = [XOObject(XOObject.TYPE_X, (9, 4), [ManagedPosition(3, 6, ManagedPosition.BOTH)])]
    state7 = State(Node((1, 3, 1, 3), None, "", LEVEL7_ARRAY, {(3, 6): False}), LEVEL7_ARRAY, xo_objects7)
    levels_array[6] = Level(state7)

    # LEVEL25 SOLVER
    xo_objects25 = [XOObject(XOObject.TYPE_O, (4, 2),
                             [ManagedPosition(8, 4, ManagedPosition.BOTH), ManagedPosition(9, 4, ManagedPosition.BOTH),
                              ManagedPosition(13, 2, ManagedPosition.BOTH),
                              ManagedPosition(13, 3, ManagedPosition.BOTH)]), XOObject(XOObject.TYPE_X, (2, 6), [
        ManagedPosition(8, 4, ManagedPosition.ONLY_ENABLE), ManagedPosition(9, 4, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_O, (8, 8), [ManagedPosition(4, 6, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(5, 6, ManagedPosition.ONLY_DISABLE),
                                                       ManagedPosition(7, 3, ManagedPosition.ONLY_ENABLE)])]
    state25 = State(Node((1, 7, 1, 7), None, "", LEVEL25_ARRAY,
                         {(4, 6): True, (5, 6): True, (7, 3): False, (8, 4): False, (9, 4): False, (13, 2): False,
                          (13, 3): False}),
                    LEVEL25_ARRAY, xo_objects25)
    levels_array[24] = Level(state25)

    # Level 11 Solver :
    xo_objects11 = [XOObject(XOObject.TYPE_O, (6, 6),
                             [ManagedPosition(4, 0, ManagedPosition.ONLY_DISABLE),
                              ManagedPosition(4, 1, ManagedPosition.ONLY_DISABLE)])]
    state11 = State(Node((0, 5, 0, 5), None, "", LEVEL11_ARRAY, {(4, 0): True, (4, 1): True}),
                    LEVEL11_ARRAY, xo_objects11)

    levels_array[10] = Level(state11)

    # Level 12 Solver :
    xo_objects12 = [XOObject(XOObject.TYPE_X, (6, 2),
                             [ManagedPosition(12, 2, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (12, 0), [ManagedPosition(6, 4, ManagedPosition.BOTH)])]
    state12 = State(Node((2, 6, 2, 6), None, "", LEVEL12_ARRAY, {(12, 2): False, (6, 4): False}),
                    LEVEL12_ARRAY, xo_objects12)

    levels_array[11] = Level(state12)

    # LEVEL13 SOLVER:
    state13 = State(Node((12, 3, 12, 3), None, "", LEVEL13_ARRAY), LEVEL13_ARRAY)
    levels_array[12] = Level(state13)

    # LEVEL14 SOLVER:
    xo_objects14 = [XOObject(XOObject.TYPE_X, (12, 3),
                             [ManagedPosition(1, 2, ManagedPosition.BOTH),
                              ManagedPosition(2, 2, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (13, 9),
                             [ManagedPosition(1, 3, ManagedPosition.BOTH),
                              ManagedPosition(2, 3, ManagedPosition.BOTH)])]
    state14 = State(
        Node((4, 2, 4, 2), None, "", LEVEL14_ARRAY, {(1, 2): False, (2, 2): False, (1, 3): False, (2, 3): False}),
        LEVEL14_ARRAY, xo_objects14)
    levels_array[13] = Level(state14)

    # LEVEL17 SOLVER:
    xo_objects17 = [XOObject(XOObject.TYPE_O, (1, 8),
                             [ManagedPosition(8, 7, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (12, 3), [ManagedPosition(6, 6, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_X, (13, 3), [ManagedPosition(6, 6, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 6), [ManagedPosition(7, 2, ManagedPosition.ONLY_ENABLE)]),
                    XOObject(XOObject.TYPE_X, (12, 9), [ManagedPosition(8, 7, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(9, 1, ManagedPosition.ONLY_ENABLE)])]
    state17 = State(Node((1, 1, 1, 1), None, "", LEVEL17_ARRAY,
                         {(1, 8): False, (8, 7): False, (6, 6): False, (7, 2): False, (8, 7): False, (9, 1): False}),
                    LEVEL17_ARRAY, xo_objects17)
    levels_array[16] = Level(state17)

    # LEVEL18 SOLVER:
    xo_objects18 = [XOObject(XOObject.TYPE_O, (7, 0),
                           [ManagedPosition(8, 3, ManagedPosition.ONLY_ENABLE),
                            ManagedPosition(9, 3, ManagedPosition.ONLY_ENABLE)]), XOObject(XOObject.TYPE_O, (2, 1), [
        ManagedPosition(12, 3, ManagedPosition.ONLY_DISABLE), ManagedPosition(13, 3, ManagedPosition.ONLY_DISABLE),
        ManagedPosition(1, 8, ManagedPosition.ONLY_DISABLE), ManagedPosition(2, 8, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_O, (1, 3), [ManagedPosition(8, 3, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(9, 3, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_O, (2, 5), [ManagedPosition(12, 3, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(13, 3, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(1, 8, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(2, 8, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_O, (8, 6), [ManagedPosition(12, 3, ManagedPosition.ONLY_ENABLE),
                                                     ManagedPosition(13, 3, ManagedPosition.ONLY_ENABLE),
                                                     ManagedPosition(1, 8, ManagedPosition.ONLY_ENABLE),
                                                     ManagedPosition(2, 8, ManagedPosition.ONLY_ENABLE)]),
                  XOObject(XOObject.TYPE_X, (3, 8), [ManagedPosition(5, 4, ManagedPosition.BOTH)])]
    state18 = State(Node((2, 3, 2, 3), None, "", LEVEL18_ARRAY,
                       {(8, 3): False, (9, 3): False, (12, 3): False, (13, 3): False, (1, 8): False, (2, 8): False,
                        (5, 4): False}),
                  LEVEL18_ARRAY, xo_objects18)

    levels_array[17] = Level(state18)

    # LEVEL19 SOLVER:
    xo_objects19 = [XOObject(XOObject.TYPE_O, (10, 0),
                             [ManagedPosition(7, 5, ManagedPosition.BOTH),
                              ManagedPosition(8, 5, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_O, (10, 5), [ManagedPosition(9, 2, ManagedPosition.ONLY_DISABLE),
                                                        ManagedPosition(9, 3, ManagedPosition.ONLY_DISABLE)]),
                    XOObject(XOObject.TYPE_O, (10, 9), [ManagedPosition(9, 2, ManagedPosition.ONLY_ENABLE),
                                                        ManagedPosition(9, 3, ManagedPosition.ONLY_ENABLE)])]
    state19 = State(
        Node((1, 0, 1, 0), None, "", LEVEL19_ARRAY, {(7, 5): False, (8, 5): False, (9, 2): True, (9, 3): True}),
        LEVEL19_ARRAY, xo_objects19)
    levels_array[18] = Level(state19)

    # LEVEL21 SOLVER:
    xo_objects21 = [XOObject(XOObject.TYPE_X, (8, 5),
                             [ManagedPosition(3, 9, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (8, 6), [ManagedPosition(5, 7, ManagedPosition.BOTH)])]
    state21 = State(Node((1, 3, 1, 3), None, "", LEVEL21_ARRAY, {(3, 9): False, (5, 7): False}),
                    LEVEL21_ARRAY, xo_objects21)
    levels_array[20] = Level(state21)

    # LEVEL22 SOLVER:
    xo_objects22 = [XOObject(XOObject.TYPE_O, (6, 2),
                           [ManagedPosition(2, 7, ManagedPosition.ONLY_DISABLE),
                            ManagedPosition(12, 3, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_O, (4, 3), [ManagedPosition(2, 7, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_X, (2, 9), [ManagedPosition(12, 3, ManagedPosition.BOTH)]),
                  XOObject(XOObject.TYPE_X, (9, 9), [ManagedPosition(2, 7, ManagedPosition.BOTH)])]
    state22 = State(Node((1, 3, 1, 3), None, "", LEVEL22_ARRAY, {(2, 7): False, (12, 3): False}),
                  LEVEL22_ARRAY, xo_objects22)
    levels_array[21] = Level(state22)

    # LEVEL27 SOLVER:
    xo_objects27 = [XOObject(XOObject.TYPE_X, (13, 3),
                           [ManagedPosition(6, 9, ManagedPosition.ONLY_DISABLE),
                            ManagedPosition(9, 9, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_O, (12, 5), [ManagedPosition(6, 9, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_O, (13, 5), [ManagedPosition(9, 9, ManagedPosition.ONLY_DISABLE)])]
    state27 = State(Node((1, 1, 1, 1), None, "", LEVEL27_ARRAY, {(6, 9): True, (9, 9): True}),
                  LEVEL27_ARRAY, xo_objects27)
    levels_array[26] = Level(state27)

    # LEVEL29 SOLVER:
    xo_objects29 = [XOObject(XOObject.TYPE_O, (2, 0),
                           [ManagedPosition(10, 0, ManagedPosition.ONLY_ENABLE),
                            ManagedPosition(11, 0, ManagedPosition.ONLY_ENABLE),
                            ManagedPosition(10, 6, ManagedPosition.ONLY_DISABLE),
                            ManagedPosition(11, 6, ManagedPosition.ONLY_DISABLE)]), XOObject(XOObject.TYPE_X, (12, 0), [
        ManagedPosition(5, 5, ManagedPosition.ONLY_ENABLE), ManagedPosition(6, 5, ManagedPosition.ONLY_ENABLE)]),
                  XOObject(XOObject.TYPE_X, (0, 3), [ManagedPosition(3, 8, ManagedPosition.ONLY_ENABLE),
                                                     ManagedPosition(4, 8, ManagedPosition.ONLY_ENABLE),
                                                     ManagedPosition(10, 9, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(11, 9, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_X, (14, 3), [ManagedPosition(3, 9, ManagedPosition.ONLY_ENABLE)]),
                  XOObject(XOObject.TYPE_O, (12, 6), [ManagedPosition(1, 3, ManagedPosition.ONLY_ENABLE),
                                                      ManagedPosition(2, 3, ManagedPosition.ONLY_ENABLE)]),
                  XOObject(XOObject.TYPE_O, (12, 9), [ManagedPosition(3, 0, ManagedPosition.ONLY_DISABLE),
                                                      ManagedPosition(4, 0, ManagedPosition.ONLY_DISABLE),
                                                      ManagedPosition(10, 0, ManagedPosition.ONLY_DISABLE),
                                                      ManagedPosition(11, 0, ManagedPosition.ONLY_DISABLE),
                                                      ManagedPosition(12, 1, ManagedPosition.ONLY_ENABLE),
                                                      ManagedPosition(13, 1, ManagedPosition.ONLY_ENABLE),
                                                      ManagedPosition(10, 6, ManagedPosition.ONLY_DISABLE),
                                                      ManagedPosition(11, 6, ManagedPosition.ONLY_DISABLE)])]

    state29 = State(Node((7, 3, 7, 3), None, "", LEVEL29_ARRAY,
                       {(1, 3): False, (2, 3): False, (10, 6): True, (11, 6): True, (10, 9): True, (11, 9): True,
                        (5, 5): False, (5, 6): False, (3, 8): False, (4, 8): False, (10, 0): False, (11, 0): False,
                        (3, 9): False, (3, 0): True, (4, 0): True, (12, 1): False, (13, 1): False}), LEVEL29_ARRAY,
                  xo_objects29)
    levels_array[28] = Level(state29)

    # LEVEL30 SOLVER:
    xo_objects30 = [XOObject(XOObject.TYPE_X, (14, 2),
                           [ManagedPosition(10, 3, ManagedPosition.ONLY_DISABLE),
                            ManagedPosition(11, 3, ManagedPosition.ONLY_ENABLE),
                            ManagedPosition(9, 6, ManagedPosition.ONLY_ENABLE),
                            ManagedPosition(12, 6, ManagedPosition.ONLY_ENABLE)]), XOObject(XOObject.TYPE_X, (1, 5), [
        ManagedPosition(10, 3, ManagedPosition.ONLY_ENABLE), ManagedPosition(11, 3, ManagedPosition.ONLY_ENABLE)]),
                  XOObject(XOObject.TYPE_X, (12, 7), [ManagedPosition(14, 7, ManagedPosition.BOTH)])]
    state30 = State(Node((2, 4, 2, 4), None, "", LEVEL30_ARRAY,
                       {(10, 3): True, (11, 3): True, (9, 6): False, (12, 6): False, (14, 7): False}), LEVEL30_ARRAY,
                  xo_objects30)
    levels_array[29] = Level(state30)

    # LEVEL31 SOLVER:
    xo_objects31 = [XOObject(XOObject.TYPE_X, (8, 1),
                           [ManagedPosition(9, 2, ManagedPosition.BOTH), ManagedPosition(10, 2, ManagedPosition.BOTH)]),
                  XOObject(XOObject.TYPE_O, (6, 4), [ManagedPosition(4, 2, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(5, 2, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(9, 2, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(10, 2, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(5, 7, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(9, 7, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(10, 7, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_O, (7, 7), [ManagedPosition(4, 2, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(5, 2, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(9, 2, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(10, 2, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(5, 7, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(9, 7, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(10, 7, ManagedPosition.ONLY_DISABLE)]),
                  XOObject(XOObject.TYPE_X, (2, 8), [ManagedPosition(4, 2, ManagedPosition.ONLY_DISABLE),
                                                     ManagedPosition(14, 0, ManagedPosition.ONLY_ENABLE),
                                                     ManagedPosition(14, 1, ManagedPosition.ONLY_ENABLE),
                                                     ManagedPosition(14, 2, ManagedPosition.ONLY_ENABLE)]),
                  XOObject(XOObject.TYPE_X, (6, 8),
                           [ManagedPosition(4, 7, ManagedPosition.BOTH), ManagedPosition(5, 7, ManagedPosition.BOTH)])]
    state31 = State(Node((12, 7, 12, 7), None, "", LEVEL31_ARRAY,
                       {(9, 7): True, (10, 7): True, (4, 2): True, (5, 2): True, (9, 2): False, (10, 2): False,
                        (4, 7): False, (5, 7): False, (14, 0): False, (14, 1): False, (14, 2): False}), LEVEL31_ARRAY,
                  xo_objects31)
    levels_array[30] = Level(state31)

    # LEVEL32 SOLVER:
    xo_objects32 = [XOObject(XOObject.TYPE_X, (13, 0),
                             [ManagedPosition(4, 1, ManagedPosition.BOTH), ManagedPosition(5, 1, ManagedPosition.BOTH),
                              ManagedPosition(2, 7, ManagedPosition.BOTH),
                              ManagedPosition(3, 7, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (11, 2),
                             [ManagedPosition(2, 8, ManagedPosition.BOTH),
                              ManagedPosition(3, 8, ManagedPosition.BOTH)]),
                    XOObject(XOObject.TYPE_X, (5, 7),
                             [ManagedPosition(4, 2, ManagedPosition.BOTH),
                              ManagedPosition(5, 2, ManagedPosition.BOTH)])]
    state32 = State(Node((10, 6, 10, 6), None, "", LEVEL32_ARRAY,
                         {(4, 1): True, (5, 1): True, (2, 7): False, (3, 7): False, (2, 8): False, (3, 8): False,
                          (4, 2): False, (5, 2): False}), LEVEL32_ARRAY, xo_objects32)
    levels_array[31] = Level(state32)

    # LEVEL33 SOLVER:
    xo_objects33 = [XOObject(XOObject.TYPE_O, (7, 0),
                           [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE), ManagedPosition(4, 7,
                                                                                                 ManagedPosition.ONLY_DISABLE)]), XOObject(
        XOObject.TYPE_O, (5, 2), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                  ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]), XOObject(XOObject.TYPE_O,
                                                                                                  (8, 2), [
                                                                                                      ManagedPosition(3,
                                                                                                                      7,
                                                                                                                      ManagedPosition.ONLY_DISABLE),
                                                                                                      ManagedPosition(4,
                                                                                                                      7,
                                                                                                                      ManagedPosition.ONLY_DISABLE)]), XOObject(
        XOObject.TYPE_O, (9, 3), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                  ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]), XOObject(XOObject.TYPE_O,
                                                                                                  (13, 3), [
                                                                                                      ManagedPosition(3,
                                                                                                                      7,
                                                                                                                      ManagedPosition.ONLY_DISABLE),
                                                                                                      ManagedPosition(4,
                                                                                                                      7,
                                                                                                                      ManagedPosition.ONLY_DISABLE)]), XOObject(
        XOObject.TYPE_O, (7, 4), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                  ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]), XOObject(XOObject.TYPE_O,
                                                                                                  (10, 4), [
                                                                                                      ManagedPosition(3,
                                                                                                                      7,
                                                                                                                      ManagedPosition.ONLY_DISABLE),
                                                                                                      ManagedPosition(4,
                                                                                                                      7,
                                                                                                                      ManagedPosition.ONLY_DISABLE)]), XOObject(
        XOObject.TYPE_O, (11, 5), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                   ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]), XOObject(XOObject.TYPE_O,
                                                                                                   (11, 6), [
                                                                                                       ManagedPosition(
                                                                                                           3, 7,
                                                                                                           ManagedPosition.ONLY_DISABLE),
                                                                                                       ManagedPosition(
                                                                                                           4, 7,
                                                                                                           ManagedPosition.ONLY_DISABLE)]), XOObject(
        XOObject.TYPE_O, (13, 7), [ManagedPosition(3, 7, ManagedPosition.ONLY_DISABLE),
                                   ManagedPosition(4, 7, ManagedPosition.ONLY_DISABLE)]), XOObject(XOObject.TYPE_X,
                                                                                                   (14, 7), [
                                                                                                       ManagedPosition(
                                                                                                           11, 1,
                                                                                                           ManagedPosition.ONLY_ENABLE)])]
    state33 = State(Node((1, 3, 1, 3), None, "", LEVEL33_ARRAY,
                       {(3, 7): True, (4, 7): True, (11, 1): False}), LEVEL33_ARRAY, xo_objects33)
    levels_array[32] = Level(state33)

    return levels_array


def main():
    levels_array = init_levels()
    level_choice = int(input("Nhap level: "))
    if levels_array[level_choice - 1] is None:
        print("Chua lam level nay :v")
        return

    done = False
    path = bfs(levels_array[level_choice - 1].state)
    pygame.init()
    pygame.display.set_caption("Bloxorz")

    resolution_height = pygame.display.Info().current_h
    resolution_width = pygame.display.Info().current_w

    screen = pygame.display.set_mode((resolution_width, resolution_height))
    i = 0
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if i < len(path) - 1:
                        i += 1
                elif event.key == pygame.K_LEFT:
                    if i > 0:
                        i -= 1
        screen.fill(GREEN)

        draw_map(screen, path[i], resolution_width, resolution_height)
        pygame.display.flip()


main()

