import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP8,
        board.GP7,
        board.GP6,
        board.GP5,
        board.GP4,
        board.GP3,
        board.GP2,
    )
    row_pins = (
        board.GP15,
        board.GP14,
        board.GP13,
        board.GP12,
        board.GP11,
        board.GP10,
        board.GP9,
    )

    # OLED
    SCL = board.GP27
    SDA = board.GP26
    
    diode_orientation = DiodeOrientation.COL2ROW
    
    # Reversed from left
    uart_rx = board.GP0
    uart_tx = board.GP1

    coord_mapping = [
        0,  1,  2,  3,  4,  5,  6,             55, 54, 53, 52, 51, 50, 49,
        7,  8,  9,  10, 11, 12, 13,            62, 61, 60, 59, 58, 57, 56,
        14, 15, 16, 17, 18, 19, 20,            69, 68, 67, 66, 65, 64, 63,
        21, 22, 23, 24, 25, 26, 27,            76, 75, 74, 73, 72, 71, 70,
        28, 29, 30, 31, 32, 33, 34,            83, 82, 81, 80, 79, 78, 77,
                    36, 37, 38, 39, 40, 41,                    86, 85,
                                    47, 48,    90, 89, 88, 87, 
    ]

    # coord_mapping = [
    #     6,  5,  4,  3,  2,  1,  0,
    #     13, 12, 11, 10, 9,  8,  7,
    #     20, 19, 18, 17, 16, 15, 14,
    #     27, 26, 25, 24, 23, 22, 21,
    #     34, 33, 32, 31, 30, 29, 28,
    #             37, 36,
    #     41, 40, 39, 38, 
    # ]
    