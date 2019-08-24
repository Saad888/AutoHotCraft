""" Widget for hotkey inputs """
import tkinter as tk


class TimeWidget:
    def __init__(self, master, default_settings, inactive_settings, 
                 active_settings):
        """ Create widget with settings. kwargs should be label settings """
        # Create widget and bind events
        self.widget = tk.Label(
            master, 
            takefocus=True, 
            **default_settings, 
            **inactive_settings, 
            text='0'
        )
        self.event_binder()

        # Settings for different label states
        self.default_settings = default_settings  # Default 
        self.inactive_settings = inactive_settings  # State without focus
        self.active_settings = active_settings  # After focused into

        # System variables
        self.timer = '0'

    def get_time(self):
        return int(self.timer)

    def _pack(self):
        """ Renders widget in pack, for debugging purposes only """
        self.widget.pack()

    def grid(self, **kwargs):
        """ Renders widget on provided master using grid"""
        self.widget.grid(**kwargs)

    def render_text(self):
        """ Render the text on the label """
        if len(self.timer) == 2 and self.timer[0] == '0':
            self.timer = self.timer[1:]
        self.widget.config(text=self.timer)

    def event_binder(self):
        self.widget.bind('<FocusIn>', self.handle_focus_in)
        self.widget.bind('<FocusOut>', self.handle_focus_out)
        self.widget.bind('<ButtonRelease-1>', self.handle_click)
        self.widget.bind('<KeyPress>', self.handle_keydown)

    def handle_focus_in(self, event):
        """ Handles widget taking focus"""
        self.widget.config(**self.active_settings)

    def handle_focus_out(self, event):
        """ Return label to default state """
        self.widget.config(**self.inactive_settings)

    def handle_click(self, event):
        """
        Sets focus onto widget
        """
        self.widget.focus_set()

    def handle_keydown(self, event):
        """
        Handle key press while in focus
        If not enabled, set to enable when <Space> is pressed
        If enabled, set the timer accordingly
        """
        if event.char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if len(self.timer) == 2:
                self.timer = self.timer[1:]
            self.timer += event.char
        elif event.keycode in (8, 46):
            self.timer = '0'

        self.render_text()


        


if __name__ == "__main__":
    print('Debugging mode for hotkey widget activated')
    root = tk.Tk()
    root.config(takefocus=False)
    button1 = tk.Button(root, text='TEST')
    button1.pack()

    widget1 = TimeWidget(root, {}, {"bg": "blue"}, {"bg": "red"})
    widget2 = TimeWidget(root, {}, {"bg": "blue"}, {"bg": "red"})

    widget1._pack()
    widget2._pack()

    root.mainloop()