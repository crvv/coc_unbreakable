__author__ = 'CRVV'

from PIL import Image
import cv2
import numpy

from src.resource import *
from src.image_process import get_screenshot


class TrophyRecognizer():
    def __init__(self):
        self.numbers_data = list()
        for i in range(10):
            self.numbers_data.append(cv2.imread(NUMBERS_DATA.format(i), -1))
        # print(self.numbers_data[1].shape)

    def recognize(self):
        get_screenshot()
        Image.open(SCREENSHOT).crop(TROPHY_BOX).convert('L').\
            point(lambda xxx: 0 if xxx < 248 else 1, '1').save(TROPHY_SCREENSHOT)
        img = cv2.imread(TROPHY_SCREENSHOT, -1)

        edge = list()
        out_edge = True
        for index, column in enumerate(zip(*img)):
            if out_edge:
                if sum(column):
                    out_edge = False
                    edge.append(index)
            else:
                if not sum(column):
                    out_edge = True
                    edge.append(index)
        numbers = list()
        if len(edge) > 1:
            for number_edge in [edge[x:x+2] for x in range(0, len(edge), 2)]:
                numbers.append(img[:, number_edge[0]:number_edge[1]])

        # for index, number in enumerate(numbers):
        #     cv2.imwrite('number{}.png'.format(index), number)
        # print(len(numbers))

        ans = '0'
        for number in numbers:
            diffs = list()
            for i in range(10):
                diff = image_minus(number, self.numbers_data[i])
                # print(diff)
                diffs.append(diff)
            ans += str(diffs.index(min(diffs)))
        return int(ans)


def image_minus(img1, img2):
    if img1.shape[1] == img2.shape[1]:
        return abs(img1 - img2).sum() / img1.shape[1]
    if img1.shape[1] > img2.shape[1]:
        img1, img2 = img2, img1
    column = img1.shape[1]
    img21 = img2[:, 0:column]
    img22 = img2[:, 1:column+1]
    # print(img21)
    # print(img22)
    ans1 = abs(img1 - img21).sum() / column
    ans2 = abs(img1 - img22).sum() / column
    return min(ans1, ans2)
