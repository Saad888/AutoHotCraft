import tkinter as tk
from .widgets.hotkey_widget import HotkeyWidget
from .widgets.time_widget import TimeWidget


class MainBody:
    def __init__(self, event_craft, event_inturrupt, key_translator):
        self.root = tk.Tk()
        self.root.withdraw()
        
        # Core Variables
        self.key_translator = key_translator

        # State Variables
        self.button_state = 0  # 0 - Idle, 1 - Crafting, 2 - Finishing sequence

        # Event connections
        self.event_craft = event_craft
        self.event_inturrupt = event_inturrupt


    def start(self):
        # Checkbox and instance Variables:
        self.root.deiconify()
        self.check_macro_1 = tk.IntVar(self.root)
        self.check_macro_2 = tk.IntVar(self.root)
        self.check_macro_3 = tk.IntVar(self.root)
        self.check_food = tk.IntVar(self.root)
        self.check_pot = tk.IntVar(self.root)
        self.check_collect = tk.IntVar(self.root)

        # Establish all style settings used for widgets
        self.default_style = {
            'font': ("Helvetica", 14), 
            'bg': "purple",
            'fg': "white"
        }
        self.style_hk_default = {
            'font': ("Helvetica", 14), 
            'width': 24
        }
        self.style_hk_inactive = {"bg": "blue"}
        self.style_hk_active = {"bg": "red"}
        self.style_hk_enabled = {"bg": "yellow"}
        self.styles_hk = (self.style_hk_default, self.style_hk_inactive, 
                          self.style_hk_active, self.style_hk_enabled)
        self.style_timer_default = {
            'font': ("Helvetica", 14), 
            'width': 2
        }
        self.style_timer_inactive = {"bg": "blue"}
        self.style_timer_active = {"bg": "red"}
        self.styles_timer = (self.style_timer_default, 
                             self.style_timer_inactive, 
                             self.style_timer_active)


        # Create all body components and launch the main loop

        # Frames
        self.fr_title = tk.Frame(self.root)  # Frame for title
        self.fr_selection = tk.Frame(self.root)  # Frame for profiles (EMPTY)
        self.fr_body = tk.Frame(self.root, bg='purple')  # Frame for macros and hotkeys
        self.fr_footer = tk.Frame(self.root, bg='purple')

        # ********* Title *********
        self.title_label = tk.Label(
            self.fr_title, 
            text="AutoHotCraft", 
            font=("Helvetica", 25), 
            bg="purple", fg="white"
        )
        self.title_label.pack(side=tk.TOP, fill=tk.X)


        # ********* Profiles *********
        # To be added


        # ********* Main Body *********
        # *** Create Widgets ***

        # Label Headers
        bdy_lbl_name = tk.Label(self.fr_body, text="Name", **self.default_style)
        bdy_lbl_hk = tk.Label(self.fr_body, text="Hotkeys", **self.default_style)
        bdy_lbl_time = tk.Label(self.fr_body, text="Time", **self.default_style)

        # Bodies

        # tuple containing order of body content
        self.body_order = ('Macro 1', 'Macro 2', 'Macro 3', 'Food', 'Potion', 
                           'Craft Window', 'Select/Confirm')  
        kwargs = {
            'frame': self.fr_body,
            'style': self.default_style,
            'hk_settings': self.styles_hk,
            'timer_settings': self.styles_timer,
            'key_trans': self.key_translator, 
            'focus_toggle': self.focus_toggle
        }
        self.body = {
            'Macro 1': WidgetGroup(label="Macro 1", var=self.check_macro_1, 
                                   **kwargs), 
            'Macro 2': WidgetGroup(label="Macro 2", var=self.check_macro_1, 
                                   **kwargs), 
            'Macro 3': WidgetGroup(label="Macro 3", var=self.check_macro_1, 
                                   **kwargs), 
            'Food': WidgetGroup(label="Food", var=self.check_food, **kwargs), 
            'Potion': WidgetGroup(label="Potion", var=self.check_pot, **kwargs),
            'Craft Window': WidgetGroup(label="Craft Window", enabler=False, 
                                        timer=False, **kwargs),
            'Select/Confirm': WidgetGroup(label="Select/Confirm", enabler=False,
                                          timer=False, **kwargs)
        }

        # *** Render Widgets ***
        self.render(bdy_lbl_name, row=0, col=0)
        self.render(bdy_lbl_hk, row=0, col=1, colspan=3)
        self.render(bdy_lbl_time, row=0, col=4)
        for index, group in enumerate(self.body_order):
            row = index + 1
            self.body[group].render_all(row=row)
        

        # ********* Footer *********
        # *** Create Widgets ***
        self.start_btn = tk.Button(self.fr_footer, text="BEGIN", 
                                   bg="blue", fg="yellow", width=10, height=3,
                                   command=self.handler_start_button)

        self.food_max_time = tk.IntVar()
        self.food_radio = [
            tk.Radiobutton(self.fr_footer, 
                           text="30 min", 
                           variable=self.food_max_time, 
                           value=30),
            tk.Radiobutton(self.fr_footer, 
                           text="40 min", 
                           variable=self.food_max_time, 
                           value=40)
        ]
        self.check_button_collect = tk.Checkbutton(
            self.fr_footer, 
            text="Collectable Craft",
            variable=self.check_collect    
        )
        
        # *** Render Widgets ***
        self.render(self.start_btn, rowspan=3)
        self.render(self.food_radio[0], col=2, sticky=tk.W)
        self.render(self.food_radio[1], col=3, sticky=tk.W)
        self.render(self.check_button_collect, row=2, col=1, sticky=tk.W)


        # Assign Events


        # Start root:
        self.fr_title.pack(side=tk.TOP, fill=tk.X)
        self.fr_body.pack(side=tk.TOP, fill=tk.X)
        self.fr_footer.pack(side=tk.TOP, fill=tk.X)
        self.root.mainloop()


    def focus_toggle(self, state):
        """ Toggles tab focus shifting """
        pass


    def render(self, widget, row=0, col=0, colspan=1, rowspan=1, 
               padx=3, pady=0, sticky=tk.W):
        """Simple method to make rendering easier"""
        widget.grid(row=row, column=col, columnspan=colspan, 
                    padx=padx, pady=pady, rowspan=rowspan, sticky=sticky)


    def handler_start_button(self):
        btn = self.start_btn
        if self.button_state == 0:
            self.button_state = 1  # Waiting for complete
            btn.config(text="RUNNING")
            self.begin_craft()
        elif self.button_state == 1:
            self.button_state = 2  # Waiting for complete
            btn.config(text="WAITING")
            self.event_inturrupt()


    def reactivate_system(self):
        self.start_btn.config(text="START")
        self.button_state = 0  



    def begin_craft(self):
        # Constructs all parameters for craft to initate, and commences craft
        macros = []
        macros.append(self.body[0].get())
        if self.check_macro_2.get():
            macros.append(self.body[1].get())
        if self.check_macro_3.get():
            macros.append(self.body[2].get())
        
        if self.check_food.get():
            food_hk, food_rem = self.body[3].get()
            food_time = self.food_max_time.get()
            food = (food_hk, food_rem, food_time)
        else:
            food = None

        if self.check_pot.get():
            potion = self.body[4].get()
        else:
            potion = None

        confirm = self.body[6].entry_hk.get()
        window = self.body[5].entry_hk.get()
        settings = (self.check_food.get() == 1, 
                    self.check_pot.get() == 1, 
                    self.check_collect.get() == 1)

        '''
        print(macros)
        print(food)
        print(potion)
        print(confirm)
        print(window)
        print(settings)
        '''

        self.event_craft(macros, food, potion, confirm, window, settings,
                         self.reactivate_system)



