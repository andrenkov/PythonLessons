from tkinter import *  # gui lib

# Tk class create
root = Tk()  # this is a Window
root.title("Main window")
root.resizable(False, False)  # horr and vert resizing

# Center screen
w = 800
h = 600
# get screen dimensions
ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()
# print(ws, wh) 1920x1080

x = int(ws / 2 - w / 2)
y = int(wh / 2 - h / 2)

# size
# root.geometry("800x600+700+400")  # size is 800x600 and the location is 700:400
root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

# Finally, opening the Main window
root.mainloop()


