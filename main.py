from basic_functions import *
from solver import solver
import sys
import cv2
import numpy as np
from PIL import Image, ImageGrab
import pyautogui
from time import time, sleep

def color(x, y):
    return colors.index([img[y, x][i] for i in range(3)])

#               white        green        red           blue         orange        yellow
colors = [[255, 255, 255], [0, 221, 0], [255, 0, 0], [0, 0, 255], [255, 170, 0], [255, 255, 0]]
inspection_commands = [['y'], ['q'], ['q'], ['q'], ['q', 'y'], ['y', 'y']]
strt_x = 1270
strt_y = 213
end_x = 1616
end_y = 440
dx = (end_x - strt_x) // 2
dy = (end_y - strt_y) // 2
coords = []
for y in range(3):
    for x in range(3):
        coords.append((dx * x, dy * y))

s = ''
while True:
    #s = input()
    if s == 'exit':
        break
    sleep(3)
    pyautogui.press('space')
    sleep(1)
    print('start inspection')
    stickers = []
    for face in range(6):
        img = np.array(ImageGrab.grab(bbox=(strt_x, strt_y, end_x + 1, end_y + 1)))
        pyautogui.press(inspection_commands[face])
        for x, y in coords:
            stickers.append(color(x, y))
        sleep(0.2)
    strt = time()
    solution = solver(stickers)
    print('solution found in ', time() - strt, 'sec')
    print('len is', len(solution))
    solution_str = ''.join(''.join(j for j in twists_key[i]) for i in solution)
    print('len of type is', len(solution_str))
    pyautogui.typewrite(solution_str)
    print('done')
    print('')
