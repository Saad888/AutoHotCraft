import os
import subprocess
import exceptions


class AHKManager:
    def __init__(self, path):
        """ Module for running AHK via command line and processing response"""
        self.path = path
        self.craft_active = False
        self.create_base()


    def execute(self, hotkey='', modifier=''):
        """ Executes AHK script via command line, sending keys as argument
        hotkey - str: in form needed by AHK (see their documentation)
        modifier - str: ^, !, or + based on modifier (see AHK documentation)
        """

        arg = modifier + "{" + hotkey + "}"
        cmd = f'{self.path} AHCScript.ahk {arg}'

        # Run the script passing the hotkey as a parameter, verifies files
        try:
            result = subprocess.run(cmd, 
                                    stderr=subprocess.PIPE, 
                                    stdout=subprocess.PIPE)
        except FileNotFoundError:
            # If error, checks if AHCScript is missing
            try:
                check_file = file.open('AHCScript.ahk')
                check_file.close()
            except FileNotFoundError:
                raise exceptions.AHKScriptMissingError
            raise exceptions.AHKMissingError
        
        # Verify script executed without issue
        if result.returncode != 0:
            raise exceptions.AHKFailedReturnError

        # Verifies if the FFXIV process was found
        process_id = result.stdout.decode('utf-8')
        if not process_id: 
            raise exceptions.ProcessNotFoundError


    def create_base(self):
        # Create the base ahk script incase script
        script = [
            '; Do NOT modify this script. If you did, restart AutoHotCraft.exe\n'
            '#NoEnv\n', '#ErrorStdOut\n', 'SendMode Input\n', 
            'WinGet, programid, List, Untitled - Notepad\n', 
            'if A_Args.Length() > 0\n', '{\n', 
            'ControlSend,, %1%, ahk_id %programid1%\n', '}\n'
            'FileAppend, %programid1%, *\n'
        ]
        with open('AHCScript.ahk', 'w') as ahk_script:
            ahk_script.writelines(script)

        
if __name__ == '__main__':
    Tester = AHKManager(path='"C:\\Program Files\\AutoHotkey\\AutoHotkey.exe"')
    Tester.execute('a')
