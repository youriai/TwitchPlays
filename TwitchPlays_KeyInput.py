import time
from pynput.keyboard import Controller, Key

Q = 'q'
W = 'w'
E = 'e'
R = 'r'
T = 't'
Y = 'y'
U = 'u'
I = 'i'
O = 'o'
P = 'p'
A = 'a'
S = 's'
D = 'd'
F = 'f'
G = 'g'
H = 'h'
J = 'j'
K = 'k'
L = 'l'
Z = 'z'
X = 'x'
C = 'c'
V = 'v'
B = 'b'
N = 'n'
M = 'm'

LEFT_ARROW = Key.left
RIGHT_ARROW = Key.right
UP_ARROW = Key.up
DOWN_ARROW = Key.down
ESC = Key.esc
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
ZERO = '0'
MINUS = '-'
EQUALS = '='
BACKSPACE = Key.backspace
APOSTROPHE = '\''
SEMICOLON = ';'
TAB = Key.tab
CAPSLOCK = Key.caps_lock
ENTER = Key.enter
LEFT_CONTROL = Key.ctrl_l
LEFT_ALT = Key.alt_l
LEFT_SHIFT = Key.shift_l
RIGHT_SHIFT = Key.shift_r
TILDE = '`'
PRINTSCREEN = Key.print_screen
NUM_LOCK = Key.num_lock
SPACE = Key.space
DELETE = Key.delete
COMMA = ','
PERIOD = '.'
BACKSLASH = '/'
FORWARDSLASH = '\\'
LEFT_BRACKET = '['
RIGHT_BRACKET = ']'

F1 = Key.f1
F2 = Key.f2
F3 = Key.f3
F4 = Key.f4
F5 = Key.f5
F6 = Key.f6
F7 = Key.f7
F8 = Key.f8
F9 = Key.f9
F10 = Key.f10
F11 = Key.f11
F12 = Key.f12


KEYBOARD = Controller()

def HoldKey(key):
    KEYBOARD.press(key)

def ReleaseKey(key):
    KEYBOARD.release(key)

def HoldAndReleaseKey(key, seconds: float):
    HoldKey(key)
    time.sleep(seconds)
    ReleaseKey(key)
