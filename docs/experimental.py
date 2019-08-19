
from tkinter import *
import time
import threading
import os

# Blank window
global root
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
    keycode = event.keycode
    state = event.state
    numpad_keys = {
        12: 101, 
        33: 105, 
        34: 99, 
        35: 97, 
        36: 103, 
        37: 100, 
        38: 104, 
        39: 102, 
        40: 98
    }
    if keycode in numpad_keys and state < 0x40000:
        keycode = numpad_keys[keycode]
    print(keycode)


# text.bind("<KeyPress>", textbind)
text.pack()


def focusedIn(even):
    print("focused in")
    even.widget.config(bg="blue")


def focusedout(even):
    print("focused out")
    even.widget.config(bg="yellow")


label = Label(root, takefocus=True, text="Noice", bg="yellow", activebackground="blue")
label.bind("<FocusIn>", focusedIn)
label.bind("<FocusOut>", focusedout)
label.bind("<KeyPress>", textbind)
label.pack()

label2 = Label(root, takefocus=True, text="Noice", bg="yellow", activebackground="blue")
label2.bind("<FocusIn>", focusedIn)
label2.bind("<FocusOut>", focusedout)
label2.bind("<KeyPress>", textbind)
label2.pack()


global toggler
toggler = True


def toggletab():
    global root
    global toggler
    toggler = not toggler
    root.config(takefocus=toggler)
    for wid in root.winfo_children():
        wid.config(takefocus=toggler)
    print('Toggled: ' + str(toggler))


tab_button = Button(root, command=toggletab)
tab_button.pack()
print(root.winfo_children())
frame = Frame(root)
frame.pack()


def testfocus(event):
    print(event.widget.focus_displayof() == event.widget)


labelframe1 = Button(frame, text='ONE', takefocus=True)
labelframe2 = Button(frame, text='TWO', takefocus=True)
labelframe1.bind("<Button-1>", testfocus)
labelframe2.bind("<Button-1>", testfocus)
labelframe1.pack()
labelframe2.pack()



# Run the loop
# All GUI applications need to be continuously on your screen
# Does this via infinite loop, this will keep the GUI running
root.mainloop()