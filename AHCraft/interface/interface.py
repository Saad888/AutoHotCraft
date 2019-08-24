import tkinter as tk
from tkinter.messagebox import showerror
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

        # Create List of widgets which can take focus:
        self.widget_focus = []

    def start(self):
        # Checkbox and instance Variables:
        self.root.deiconify()
        self.check_macro_1 = tk.IntVar(self.root)
        self.check_macro_2 = tk.IntVar(self.root)
        self.check_macro_3 = tk.IntVar(self.root)
        self.check_food = tk.IntVar(self.root)
        self.check_pot = tk.IntVar(self.root)
        self.check_collect = tk.IntVar(self.root)
        self.profile = tk.StringVar(self.root)

        # Establish all style settings used for widgets
        background_color = 'purple'
        foreground_color = 'white'
        color_inactive = '#2200FF'
        color_active = '#626DFF'
        color_enabled = '#FFFF66'

        self.default_style = {
            'font': ("Helvetica", 14), 
            'bg': background_color,
            'fg': foreground_color
        }
        self.default_style_lab = {
            'font': ("Helvetica", 12), 
            'bg': background_color,
            'fg': foreground_color
        }
        self.default_style_small = {
            'font': ("Helvetica", 12), 
            'bg': background_color,
            'activebackground': background_color
        }
        self.style_hk_default = {
            'font': ("Helvetica", 14), 
            'width': 24
        }
        self.style_hk_inactive = {"bg": color_inactive}
        self.style_hk_active = {"bg": color_active}
        self.style_hk_enabled = {"bg": color_enabled}
        self.styles_hk = (self.style_hk_default, self.style_hk_inactive, 
                          self.style_hk_active, self.style_hk_enabled)
        self.style_timer_default = {
            'font': ("Helvetica", 14), 
            'width': 2
        }
        self.style_timer_inactive = {"bg": color_inactive}
        self.style_timer_active = {"bg": color_enabled}
        self.styles_timer = (self.style_timer_default, 
                             self.style_timer_inactive, 
                             self.style_timer_active)


        # Create all body components and launch the main loop

        # Frames
        self.fr_title = tk.Frame(self.root)  # Frame for title
        self.fr_selection = tk.Frame(self.root)  # Frame for profiles (EMPTY)
        self.fr_body = tk.Frame(self.root, bg=background_color)  # Frame for macros and hotkeys
        self.fr_footer = tk.Frame(self.root, bg=background_color)

        # ********* Title *********
        self.title_label = tk.Label(
            self.fr_title, 
            text="AutoHotCraft", 
            font=("Helvetica", 25), 
            bg=background_color, fg=foreground_color
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
                           'Craft Window', 'Select/Confirm', 'Exit Menus')  
        kwargs = {
            'frame': self.fr_body,
            'style': self.default_style,
            'hk_settings': self.styles_hk,
            'timer_settings': self.styles_timer,
            'key_trans': self.key_translator, 
            'focus_toggle': self.focus_toggle, 
            'enable_settings': self.default_style_small
        }
        self.body = {
            'Macro 1': WidgetGroup(label="Macro 1", enabler=False, 
                                   time_label="sec", **kwargs), 
            'Macro 2': WidgetGroup(label="Macro 2", var=self.check_macro_2, 
                                   time_label="sec", **kwargs), 
            'Macro 3': WidgetGroup(label="Macro 3", var=self.check_macro_3, 
                                   time_label="sec", **kwargs), 
            'Food': WidgetGroup(label="Food", var=self.check_food, **kwargs), 
            'Potion': WidgetGroup(label="Potion", var=self.check_pot, **kwargs),
            'Craft Window': WidgetGroup(label="Craft Window", enabler=False, 
                                        timer=False, **kwargs),
            'Select/Confirm': WidgetGroup(label="Select/Confirm", enabler=False,
                                          timer=False, **kwargs),
            'Exit Menus': WidgetGroup(label="Exit Menus", enabler=False, 
                                      timer=False, **kwargs)
        }
        self.body['Exit Menus'].entry_hk.set_hotkey(27, [])

        for group in self.body.values():
            self.widget_focus.append(group.entry_hk.widget)
            if group.entry_time:
                self.widget_focus.append(group.entry_time.widget)
            if group.enable:
                self.widget_focus.append(group.enable)

        # *** Render Widgets ***
        self.render(bdy_lbl_name, row=0, col=0)
        self.render(bdy_lbl_hk, row=0, col=1, colspan=3)
        self.render(bdy_lbl_time, row=0, col=4, colspan=3)
        for index, group in enumerate(self.body_order):
            row = index + 1
            self.body[group].render_all(row=row)
        

        # ********* Footer *********
        # *** Create Widgets ***
        self.start_btn = tk.Button(self.fr_footer, text="BEGIN", 
                                   bg="blue", fg="yellow", width=10, height=3,
                                   command=self.handler_start_button)
        self.widget_focus.append(self.start_btn)

        self.food_max_time = tk.IntVar()
        self.food_radio = [
            tk.Radiobutton(self.fr_footer, 
                           variable=self.food_max_time, 
                           value=30, 
                           **self.default_style_small),
            tk.Radiobutton(self.fr_footer, 
                           variable=self.food_max_time, 
                           value=40, 
                           **self.default_style_small)
        ]
        self.widget_focus.append(self.food_radio[0])
        self.widget_focus.append(self.food_radio[1])
        self.food_radio_label = [
            tk.Label(self.fr_footer, text="30 min", **self.default_style_lab), 
            tk.Label(self.fr_footer, text="40 min", **self.default_style_lab)
        ]

        # Profile
        self.profile_select = tk.OptionMenu(self.fr_footer, self.profile, 
                                            "Select a Profile")
        self.profile_select['menu'].add_command(
            label="A", command=tk._setit(self.profile, 'A')
        )
        self.profile_select["highlightthickness"] = 0
        self.profile_select.config(**self.default_style_lab)
        self.widget_focus.append(self.profile_select)


        self.check_button_collect = tk.Checkbutton(
            self.fr_footer, 
            variable=self.check_collect, 
            **self.default_style_small   
        )
        self.widget_focus.append(self.check_button_collect)
        self.check_button_label = tk.Label(
            self.fr_footer,
            text="Collectable Craft", 
            **self.default_style_lab
        )
        
        # *** Render Widgets ***
        self.render(self.start_btn, rowspan=3)
        self.render(self.food_radio[0], col=1,)
        self.render(self.food_radio[1], col=1, row=2)
        self.render(self.food_radio_label[0], col=1, padx=22, sticky=tk.W)
        self.render(self.food_radio_label[1], col=1, padx=22, row=2, sticky=tk.W)
        self.render(self.check_button_collect, col=2, sticky=tk.W)
        self.render(self.check_button_label, col=2, padx=25)
        self.render(self.profile_select, col=3, colspan=2, padx=0)


        # Assign Events


        # Start root:
        self.fr_title.pack(side=tk.TOP, fill=tk.X)
        self.fr_body.pack(side=tk.TOP, fill=tk.X)
        self.fr_footer.pack(side=tk.TOP, fill=tk.X)
        self.root.mainloop()


    def focus_toggle(self, state):
        """ Toggles tab focus shifting """
        for widget in self.widget_focus:
            widget.config(takefocus=state)


    def render(self, widget, row=0, col=0, colspan=1, rowspan=1, 
               padx=3, pady=0, sticky=tk.W):
        """Simple method to make rendering easier"""
        widget.grid(row=row, column=col, columnspan=colspan, 
                    padx=padx, pady=pady, rowspan=rowspan, sticky=sticky)


    def handler_start_button(self):
        """ Handle button between two states """
        btn = self.start_btn
        if self.button_state == 0:
            check, args = self.prepare_craft()
            if check:
                self.button_state = 1  # FIX THIS
                btn.config(text="RUNNING")
                self.event_craft(self.reactivate_system, args)
            else:
                showerror("Error", args)
        elif self.button_state == 1:
            self.button_state = 2  # Waiting for complete
            btn.config(text="WAITING")
            self.event_inturrupt()
               


    def reactivate_system(self):
        self.start_btn.config(text="START")
        self.button_state = 0  


    def prepare_craft(self):
        # Constructs all parameters for craft to initate, and commences craft
        # Returns true if all parameters checked correctly
        # Returns false otherwise

        # Collect Macro Data
        macros = []
        macros.append(self.body['Macro 1'].get())
        if self.check_macro_2.get():
            macros.append(self.body['Macro 2'].get())
        if self.check_macro_3.get():
            macros.append(self.body['Macro 3'].get())
        
        # Check Macro:
        for hotkey, timer in macros:
            if hotkey == '':
                return (False, "Please enter valid hotkeys for the enabled macros.")
            if timer == 0:
                return (False, "Please enter a time in seconds for the enabled macros.")

        if self.check_food.get():
            food_hk, food_rem = self.body['Food'].get()
            food_time = self.food_max_time.get()
            food = (food_hk, food_rem, food_time)
            if food_hk == '':
                return (False, "Pleasae enter a valid hotkey for food.")
            if food_time == 0:
                return (False, "Please select how long the food will last for.")
        else:
            food = None

        if self.check_pot.get():
            potion = (self.body['Potion'].entry_hk.get_ahk_code(), 
                      self.body['Potion'].entry_time.get_time())
            if potion[0] == '':
                return (False, "Please enter a valid hotkey for potions.")
        else:
            potion = None

        confirm = self.body['Select/Confirm'].entry_hk.get_ahk_code()
        window = self.body['Craft Window'].entry_hk.get_ahk_code()
        escape = self.body["Exit Menus"].entry_hk.get_ahk_code()
        if any(selection == '' for selection in (confirm, window, escape)):
            return (False, "Please enter valid hotkeys for menu management.")
        settings = (self.check_food.get() == 1, 
                    self.check_pot.get() == 1, 
                    self.check_collect.get() == 1)
        
        # Confirm no duplicate hotkeys
        vk_list = [confirm, window, escape]
        for macro in macros:
            vk_list.append(macro[0])
        if food is not None:
            vk_list.append(food[0])
        if potion is not None:
            vk_list.append(potion[0])
        if any(vk_list.count(x) > 1 for x in vk_list):
            return (False, "Please change duplicate hotkey entries.")


        final_args = (macros, food, potion, confirm, window, escape, settings, 
                      self.update_status)
        return (True, final_args)

    def update_status(self, text):
        """ Update display on what is happening next """
        print(text)


