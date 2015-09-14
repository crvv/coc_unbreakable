__author__ = 'CRVV'

import time

from src.control import Controller
from src.image_process import get_coordinates
from src.image_process import get_screenshot
from src.trophy import TrophyRecognizer
from src.resource import *


controller = Controller(get_screenshot())
trophy_recognizer = TrophyRecognizer()


def do_missions(mission_tuple, base_coordinate=None):
    global controller
    timer = time.clock()
    while True:
        try:
            if time.clock() - timer > 300:
                restart_bluestacks()
            if mission_tuple is not MISSION_EXCEPTION:
                controller = Controller(get_screenshot())
                do_missions(MISSION_EXCEPTION)
            for m in mission_tuple:
                if mission(m, base_coordinate):
                    controller = Controller(get_screenshot())
        except BreakMissions:
            break
        except LoopDone:
            timer = time.clock()
            while True:
                controller = Controller(get_screenshot())
                if get_coordinates(SHOP_BUTTON):
                    break
                if time.clock() - timer > 20:
                    break
            trophies = trophy_recognizer.recognize()
            print('{} trophies'.format(trophies))
            if 0 < trophies < TROPHY_TARGET:
                break
        except GameException as game_exception:
            if game_exception.args[0] == EXCEPTION_FOR_EXCEPTION_LOOP:
                raise GameException(EXCEPTION_FOR_MAIN_LOOP)
            else:
                do_missions(MISSION_START_GAME)
                do_missions(mission_tuple, base_coordinate)
                break


def restart_bluestacks():
    global controller
    while get_coordinates(BLUESTACKS_EXIT_BUTTON):
        controller = Controller(get_screenshot())
        click_points_by_name(BLUESTACKS_EXIT_BUTTON)
    time.sleep(1)
    while not get_coordinates(BLUESTACKS_EXIT_BUTTON):
        controller = Controller(get_screenshot())
        if get_coordinates(START_BLUESTACKS):
            controller.click(get_coordinates(START_BLUESTACKS)[0], click_times=2)
        time.sleep(10)
    raise GameException(EXCEPTION_FOR_MAIN_LOOP)


def mission(name, base_coordinate=None):
    if name is PUT_ARMY:
        if get_coordinates(END_BATTLE_BUTTON):
            choose_troop(TROOPS_FOR_THROW_TROPHY)
            click_points([PUT_ARMY_POINTS])
            time.sleep(0.5)
            return True
    elif name in (RESOURCE_DARK_ELIXIR, RESOURCE_ELIXIR, RESOURCE_GOLD):
        if not get_coordinates(ZOOM_OUT_RIGHT):
            raise GameException(EXCEPTION_FOR_MAIN_LOOP)
        click_points(get_coordinates(name), number=6)
    elif name is BARRACKS_LV10:  # need base_coordinate
        return click_points(base_coordinate)
    elif name is BARRACKS_BARBARIAN:
        return click_points(get_coordinates(name), hold_time=3)
    elif name is BARRACKS_CLOSE_BUTTON:
        if click_points_by_name(name):
            raise LoopDone
    elif name is RETURN_HOME_BUTTON:
        if click_points_by_name(name):
            time.sleep(1)
            raise LoopDone
    elif name is ZOOM_OUT_RIGHT:
        if get_coordinates(ZOOM_OUT_RIGHT):
            raise BreakMissions
        elif get_coordinates(SHOP_BUTTON):
            controller.zoom_out()
    elif name is EXIT_CONFIRM_BUTTON:
        if click_points_by_name(name):
            raise BreakMissions
    elif name is BREAK:
        raise BreakMissions
    elif name in MISSION_EXCEPTION:
        if click_points_by_name(name):
            raise GameException(EXCEPTION_FOR_EXCEPTION_LOOP)
    else:
        return click_points_by_name(name)


def choose_troop(troops):
    for troop in troops:
        if click_points_by_name(troop):
            return True


def click_points_by_name(name):
    return click_points(get_coordinates(name))


def click_points(coordinates, number=1, hold_time=0):
    if coordinates:
        for coordinate in coordinates:
            controller.click(coordinate, hold_time)
            time.sleep(0.5)
            number -= 1
            if number < 1:
                break
        return True
    else:
        return False


def produce_army():
    global controller
    while True:
        controller = Controller(get_screenshot())
        barracks_coordinates = get_coordinates(BARRACKS_LV10)
        if len(barracks_coordinates) >= BARRACKS_NUMBER:
            break
    for coordinate in barracks_coordinates[:4]:
        do_missions(MISSION_PRODUCE_ARMY, [coordinate])
        controller.click_blank()
