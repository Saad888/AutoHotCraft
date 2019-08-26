# AutoHotCraft
An application designed for automatic crafting in Final Fantasy XIV
This application uses Autohotkey to send inputs into the game to start crafting macros, repeat the same crafts, and reactivate food and potions when they are running out.
It's designed to make it easy to handle different macros and craft lengths. 

![Main Body Image](https://github.com/Saad888/AutoHotCraft/blob/master/docs/Main%20Screen.PNG)

# Main features:
1. Automate up to three macros   
2. Refresh food and potions   
3. Auto-confirm for collectable synthesis  
4. Save profiles of different hotkey configurations and timers for various crafts  
5. Runs in the background without requiring focus on the game  

# Requirements:
This applicaiton requires AutoHotkey to be installed to use, you can download it from here:  
https://www.autohotkey.com/

# Instructions for use:
To enter a hotkey into a selection, click on the window or tab over to it. When it is highlighted, press SPACE or click on the window again until it turns yellow.  
![Active UI Image](https://github.com/Saad888/AutoHotCraft/blob/master/docs/Accepting%20Input.PNG)

When the window is yellow, it ready to take a hotkey. Press any key along with modifiers (Shift, Contorl, or Alt) to save it in that field.    

For the timers, simply tab over to or click on the time window and type in any number.

For macros, enter the time of the macro in seconds
For food and pots, enter the amount of time left on your food and/or pot before the craft begins
Be sure to select the check next to the windows to enable those during the craft.

A hotkey for the crafting window, select/confirm action, and exit menus are required.

You can select the food timer to be 30 minutes or 40 minutes based on your FC buffs. Selecting the collectable craft button will ensure it automatically accepts the prompt after the craft is complete. 

To begin the autocrafting, you must **start in crafting position** with your food and pots already enabled. The first action the autocrafter will take is the first macro.
Also, note that if you are using the food/pot option on the autocrafter, you MUST manually find which item you want to craft through the ingame crafting window WITHOUT using the search feature. See limitations for more details. 

# Profiles:
You can save and load your settings for various set-ups. 
To save a profile, click the "Save Profile" button and enter a name when prompted.
To load a profile, select it from the dropdown menu and click "Load Profile". 
To delete a profile, select it from the drowdown menu and click "Delete Profile".


# Limitations:
This application does not detect what is happening within the game, it will not detect what is happening on your screen on its own. If it desyncs at any point, either due to issues with the craft, latency, or incorrect inputs, the autocraft will need to be paused and restarted.  

FFXIV's ingame crafting menu will save what last craft you selected through the menus. It will NOT save what you started crafting when you use the search feature. As a result, if you are using the food or pot refresh option, you need to manually find the craft through the menus without searching for it. This is because to refresh the food, you need to leave the menu and exit crafting altogehter, use the consumables, and then enter back in. AHC won't find which craft you were using, rather it will just try to intiate the craft that is currently selected. If you select the craft manually, it will automatically default back to the craft you were doing and keep going without any user inputs. 
If you are not using the food/pot option, this won't be nessecary as there is no reason to leave the crafting menu in the first place. 

AHC doesn't account for mat usage and doesn't (currently) have a feature to do a specific number of crafts. This might be added in later on.
AHC also doesn't repair gear. 


