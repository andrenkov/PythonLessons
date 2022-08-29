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

text = Text(root, bd=2, font="Tahoma 10", bg="Yellow", width=50, height=8, padx=10, pady=20)  # width and Height are in number of chars
text.insert(END, "My Memo\ntesting it")
# read from Memo
print(text.get("1.0", END))  # 1 is from what line to read. 0 is from what symbol (0 means any ), END - to the end of
# the field

text.pack()


# Finally, opening the Main window
root.mainloop()
