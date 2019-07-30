
from tkinter import *
import time
import threading
import os

# Blank window
root = Tk()

LAMAO = False


def testFunc(event):
    threading.Thread(target=threadedFunc).start()


def threadedFunc():
    global LAMAO
    for i in range(10):
        if LAMAO:
            break
        else:
            print(f'sleep number {i}')
            time.sleep(1)


def test2():
    global LAMAO
    print('swap state')
    LAMAO = not LAMAO


def counter():
    print(threading.active_count())


button1 = Button(root, text="Sleeper")
button1.bind('<Button-1>', testFunc)
button2 = Button(root, text="Tester", command=test2)
button3 = Button(root, text='count', command=counter)
button1.pack()
button2.pack()
button3.pack()
text = Entry(root, state="readonly")


mod = ''
char = ''


def formatter(widget):
    global mod
    global char
    ret = char
    if mod:
        ret = 'mod + ' + char
    widget.icursor(0)
    widget.delete(0, END)
    widget.insert(0, ret)


def modifier(event):
    global mod
    mod = "yes"
    formatter(event.widget)


def modifierrel(event):
    global mod
    mod = None
    formatter(event.widget)


def testtab(event):
    print('tabbed')



def textbind(event):
    arg = hex(event.keycode)
    cmd = f'"C:\Program Files\AutoHotkey\AutoHotkey.exe" AHCScript.ahk vk{arg[2:]}'
    os.system(cmd)
    print(event.keycode)


text.bind("<KeyPress>", textbind)
text.pack()

# Run the loop
# All GUI applications need to be continuously on your screen
# Does this via infinite loop, this will keep the GUI running
root.mainloop()