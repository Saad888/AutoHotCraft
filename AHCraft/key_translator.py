""" Series of methods to translate between AHK and AHC text for hotkeys"""


class KeyTranslator:
    def __init__(self):
        # Codes in the form [dec] = (display name, AHK code, modifier)
        self.codes = {
            -1: ("", "", False),
            8: ("BackSpace", "{vk08}", False),
            9: ("Tab", "{vk09}", False),
            13: ("Enter", "{vk0D}", False),
            16: ("Shift", "+", True),
            17: ("Ctrl", "^", True),
            18: ("Alt", "!", True),
            19: ("Pause", "{vk13}", False),
            20: ("Caps Lock", "{vk14}", False),
            27: ("ESC", "{vk1B}", False),
            32: ("Space", "{vk20}", False),
            33: ("Page Up", "{vk21}", False),
            34: ("Page Down", "{vk22}", False),
            35: ("End", "{vk23}", False),
            36: ("Home", "{vk24}", False),
            37: ("Left", "{vk25}", False),
            38: ("Up", "{vk26}", False),
            39: ("Right", "{vk27}", False),
            40: ("Down", "{vk28}", False),
            45: ("Insert", "{vk2D}", False),
            46: ("Delete", "{vk2E}", False),
            48: ("0", "{vk30}", False),
            49: ("1", "{vk31}", False),
            50: ("2", "{vk32}", False),
            51: ("3", "{vk33}", False),
            52: ("4", "{vk34}", False),
            53: ("5", "{vk35}", False),
            54: ("6", "{vk36}", False),
            55: ("7", "{vk37}", False),
            56: ("8", "{vk38}", False),
            57: ("9", "{vk39}", False),
            65: ("A", "{vk41}", False),
            66: ("B", "{vk42}", False),
            67: ("C", "{vk43}", False),
            68: ("D", "{vk44}", False),
            69: ("E", "{vk45}", False),
            70: ("F", "{vk46}", False),
            71: ("G", "{vk47}", False),
            72: ("H", "{vk48}", False),
            73: ("I", "{vk49}", False),
            74: ("J", "{vk4A}", False),
            75: ("K", "{vk4B}", False),
            76: ("L", "{vk4C}", False),
            77: ("M", "{vk4D}", False),
            78: ("N", "{vk4E}", False),
            79: ("O", "{vk4F}", False),
            80: ("P", "{vk50}", False),
            81: ("Q", "{vk51}", False),
            82: ("R", "{vk52}", False),
            83: ("S", "{vk53}", False),
            84: ("T", "{vk54}", False),
            85: ("U", "{vk55}", False),
            86: ("V", "{vk56}", False),
            87: ("W", "{vk57}", False),
            88: ("X", "{vk58}", False),
            89: ("Y", "{vk59}", False),
            90: ("Z", "{vk5A}", False),
            96: ("Numpad 0", "{vk60}", False),
            97: ("Numpad 1", "{vk61}", False),
            98: ("Numpad 2", "{vk62}", False),
            99: ("Numpad 3", "{vk63}", False),
            100: ("Numpad 4", "{vk64}", False),
            101: ("Numpad 5", "{vk65}", False),
            102: ("Numpad 6", "{vk66}", False),
            103: ("Numpad 7", "{vk67}", False),
            104: ("Numpad 8", "{vk68}", False),
            105: ("Numpad 9", "{vk69}", False),
            106: (" Numpad *", "{vk6A}", False),
            107: ("Numpad  +", "{vk6B}", False),
            109: (" Numpad -", "{vk6D}", False),
            110: ("Numpad .", "{vk6E}", False),
            111: (" Numpad /", "{vk6F}", False),
            112: ("F1", "{vk70}", False),
            113: ("F2", "{vk71}", False),
            114: ("F3", "{vk72}", False),
            115: ("F4", "{vk73}", False),
            116: ("F5", "{vk74}", False),
            117: ("F6", "{vk75}", False),
            118: ("F7", "{vk76}", False),
            119: ("F8", "{vk77}", False),
            120: ("F9", "{vk78}", False),
            121: ("F10", "{vk79}", False),
            122: ("F11", "{vk7A}", False),
            123: ("F12", "{vk7B}", False),
            144: (" Numlock", "{vk90}", False),
            145: ("Scroll Lock", "{vk91}", False),
            186: (" ;", "{vkBA}", False),
            187: (" =", "{vkBB}", False),
            188: (",", "{vkBC}", False),
            189: (" -", "{vkBD}", False),
            190: (" .", "{vkBE}", False),
            191: (" /", "{vkBF}", False),
            192: (" `", "{vkC0}", False),
            219: (" [", "{vkDB}", False),
            220: (" \\", "{vkDC}", False),
            221: (" ]", "{vkDD}", False),
            222: (" '", "{vkDE}", False)
        }
        # Translating for numpad inputs
        self.numpad_keys = {
            12: 101, 
            33: 105, 
            34: 99, 
            35: 97, 
            36: 103, 
            37: 100, 
            38: 104, 
            39: 102, 
            40: 98
        }

    def _key_value_return(self, keycode, index):
        if keycode in self.codes:
            return self.codes[keycode][index]

    def key_name(self, keycode):
        return self._key_value_return(keycode, 0)

    def key_ahk(self, keycode):
        return self._key_value_return(keycode, 1)

    def key_mod(self, keycode):
        return self._key_value_return(keycode, 2)

    def keycode(self, keycode, state):
        """ Translates numpad inputs to be correct """
        if keycode in self.numpad_keys and state < 0x40000:
            return self.numpad_keys[keycode]
        return keycode