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

# pack controls the layout. Center is the default location in the designated area

label1 = Label(root, text="Label 1", font="Tahoma 20", bg="red")
label2 = Label(root, text="Label 2", font="Tahoma 20", bg="blue")
label3 = Label(root, text="Label 3", font="Tahoma 20", bg="green")
label4 = Label(root, text="Label 4", font="Tahoma 20", bg="yellow")
label5 = Label(root, text="Label 5", font="Tahoma 20", bg="#777")
label6 = Label(root, text="Label 6", font="Tahoma 20", bg="#789")

# side means Dock. Literal["left", "right", "top", "bottom"] = ...,
# expand means align within the area
# fill=X is for stretching horizontally. Literal["none", "x", "y", "both"]
# anchor align to West, East, North or South

label1.pack(side='left', expand=True, fill=X, anchor='n')
label2.pack(side='right', anchor='n')
label3.pack(side='top')
label4.pack(side='bottom')
label5.pack(side='bottom')
label6.pack(side='bottom', expand=True)

# Finally, opening the Main window
root.mainloop()
