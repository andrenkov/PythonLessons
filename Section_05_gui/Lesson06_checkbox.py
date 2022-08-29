from tkinter import *  # gui lib
import random

def setWindow(mainroot):
    mainroot.title("Main window")
    mainroot.resizable(False, False)  # horizontal and vert resizing

    # Center screen
    w = 800
    h = 600
    # get screen dimensions
    ws = mainroot.winfo_screenwidth()
    wh = mainroot.winfo_screenheight()
    # print(ws, wh) 1920x1080

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    # size uses the geometry tuple
    # root.geometry("800x600+700+400")  # size is 800x600 and the location is 700:400
    mainroot.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


root = Tk()
setWindow(root)

# boxed var
choice = IntVar()
cbx = Checkbutton(root, bd=20, text="delete after reading", variable=choice, onvalue=1, offvalue=0)
# variable=choice is for getting the status of the checkbox
# onvalue=1, offvalue=0 for setting the value for On and Off

# change and check the status
# cbx.select()
# print(choice.get())
# cbx.deselect()
# print(choice.get())
# or to select the cbx modify the choice var
# choice.set(1)  # check
# choice.set(0)  # uncheck

# exercise
checked = int(random.randrange(0, 2))
choice.set(checked)

cbx.pack()

# Finally, opening the Main window
root.mainloop()
