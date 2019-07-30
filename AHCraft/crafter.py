import time
import threading
import AHKManager from AHKManager


class Crafter:
    def __init__(self, AHKObj):
        """ This loop will run the expected sequence of actions required 
        to craft based on requested parameters"""

        # Parameters for system 
        self.active = False
        self.user_inturrupt = False
        self.script = AHKObj

        # Parameters for hotkeys and timers
        self.macros = []  # Tuple with command + time (str, int)
        self.food_timer = 30  # Default
        self.hk_food = None
        self.hk_consumable = None
        self.hk_confirm = None


    def update_keybinds(self, macros, food, pot, confirm):
        """ Update all keybinds internally 
        macros: list of tuple (hotkey: str, timer: int)
        food: tuple (hotkey: str, timer: int)
        pot: str with hotkey
        confirm: str with hotkey        
        """
        self.macros = macros
        self.food_timer = food[1]
        self.hk_food = food[0]
        self.hk_consumable = pot
        self.hk_confirm = confirm


    def start(self):
        """ Begins separate thread for crafting loop """
        threading.Thread(target=mainloop).start()


    def mainloop(self):
        """ Runs the main crafting loop """
        self.active = True

        while self.active:
            # Main looper
            pass


    def run_sequence(self, sequence):
        """ Runs the sequence, provided in a list in the form (hotkey, timer) """
        for hotkey, wait in sequence:
            


