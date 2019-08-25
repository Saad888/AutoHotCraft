from interface.interface import MainBody
from key_translator import KeyTranslator
from crafter import Crafter
from AHKManager import AHKManager
from exceptions import AHKExeAccessError
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter.filedialog import askopenfilename
import threading
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
        self.config_rw = ConfigLoader()
        self.GUI = MainBody(self.initiate_craft_thread, self.inturrupt_craft,
                            self.translator, self.config_rw)


    def initiate_craft_thread(self, *args):
        """
        Creates a separate thread to run the script, allowing the UI to function
        without freezing the app while the script is running.
        See crafter library for args
        toggeler is a callback function which will unlock parts of the
        UI as needed while the craft is happening
        """
        print("BEGIN CRAFT")
        threading.Thread(target=self.script_begin, args=args).start()


    def script_begin(self, toggler, args):
        print('Separate Thread Established')
        self.crafter.start(args)
        toggler()
        

    def inturrupt_craft(self):
        print('INTURRUPTED')
        self.crafter.user_inturrupt = True


    def initiate(self):
        # Loads configurations file and locates the path to AutoHotkey.exe
        path = self.config_rw.load_config('AHKPath')
        print(path)

        # If config could not be loaded, take from user input
        if (not path) or (self.verify_path(path) is False):
            path = self.get_AHK_exe()

            # If no path was given, exit application
            if path is None:
                sys.exit()
            
            # Savea the provided path
            configs = self.config_rw.load_all()
            if configs is None:
                configs = {}
            configs['AHKPath'] = path
            self.config_rw.save_config(configs)

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



class ConfigLoader:
    def load_all(self):
        try:
            with open('configs.json', 'r') as file:
                configs = json.load(file)
            return configs
        except FileNotFoundError:
            return None

    def load_config(self, param):
        configs = self.load_all()
        try:
            return configs[param]
        except (KeyError, TypeError) as e:
            return None

    def save_config(self, configs):
        with open('configs.json', 'w') as file:
            json.dump(configs, file)
            

if __name__ == "__main__":
    test = Main()
    print('starting')
    test.initiate()