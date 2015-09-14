__author__ = 'CRVV'

BACK_BUTTON = 'resource/android_back_button.png'
NO_RESPONSE = 'resource/android_no_response.png'
RELOAD_BUTTON = 'resource/android_reload_button.png'
TRY_AGAIN_BUTTON = 'resource/android_try_again_button.png'
BLUESTACKS_AD = 'resource/bluestacks_ad.png'
BLUESTACKS_EXIT_BUTTON = 'resource/bluestacks_exit_button.png'
BLUESTACKS_WINDOW_BUTTON = 'resource/bluestacks_window_button.png'
APP_ICON = 'resource/coc_app_icon.png'
ATTACK_BUTTON = 'resource/coc_attack_button.png'
BARRACKS_BARBARIAN = 'resource/coc_barracks_barbarian.png'
BARRACKS_LV10 = 'resource/coc_barracks_lv10.png'
BARRACKS_TRAIN_TROOPS_BUTTON = 'resource/coc_barracks_train_troops_button.png'
BARRACKS_CLOSE_BUTTON = 'resource/coc_close_button.png'
DISABLE_SHIELD = 'resource/coc_disable_shield_button.png'
END_BATTLE_BUTTON = 'resource/coc_end_battle_button.png'
EXIT_CONFIRM_BUTTON = 'resource/coc_exit_confirm_button.png'
FIND_OPPONENT_BUTTON = 'resource/coc_find_opponent_button.png'
RESOURCE_DARK_ELIXIR = 'resource/coc_resource_dark_elixir_bubble.png'
RESOURCE_ELIXIR = 'resource/coc_resource_elixir_bubble.png'
RESOURCE_GOLD = 'resource/coc_resource_gold_bubble.png'
RETURN_HOME_BUTTON = 'resource/coc_return_home_button.png'
SHOP_BUTTON = 'resource/coc_shop_button.png'
START_GAME_RETURN_BUTTON = 'resource/coc_start_game_return_home_button.png'
SURRENDER_BUTTON = 'resource/coc_surrender_button.png'
SURRENDER_OKAY_BUTTON = 'resource/coc_surrender_okay_button.png'
TROOPS_ARCHER = 'resource/coc_troops_archer.png'
TROOPS_BARBARIAN = 'resource/coc_troops_barbarian.png'
TROOPS_KING = 'resource/coc_troops_king.png'
TROOPS_QUEEN = 'resource/coc_troops_queen.png'
TROPHY_ICON = 'resource/coc_trophy_icon.png'
ZOOM_OUT_RIGHT = 'resource/coc_zoom_out_right_down_corner.png'

SCREENSHOT = 'working/screenshot.png'
TROPHY_SCREENSHOT = 'working/trophy.png'
NUMBERS_DATA = 'resource/numbers/number-{}.png'

START_BLUESTACKS = 'resource/start_bluestacks.png'

PRODUCE_BARBARIAN = 'mission_produce_barbarian'
BARRACKS_NUMBER = 1

SCREEN_SIZE = (800, 600)
PUT_ARMY_POINTS = (559, 437)
BLANK_POINT = (679, 477)
ZOOM_DRAG_START_POINT = (679, 377)
ZOOM_DRAG_END_POINT = (679, 477)
TROPHY_BOX = (48, 65, 94, 75)

PUT_ARMY = 'put_army'
BREAK = 'break_missions'
EXCEPTION_FOR_MAIN_LOOP = 'exception_for_main_loop'
EXCEPTION_FOR_EXCEPTION_LOOP = 'exception_for_exception_loop'

TROPHY_TARGET = 236

MISSION_PRODUCE_ARMY = (BARRACKS_LV10,
                        BARRACKS_TRAIN_TROOPS_BUTTON,
                        BARRACKS_BARBARIAN,
                        BARRACKS_CLOSE_BUTTON,
                        BREAK)

MISSION_THROW_TROPHY = (ATTACK_BUTTON,
                        FIND_OPPONENT_BUTTON,
                        DISABLE_SHIELD,
                        PUT_ARMY,
                        SURRENDER_BUTTON,
                        SURRENDER_OKAY_BUTTON,
                        RETURN_HOME_BUTTON)

MISSION_EXIT_GAME = (EXIT_CONFIRM_BUTTON,
                     BACK_BUTTON)

MISSION_START_GAME = (APP_ICON,
                      START_GAME_RETURN_BUTTON,
                      ZOOM_OUT_RIGHT)

MISSION_COLLECT_RESOURCE = (RESOURCE_DARK_ELIXIR,
                            RESOURCE_GOLD,
                            RESOURCE_ELIXIR,
                            BREAK)

TROOPS_FOR_THROW_TROPHY = (TROOPS_KING,
                           TROOPS_QUEEN,
                           TROOPS_BARBARIAN,
                           TROOPS_ARCHER)

MISSION_EXCEPTION = (RELOAD_BUTTON,
                     NO_RESPONSE,
                     TRY_AGAIN_BUTTON,
                     BLUESTACKS_AD,
                     BREAK)


class BreakMissions(Exception):
    pass


class LoopDone(Exception):
    pass


class GameException(Exception):
    pass


# class WindowMoved(Exception):
#     def __init__(self, bottom_right):
#         Exception.__init__(self)
#         self.bottom_right = bottom_right
