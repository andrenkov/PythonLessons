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

# example of complete interface with header, labels etc

# event=False means not mandatory param. Will work for Bind(), but allow command=OnClick1 as well without an argument
def OnClick1(event=False):
    # global used to avoid messing up with other vars by name
    global edEntry1
    global edEntry2
    global edResult
    try:
        r = str(float(edEntry1.get()) + float(edEntry2.get()))
        edResult.config(text="Sum = " + r)
    except ValueError:
        if not edEntry1.get() or not edEntry2.get():  # empty str in Python is the same as False
            edResult.config(text="Empty entry")
        else:
            edResult.config(text="You didn't enter numbers")

formHeader = Label(root, text="Summary of numbers", font="Tahoma 24")
edEntry1 = Entry(root, font="Tahoma 18")
edEntry2 = Entry(root, font="Tahoma 18")
button1 = Button(root, text="Sum it", font="Tahoma 18", command=OnClick1)
edResult = Label(root, font="Tahoma 20")
# add calculation on a hot key "Enter"
edEntry1.bind("<Return>", OnClick1)
edEntry2.bind("<Return>", OnClick1)

formHeader.place(relx=0.5, rely=0.01, anchor="n")
edEntry1.place(relx=0.5, rely=0.1, anchor="n")
edEntry2.place(relx=0.5, rely=0.2, anchor="n")
button1.place(relx=0.5, rely=0.3, anchor="n")
edResult.place(relx=0.5, rely=0.4, anchor="n")

# Finally, opening the Main window
root.mainloop()


