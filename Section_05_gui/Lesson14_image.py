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

root = Tk(screenName="GuiTest")
setWindow(root)

# PhotoImage is a basic libs and there are other more advanced (Python Image Library)

MyPhoto = PhotoImage(file="C:\\Temp\\test.png")
# or
bgImage = MyPhoto.zoom(2, 2)  # zoom out 2 times
# bgImage = MyPhoto.subsample(2, 2)  # zoom in 2 times
MyImage = Label(root, image=MyPhoto)

# MyImage.pack()
# or
bg = Label(root, image=bgImage)
bg.place(x=0, y=0, relwidth=1, relheight=1)
# or
bt = Button(root, image=MyPhoto)
bt.pack()

# Finally, opening the Main window
root.mainloop()
