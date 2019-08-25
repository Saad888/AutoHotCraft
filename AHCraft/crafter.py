import time
from AHKManager import AHKManager


class Crafter:
    def __init__(self, AHKObj):
        """ This loop will run the expected sequence of actions required 
        to craft based on requested parameters"""

        # Parameters for system 
        self.user_inturrupt = False
        self.script = AHKObj
    

    def update(self, macros, food, pot, confirm, window, escape, settings, 
               UIUpdate):
        """ Update all keybinds internally 
        macros: list of tuple (hotkey: str, timer: int)
        food: tuple (hotkey: str, remaining: int, timer: int)
        pot: tuple (hotkey: str, remaining: int)
        confirm: str with hotkey      
        window: str with crafting window hotkey  
        settings: Tuple of three Bol values:
            (use_food, use_pot, use_collect)
        UIUpdate: Callback function to place message on UI
        """

        # Counters:
        self.craft_count = 1
        self.total_time = 0
        self.food_used = 0
        self.pots_used = 0


        self.macros = macros
        self.use_food, self.use_pot, self.use_collect = settings

        self.hk_food = food[0] if self.use_food else None
        self.food_remains = food[1] if self.use_food else None
        self.food_timer = food[2] if self.use_food else None

        self.hk_pot = pot[0] if self.use_pot else None
        self.pot_remains = pot[1] if self.use_pot else None
        self.pot_timer = 15

        self.hk_craft = window
        self.hk_confirm = confirm
        self.hk_escape = escape

        
        # Sequences Update:
        self.sq_craft = []
        for macro in self.macros:
            self.sq_craft.append((macro[0], macro[1] + 1))  # Add 1 second buffer
        
        # Start the craft
        self.sq_begin_craft = [
            (self.hk_confirm, 1), 
            (self.hk_confirm, 1), 
            (self.hk_confirm, 2)
        ]

        # End Craft (from end of craft)
        self.sq_end_craft = []
        if self.use_collect:
            self.sq_end_craft.append((confirm, 1))
        self.sq_end_craft.append((confirm, 3))

        # Exit Craft (from crafting window)
        self.sq_exit_craft = [
            (self.hk_escape, 2)
        ]

        # Food and pots
        self.sq_food = [(self.hk_food, 4)]
        self.sq_pot = [(self.hk_pot, 3)]

        # Restart Craft
        self.sq_restart_craft = [
            (self.hk_craft, 1), 
            (self.hk_confirm, 1), 
            (self.hk_confirm, 1), 
            (self.hk_confirm, 1), 
            (self.hk_confirm, 2)
        ]

        self.UI_update = UIUpdate


    def start(self, args):
        """ Updates parameters and Begins separate thread for crafting loop """
        self.update(*args)
        self.mainloop()

    def mainloop(self):
        """ Runs the main crafting loop """
        loop_time = time.perf_counter()
        loop_start = loop_time
        self.user_inturrupt = False

        food_remains = self.food_remains * 60 if self.use_food else None
        pot_remains = self.pot_remains * 60 if self.use_pot else None
        refresh_food, refresh_pot = False, False

        macro_time = 0
        for macro in self.macros:
            macro_time += macro[1]

        while self.user_inturrupt is False:
            # Main looper
            sequence = []
            sequence += self.macros  # Add crafting macros to sequence
            sequence += self.sq_end_craft
            UI_text = f"Craft number {self.craft_count} ...\n"

            # Sets food timers
            # If food or pots need to be refreshed, do so, else start next craft
            if self.use_food:
                food_remains -= (time.perf_counter() - loop_time)
                refresh_food = food_remains - (macro_time + 15) < 60
                UI_text += f'Food: ~{food_remains / 60:0.2f} min remains'
                UI_text += ', refreshing after craft' if refresh_food else ''
                UI_text += '\n'
            if self.use_pot:
                pot_remains -= (time.perf_counter() - loop_time)
                refresh_pot = pot_remains - (macro_time + 15) < 60
                UI_text += f'Pot: ~{pot_remains / 60:0.2f} min remains'
                UI_text += ', refreshing after craft' if refresh_pot else ''
                UI_text += '\n'
            
            if refresh_food or refresh_pot:
                sequence += self.sq_exit_craft
                if refresh_food:
                    sequence += self.sq_food
                    food_remains = self.food_timer * 60 + macro_time
                if refresh_pot:
                    sequence += self.sq_pot
                    pot_remains = self.pot_timer * 60 + macro_time
                sequence += self.sq_restart_craft
            else:
                sequence += self.sq_begin_craft

            loop_time = time.perf_counter()
            self.UI_update(UI_text)
            self.run_sequence(sequence)


            self.total_time = time.perf_counter() - loop_start
            if self.user_inturrupt is False: 
                self.craft_count += 1
                self.food_used += 1 if refresh_food else 0
                self.pots_used += 1 if refresh_pot else 0
            if self.user_inturrupt is True:
                mins = int(self.total_time / 60)
                secs = int(self.total_time - (mins * 60))
                UI_text = f"{self.craft_count} crafts complete "
                UI_text += f"in {mins}:{secs:02d} minutes\n"
                if self.use_food:
                    UI_text += f"{self.food_used} food consumed\n"
                if self.use_pot:
                    UI_text += f"{self.pots_used} pots consumed\n"
                self.UI_update(UI_text)



    def run_sequence(self, sequence):
        """ Runs the sequence, provided in a list in the form (hotkey, timer)"""
        for hotkey, wait in sequence:
            print(f'Execute {hotkey} with delay {wait}s')
            self.script.execute(hotkey)
            for i in range(wait):
                time.sleep(1)
                if self.user_inturrupt is True: 
                    break
            if self.user_inturrupt is True: 
                break



if __name__ == "__main__":
    print('Starting test')
    AHK = AHKManager("C:\\Program Files\\AutoHotkey\\AutoHotkey.exe")
    tester = Crafter(AHK)
    tester.start(
        macros=[("{1}", 3), ("{2}", 3), ("{3}", 3)], 
        food=None, 
        pot=None, 
        confirm='{C}', 
        window='{W}', 
        settings=(False, False, False)
    )

""" Update all keybinds internally 
macros: list of tuple (hotkey: str, timer: int)
food: tuple (hotkey: str, remaining: int, timer: int)
pot: tuple (hotkey: str, remaining: int)
confirm: str with hotkey      
window: str with crafting window hotkey  
settings: Tuple of three Bol values:
    (use_food, use_pot, use_collect)
"""