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
# simple edit
edit = Entry(root, font="Tahoma 20", bg="Yellow", fg="Blue", bd=4)
edit.insert(END, "Hello ")
edit.insert(END, "Vlad")
edit.pack()
# password box
password = Entry(root, font="Tahoma 20", bg="Yellow", fg="Blue", bd=4, show="*")
password.pack()
# check params of the control
print(edit.cget("font"))  # "Tahoma 20"
# or
edit["font"] = "Tahoma 12"  # change property
print(edit["font"])  # "Tahoma 20"

# exercise
text = input("Enter your Name :")
edit.delete(0, 100)
edit.insert(0, "You entered : {0}".format(text))
print("Entered : {0}".format(edit.get()))  # read text context

# Finally, opening the Main window
root.mainloop()
