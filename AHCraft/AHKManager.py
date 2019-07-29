

class AHKManager:
    def __init__(self, path):
        self.path = path
        self.craft_active = False
        self.create_base()


    def execute(self, hotkey):
        # Run the script passing the hotkey as a parameter
        pass

    def start_thread(self):
        # Start the thread running the main script
        pass

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
    Tester = AHKManager(path='')
    Tester.create_base()