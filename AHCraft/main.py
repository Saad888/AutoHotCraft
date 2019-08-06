from interface import MainBody
from key_translator import KeyTranslator
from crafter import Crafter
from AHKManager import AHKManager
from exceptions import AHKExeAccessError
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
import json
import os
import sys
import re


class Main:
    def __init__(self):
        # Class instances
        self.translator = KeyTranslator()
        self.AHKManager = AHKManager()
        self.crafter = Crafter(self.AHKManager)
        self.GUI = MainBody(self.script_begin, self.inturrupt_craft)


    def script_begin(self, macros, food, pot, confirm, window, 
                     settings, button_func):
        print('BEGIN')
        self.crafter.start(macros, food, pot, confirm, window, settings, 
                           button_func)

    def inturrupt_craft(self):
        print('INTURRUPTED')
        self.crafter.user_inturrupt = True

    def initiate(self):
        self.configs = {}

        # Loads configurations file and locates the path to AutoHotkey.exe
        try:
            with open('configs.json', 'r') as file:
                self.configs = json.load(file)
            try: 
                path = self.configs['AHKPath']
                if self.verify_path(path) is False:
                    path = self.get_AHK_exe()
            except KeyError:
                path = self.get_AHK_exe()
        except FileNotFoundError:
            # If the configurations file could not be found, create it via user input
            print('configs.json was not found')
            path = self.get_AHK_exe()

        # If no path was provided at this stage, exit the application
        if path is None:
            sys.exit()

        # Rewrite the configs to ensure any path updates are reflected
        self.configs['AHKPath'] = path
        self.write_configs()

        self.AHKManager.path = path

        self.GUI.start()


        
    def get_AHK_exe(self):
        """User request for the AutoHotkey.exe file, verifies the executable"""
        while True:
            message = 'Please locate AutoHotkey.exe'
            showwarning('AutoHotkey.exe missing!', message=message)
            default = 'C:\Program Files\AutoHotkey'
            path = askopenfilename(title='Please locate AutoHotkey.exe', 
                                   initialdir=default)
            if not path:
                return None
            checker = re.search('AutoHotkey.exe$', path)
            if (checker is not None):
                if (os.access(path, os.X_OK)):
                    return path
                else:
                    showwarning('Cannot load executable for some reason')
                    raise AHKExeAccessError

            showwarning('Invalid file, please find AutoHotkey.exe')

    def verify_path(self, path):
        return re.search('AutoHotkey.exe$', path) and (os.access(path, os.X_OK))

    def write_configs(self):
        with open('configs.json', 'w') as file:
            json.dump(self.configs, file)

if __name__ == "__main__":
    test = Main()
    test.initiate()