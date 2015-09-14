__author__ = 'CRVV'

import time
from numpy import array

from pymouse import PyMouse
from pykeyboard import PyKeyboard

from src.resource import *


mouse = PyMouse()
keyboard = PyKeyboard()


class Controller():
    def __init__(self, top_left):
        self.corner = top_left

    def click(self, coordinate, hold_time=0, click_times=1):
        if not coordinate:
            return
        coordinate = array(coordinate)
        coordinate += self.corner
        x_orig, y_orig = mouse.position()

        for _ in range(click_times):
            time.sleep(0.05)
            mouse.press(*coordinate)
            time.sleep(hold_time)
            mouse.release(*coordinate)

        mouse.move(x_orig, y_orig)

    def click_blank(self, times=2):
        for _ in range(times):
            self.click(BLANK_POINT)
            time.sleep(0.2)

    def zoom_out(self):
        x_orig, y_orig = mouse.position()

        self.click_blank()
        keyboard.tap_key(keyboard.down_key, 8, 0.5)

        start = self.corner + array(ZOOM_DRAG_START_POINT)
        end = self.corner + array(ZOOM_DRAG_END_POINT)
        self.drag(start, end)
        self.click_blank()

        mouse.move(x_orig, y_orig)

    @staticmethod
    def drag(start, end):
        # print(start, end)
        mouse.press(*start)
        while abs(mouse.position()[0] - end[0]) > 20 or abs(mouse.position()[1] - end[1]) > 20:
            if abs(mouse.position()[0] - end[0]) > 12:
                p = mouse.position()
                d = (end[0] - p[0]) / abs(end[0] - p[0])
                mouse.move(int(p[0] + 10 * d), int(p[1]))
            if abs(mouse.position()[1] - end[1]) > 12:
                p = mouse.position()
                d = (end[1] - p[1]) / abs(end[1] - p[1])
                mouse.move(int(p[0]), int(p[1] + 10 * d))
            time.sleep(0.05)
        mouse.release(*end)
