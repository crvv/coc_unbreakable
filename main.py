__author__ = 'CRVV'

import time

from src.resource import *
from src.game_operate import do_missions
from src.game_operate import produce_army
from src.image_process import get_coordinates
from src.image_process import get_screenshot
from src.trophy import TrophyRecognizer


def _main():
    throw_trophy()
    # recognizer = TrophyRecognizer()
    # print(recognizer.recognize())


def throw_trophy():
    while True:
        do_missions(MISSION_START_GAME)
        # produce_army()
        do_missions(MISSION_THROW_TROPHY)
        do_missions(MISSION_COLLECT_RESOURCE)
        do_missions(MISSION_EXIT_GAME)
        # break
        time.sleep(900)


if __name__ == '__main__':
    _main()
