""" Series of methods to translate between AHK and AHC text for hotkeys"""


class Translator:
    def translate(self, origin):
        """ Origin in the form: MOD + KEY """
        part = origin.split(' + ')
        part[0] = part[0].replace('SHIFT', '+')
        part[0] = part[0].replace('CRTL', '^')
        part[0] = part[0].replace('ALT', '!')

        