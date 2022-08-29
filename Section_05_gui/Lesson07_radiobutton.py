from tkinter import *  # gui lib

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

label = Label(root, text="Choose the color")

choice = StringVar()  # could be IntVar as well
# variable=choice creates a Group showing the "choice" selection
r1 = Radiobutton(root, text="Red", variable=choice, value="red")
r2 = Radiobutton(root, text="Yellow", variable=choice, value="yellow")
r3 = Radiobutton(root, text="Green", variable=choice, value="green")
# set init selection
choice.set("yellow")
# read the selected value
print(choice.get())


choice1 = IntVar()  # could be IntVar as well
# variable=choice creates a Group showing the "choice" selection
r4 = Radiobutton(root, text="Red", variable=choice1, value=1)
r5 = Radiobutton(root, text="Yellow", variable=choice1, value=2)
r6 = Radiobutton(root, text="Green", variable=choice1, value=3)
choice1.set(3)

r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()
r6.pack()

# Finally, opening the Main window
root.mainloop()
