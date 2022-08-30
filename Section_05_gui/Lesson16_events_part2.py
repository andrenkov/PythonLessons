import random
from tkinter import *  # gui lib

def setWindow(root):
    root.title("Main window")
    root.resizable(False, False)  # horriz and vert resizing

    # Center screen
    w = 800
    h = 600
    # get screen dimentions
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    # print(ws, wh) 1920x1080

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    # size uses the geometry tuple
    # root.geometry("800x600+700+400")  # size is 800x600 and the location is 700:400
    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setWindow(root)

# example of hover event
# event.widget is the object of the Event like "Sender"

def OnHover(event):
    # button1.config(bg="red")
    event.widget.config(bg="red")


def OnLeave(event):
    # button1.config(bg="yellow")
    event.widget.config(bg="yellow")

button1 = Button(root, text="Hover me 1", font="Tahoma 18", bg="yellow")
button2 = Button(root, text="Hover me 2", font="Tahoma 18", bg="yellow")

button1.bind("<Enter>", OnHover)
button1.bind("<Leave>", OnLeave)

button2.bind("<Enter>", OnHover)
button2.bind("<Leave>", OnLeave)

button1.pack()
button2.pack()

# Finally, opening the Main window
root.mainloop()


