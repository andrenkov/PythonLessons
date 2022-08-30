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

# frame the same as Panel
fram1 = Frame(root, bg="Red", bd=1)
fram2 = Frame(root, bg="Green", bd=10)

label1 = Label(fram1, text="Label 1", font="Tahoma 20")
label2 = Label(fram2, text="Label 2", font="Tahoma 20")
label3 = Label(fram2, text="Label 3", font="Tahoma 20")

fram1.pack()
fram2.pack()

label1.pack()
label2.pack()
label3.pack()

# Finally, opening the Main window
root.mainloop()
