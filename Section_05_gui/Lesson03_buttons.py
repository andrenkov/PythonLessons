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

button1 = Button(root, text="My button", bg="Blue", fg="White", font="Tahoma 18")
button1.pack()
button1 = Button(root, text="Close", bg="Black", fg="White", font="Tahoma 22")
button1.pack()

# Finally, opening the Main window
root.mainloop()


