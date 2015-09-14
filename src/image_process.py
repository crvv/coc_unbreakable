__author__ = 'CRVV'

import cv2
import numpy
from PIL import Image
from PIL import ImageGrab
from numpy import array

from src.control import Controller
from src.resource import *


def get_coordinates(point_name):
    if point_name is BARRACKS_LV10:
        coordinates = match_color(point_name, 0.8)
    elif point_name is RESOURCE_DARK_ELIXIR:
        coordinates = match_color(point_name, 0.7)
    elif point_name is RESOURCE_ELIXIR:
        coordinates = match_color(point_name, 0.6)
    elif point_name is RESOURCE_GOLD:
        coordinates = match_color(point_name, 0.5)
    else:
        coordinates = match_grey(point_name)
    if coordinates:
        print(point_name, coordinates)
    return coordinates


def match_grey(file_name, corner=False):
    img_gray = cv2.imread(SCREENSHOT, 0)
    template_gray = cv2.imread(file_name, 0)
    w, h = template_gray.shape[::-1]

    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    loc = numpy.where(res >= 0.95)
    result = list()
    for pt in zip(*loc[::-1]):
        if corner:
            result.append((pt[0] + w, pt[1] + h))
        else:
            result.append((pt[0] + w / 2, pt[1] + h / 2))
    # print(file_name, result)
    return result


def match_color(file_name, threshold=0.9):
    img = cv2.imread(SCREENSHOT)
    template = cv2.imread(file_name)
    img = cv2.split(img)
    template = cv2.split(template)
    res = 0
    for pic in zip(img, template):
        w, h = pic[1].shape[::-1]
        res += cv2.matchTemplate(pic[0], pic[1], cv2.TM_CCOEFF_NORMED)
    res /= 3

    loc = numpy.where(res >= threshold)
    result = list()

    for pt in zip(*loc[::-1]):
        result.append((pt[0] + w / 2, pt[1] + h / 2))
    # print(file_name, result)
    return del_duplicate(result)


def get_screenshot():
    screen_image = ImageGrab.grab()
    image_file = open(SCREENSHOT, 'wb')
    screen_image.save(image_file)
    image_file.close()

    bottom_right = match_grey(BLUESTACKS_EXIT_BUTTON, corner=True)
    if not bottom_right:
        return 0, 0
    bottom_right = bottom_right[0]
    box = (bottom_right[0] - SCREEN_SIZE[0], bottom_right[1] - SCREEN_SIZE[1],
           bottom_right[0], bottom_right[1])
    Image.open(SCREENSHOT).crop(box).save(SCREENSHOT)
    return array(bottom_right) - array(SCREEN_SIZE)


def del_duplicate(result):
    i = 1
    while not i >= len(result):
        diff = abs(result[i][0] - result[i-1][0]) + abs(result[i][1] - result[i-1][1])
        if diff < 4:
            del result[i]
        else:
            i += 1
    return result
