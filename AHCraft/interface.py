import tkinter as tk


class MainBody:
    def __init__(self, configs=None):
        self.configs = configs
        self.default_style = {
            'font': ("Helvetica", 14), 
            'bg': "purple",
            'fg': "white"
        }
        self.root = tk.Tk()

    def start(self):
        # Create all body components and launch the main loop
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
        self.body = (
            WidgetGroup(self.fr_body, "Macro 1", self.default_style),
            WidgetGroup(self.fr_body, "Macro 2", self.default_style),
            WidgetGroup(self.fr_body, "Macro 3", self.default_style),
            WidgetGroup(self.fr_body, "Food", self.default_style),
            WidgetGroup(self.fr_body, "Craft Window", self.default_style, False),
            WidgetGroup(self.fr_body, "Select/Confirm", self.default_style, False)
        )

        # *** Render Widgets ***
        self.render(bdy_lbl_name, row=0, col=0)
        self.render(bdy_lbl_hk, row=0, col=1, colspan=3)
        self.render(bdy_lbl_time, row=0, col=4)
        for index, group in enumerate(self.body):
            row = index + 1
            group.render_all(row=row)
        

        # ********* Footer *********
        # *** Create Widgets ***
        self.start_btn = tk.Button(self.fr_footer, text="BEGIN", 
                                   bg="blue", fg="yellow", width=10, height=3)
        self.check_food = tk.Checkbutton(self.fr_footer, text="Use Food")
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
        self.check_potion = tk.Checkbutton(self.fr_footer, text="Use Potion")
        self.check_collect = tk.Checkbutton(self.fr_footer, text="Collectable Craft")
        
        # *** Render Widgets ***
        self.render(self.start_btn, rowspan=3)
        self.render(self.check_food, col=1, sticky=tk.W)
        self.render(self.food_radio[0], col=2, sticky=tk.W)
        self.render(self.food_radio[1], col=3, sticky=tk.W)
        self.render(self.check_potion, row=1, col=1, sticky=tk.W)
        self.render(self.check_collect, row=2, col=1, sticky=tk.W)

        # Start root:
        self.fr_title.pack(side=tk.TOP, fill=tk.X)
        self.fr_body.pack(side=tk.TOP, fill=tk.X)
        self.fr_footer.pack(side=tk.TOP, fill=tk.X)
        self.root.mainloop()


    def render(self, widget, row=0, col=0, colspan=1, rowspan=1, 
               padx=3, pady=0, sticky=tk.W):
        """Simple method to make rendering easier"""
        widget.grid(row=row, column=col, columnspan=colspan, 
                    padx=padx, pady=pady, rowspan=rowspan, sticky=sticky)





class WidgetGroup:
    def __init__(self, frame, label, style, timer=True):
        """
        Groups a label with two entries for the body frame
        
        frame: Frame to center the widgets within
        label: Str, name of the group
        style: dictionary passed from parent caller for text formatting
        timer: Bol, if this group has a timer
        """
        self.label = tk.Label(frame, text=label, **style)
        self.entry_hk = tk.Entry(frame, width=16)
        self.entry_time = tk.Entry(frame, width=3) if timer else None

    def render_all(self, row):
        self.label.grid(row=row, padx=3, pady=0, sticky=tk.E)
        self.entry_hk.grid(row=row, column=1, columnspan=3, padx=3, pady=1)
        if (self.entry_time is not None):
            self.entry_time.grid(row=row, column=4, padx=3, pady=1)


        

if __name__ == '__main__':
    test = MainBody()
    test.start()