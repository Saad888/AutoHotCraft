""" Widget for hotkey inputs """
import tkinter as tk


class HotkeyWidget:
    def __init__(self, master, default_settings, inactive_settings, 
                 active_settings, enabled_settings, key_translator=None, 
                 focus_toggle=None):
        """ Create widget with settings. kwargs should be label settings """
        # Create widget and bind events
        self.widget = tk.Label(
            master, 
            takefocus=True, 
            **default_settings, 
            **inactive_settings
        )
        self.event_binder()

        # Settings for different label states
        self.default_settings = default_settings  # Default 
        self.inactive_settings = inactive_settings  # State without focus
        self.active_settings = active_settings  # After focused into
        self.enabled_settings = enabled_settings  # When activated for inputs

        # System variables
        self.input_enabled = False  # When input is enabled
        self._default_inputs()
        self.key_translator = key_translator

        # Saves callback function for toggling system focus
        # This function should be provided from the interface class
        # For the purposes of debugging an empty lambda function will be created
        # if no input is given
        # The focus toggler should have one boolean input
        if focus_toggle:
            self.focus_toggle = focus_toggle
        else:
            self.focus_toggle = lambda x: print(x)

    def _default_inputs(self):
        """ Set default input values """
        self.active_keys = {'mods': [], 'key': -1}

    def _pack(self):
        """ Renders widget in pack, for debugging purposes only """
        self.widget.pack()

    def grid(self, **kwargs):
        """ Renders widget on provided master using grid"""
        self.widget.grid(**kwargs)

    def get_ahk_code(self):
        """ Returns ahk command """
        code = ''
        for mod in self.active_keys['mods']:
            code += self.key_translator.key_ahk(mod)
        code += self.key_translator.key_ahk(self.active_keys['key'])
        return code

    def render_text(self):
        """ Render the text on the label """
        text = ''
        for mod in self.active_keys['mods']:
            text += self.key_translator.key_name(mod) + " + "
        text += self.key_translator.key_name(self.active_keys['key'])
        self.widget.config(text=text)

    def toggle_input(self, input, configs):
        """ Used to DRY enabling and disabling input selection """
        self.input_enabled = input
        self.widget.config(**configs)
        self.focus_toggle(not input)


    def enable_input(self):
        """ Enables hotkey input and disables window focus shifting """
        self.toggle_input(True, self.enabled_settings)
        self._default_inputs()
        self.render_text()
        print('Input Enabled')

    def disable_input(self):
        """ Disables hotkey input and enables window focus shifting """
        self.toggle_input(False, self.active_settings)
        print('Input Disabled')

    def event_binder(self):
        self.widget.bind('<FocusIn>', self.handle_focus_in)
        self.widget.bind('<FocusOut>', self.handle_focus_out)
        self.widget.bind('<ButtonRelease-1>', self.handle_click)
        self.widget.bind('<KeyPress>', self.handle_keydown)
        self.widget.bind('<KeyRelease>', self.handle_keyup)

    def handle_focus_in(self, event):
        """ Handles widget taking focus"""
        self.widget.config(**self.active_settings)
        print('Focused In')

    def handle_focus_out(self, event):
        """ Return label to default state """
        if self.input_enabled:
            self.disable_input()
        self.widget.config(**self.inactive_settings)
        print('Focused Out')

    def handle_click(self, event):
        """
        Handle label being clicked 
        If not in focus, take focus
        If in focus, enable for input
        Does nothing if input is enabled
        """
        if self.input_enabled:
            self.disable_input()
            return
        
        verify_focus = event.widget.focus_get() == self.widget
        if verify_focus:
            self.enable_input()
        else:
            self.widget.focus_set()
        print('Clicked')

    def handle_keydown(self, event):
        """
        Handle key press while in focus
        If not enabled, set to enable when <Space> is pressed
        If enabled, set the hotkey accordingly
        """
        if not isinstance(event, int):
            keycode = self.key_translator.keycode(event.keycode, event.state)
            if keycode != event.keycode:
                self.handle_keydown(16)
        else:
            keycode = event
            
        if self.input_enabled is True:
            if self.key_translator.key_mod(keycode) is True:
                if keycode not in self.active_keys['mods']:
                    self.active_keys['mods'].append(keycode)
            else:
                self.active_keys['key'] = keycode
            self.render_text()

    def handle_keyup(self, event):
        """
        Handle key up while in focus
        Must be enabled to do action
        If key up is a mod, remove modifier
        If key up is non mod, disbale key input
        """
        """
        if not isinstance(event, int):
            
            if keycode != event.keycode:
                self.handle_keyup(16)
        else:
            keycode = event
        """
        keycode = self.key_translator.keycode(event.keycode, event.state)

        if self.input_enabled is True:
            if keycode in self.active_keys['mods']:
                self.active_keys['mods'].remove(keycode)
            elif keycode == self.active_keys['key']:
                self.disable_input()
            self.render_text()
        else:
            if keycode == 32:
                self.enable_input()
        print('Released')
        


if __name__ == "__main__":
    print('Debugging mode for hotkey widget activated')
    root = tk.Tk()
    root.config(takefocus=False)
    button1 = tk.Button(root, text='TEST')
    button1.pack()
    root.unbind_all('<Alt>')
    root.unbind_all('<F10>')

    def focus_toggleer(k):
        button1.config(takefocus=k)

    widget1 = HotkeyWidget(root, {}, {"bg": "blue"}, {"bg": "red"}, {"bg": "yellow"}, focus_toggle=focus_toggleer)
    widget2 = HotkeyWidget(root, {}, {"bg": "blue"}, {"bg": "red"}, {"bg": "yellow"}, focus_toggle=focus_toggleer)

    def focus_toggleer(k):
        button1.config(takefocus=k)
        widget1.widget.config(takefocus=k)
        widget2.widget.config(takefocus=k)

    widget1.focus_toggle = focus_toggleer
    widget2.focus_toggle = focus_toggleer
    widget1._pack()
    widget2._pack()

    def test_ahk():
        print(widget1.get_ahk_code())
        print(widget2.get_ahk_code())

    button1.config(command=test_ahk)

    root.mainloop()