class WidgetGroup:
    def __init__(self, frame=None, label='', style=None, hk_settings=None, 
                 timer=True, timer_settings=None, enabler=True, var=None, 
                 enable_settings=None, key_trans=None, focus_toggle=None, 
                 time_label='min'):
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
            self.entry_time_label = tk.Label(frame, text=time_label, 
                                             width=3, anchor=tk.W, **style)
        else:
            self.entry_time = None
        if enabler:
            self.enable = tk.Checkbutton(frame, variable=var, **enable_settings) 
        else: 
            self.enable = None

    def render_all(self, row):
        x = 3
        y = 1
        self.label.grid(row=row, padx=3, pady=0, sticky=tk.E)
        self.entry_hk.grid(row=row, column=1, columnspan=3, padx=x, pady=y)
        if self.entry_time is not None:
            self.entry_time.grid(row=row, column=4, padx=x, pady=y)
            self.entry_time_label.grid(row=row, column=5, padx=0, pady=y, sticky=tk.W)
        if self.enable is not None:
            self.enable.grid(row=row, column=6, padx=x, pady=y)

    def get(self):
        return (self.entry_hk.get_ahk_code(), self.entry_time.get_time())


        

if __name__ == '__main__':
    """
    test = MainBody()
    test.start()
    """
    print('import loaded')