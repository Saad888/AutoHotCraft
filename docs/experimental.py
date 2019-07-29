
from tkinter import *
import time
import threading

# Blank window
root = Tk()

LAMAO = False


def testFunc(event):
    threading.Thread(target=threadedFunc, daemon=True).start()


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



button1 = Button(root, text="Sleeper")
button1.bind('<Button-1>', testFunc)
button2 = Button(root, text="Tester", command=test2)
button1.pack()
button2.pack()

# Run the loop
# All GUI applications need to be continuously on your screen
# Does this via infinite loop, this will keep the GUI running
root.mainloop()