class WidgetGroup:
    def __init__(self, frame=None, label='', style=None, hk_settings=None, 
                 timer=True, timer_settings=None, enabler=True, var=None, 
                 key_trans=None, focus_toggle=None):
        """
        Groups a label with two entries for the body frame
        
        frame: Frame to center the widgets within
        label: Str, name of the group
        style: dictionary passed from parent caller for text formatting
        hk_settings: list of dictionaries with default, inacitve, active, and 
                     enabled display settings
        timer: Bol, if this group has a timer
        keytranslator: Instance of KeyTranslator
        focus_toggle: Focus toggler
        """
        self.label = tk.Label(frame, text=label, **style)
        self.entry_hk = HotkeyWidget(frame, hk_settings[0], hk_settings[1], 
                                     hk_settings[2], hk_settings[3], 
                                     key_trans, focus_toggle)
        if timer:
            self.entry_time = TimeWidget(frame, timer_settings[0], 
                                         timer_settings[1], timer_settings[2])
        else:
            self.entry_time = None
        self.enable = tk.Checkbutton(frame, variable=var) if enabler else None

    def render_all(self, row):
        x = 3
        y = 1
        self.label.grid(row=row, padx=3, pady=0, sticky=tk.E)
        self.entry_hk.grid(row=row, column=1, columnspan=3, padx=x, pady=y)
        if self.entry_time is not None:
            self.entry_time.grid(row=row, column=4, padx=x, pady=y)
        if self.enable is not None:
            self.enable.grid(row=row, column=5, padx=x, pady=y)

    def get(self):
        return (self.entry_hk.get(), int(self.entry_time.get()))


        

if __name__ == '__main__':
    """
    test = MainBody()
    test.start()
    """
    print('import loaded')