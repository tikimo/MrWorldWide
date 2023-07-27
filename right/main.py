import board 

from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard = KMKKeyboard()

keyboard.debug_enabled = True

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())

# SPLIT (BLE not supported on Circuitpython yet with PICO W, however, Micropython does support it)
split = Split(
    data_pin=board.GP1,
    debug_enabled=True,
)
keyboard.modules.append(split)

keyboard.keymap = [
    [   #0
        KC.ESC,   KC.F1,    KC.F2,   KC.F3,   KC.F4,   KC.F5,     KC.F6,                            KC.F7,     KC.F8,     KC.F9,     KC.F10,    KC.F11,    KC.F12,    KC.PGUP,
        KC.TRNS,  KC.N1,    KC.N2,   KC.N3,   KC.N4,   KC.N5,     KC.N6,                            KC.N7,     KC.N8,     KC.N9,     KC.N0,     KC.SLSH,   KC.GRAVE,  KC.PGDN,
        KC.TAB,   KC.Q,     KC.W,    KC.E,    KC.R,    KC.T,      KC.Y,                             KC.U,      KC.I,      KC.O,      KC.P,      KC.A,      KC.CIRC,   KC.TRNS,
        KC.LSFT,  KC.A,     KC.S,    KC.D,    KC.F,    KC.G,      KC.H,                             KC.J,      KC.K,      KC.L,      KC.O,      KC.A,      KC.ASTR,   KC.TRNS,
        KC.LCTL,  KC.LABK,  KC.Z,    KC.X,    KC.C,    KC.V,      KC.B,                             KC.N,      KC.M,      KC.COMMA,  KC.DOT,    KC.SCLN,   KC.RSFT,   KC.TRNS,
                                     KC.LCBR, KC.RCBR, KC.LSFT,   KC.SPC,  KC.MB_LMB,  KC.MB_RMB,                         KC.LALT,   KC.DEL,
                                                                           KC.LGUI,    KC.TRNS,     KC.SPC,    KC.ENTER,  KC.BSPC,   KC.DEL
    ],
]

oled_ext = Oled(
    views=OledData(
        corner_one={0:OledReactionType.STATIC, 1:["layer"]},
        corner_two={0:OledReactionType.LAYER, 1:["1","2","3","4"]},
        corner_three={0:OledReactionType.LAYER, 1:["base","raise","lower","adjust"]},
        corner_four={0:OledReactionType.LAYER, 1:["qwerty","nums","shifted","leds"]},
    ),
    toDisplay=OledDisplayMode.TXT,
    oWidth=128,
    oHeight=32,
    flip=True,
)
keyboard.extensions.append(oled_ext)


if __name__ == '__main__':
    keyboard.go()
