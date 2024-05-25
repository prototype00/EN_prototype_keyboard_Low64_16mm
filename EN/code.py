import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.layers import Layers


keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP16,board.GP17,board.GP18,board.GP19,board.GP20,board.GP21,board.GP22,board.GP23,board.GP24,board.GP26,board.GP27,board.GP28,board.GP7,board.GP9,board.GP11,)
keyboard.row_pins = (board.GP10,board.GP8,board.GP6,board.GP12,board.GP13,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

CH = KC.MO(1)

keyboard.keymap = [
    # base layer
    [
    KC.ESC,  KC.N1,   KC.N2,   KC.N3,  KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.N1,   KC.MINS, KC.EQL,  KC.GRV,
    KC.TAB,  KC.Q,    KC.W,    KC.E,   KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSPC, KC.NO,
    KC.LCTL, KC.A,    KC.S,    KC.D,   KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.NO,   KC.NO,
    KC.LSFT, KC.Z,    KC.X,    KC.C,   KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.PSLS, KC.NO,   KC.UP,   KC.NO,   KC.NO,
    CH,      KC.RGUI, KC.CAPS, KC.NO,  KC.LALT, KC.SPC,  KC.SPC,  KC.RALT, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.LEFT, KC.DOWN, KC.RGHT,
    ],

    # Change layer
    [
    KC.TRNS, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.EQL,  KC.GRV,
    KC.TRNS, KC.A,    KC.A,    KC.A,    KC.R,    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSPC, KC.NO,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.SCLN, KC.QUOT, KC.ENT,  KC.NO,   KC.NO,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.PSLS, KC.NO,   KC.UP,   KC.NO,   KC.NO,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.LEFT, KC.DOWN, KC.RGHT,
    ],
]

if __name__ == '__main__':
    keyboard.go()

