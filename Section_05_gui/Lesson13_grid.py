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
label6 = Label(root, text="User name : ", font="Tahoma 20", bg="#789")
label7 = Label(root, text="Password  : ", font="Tahoma 20", bg="#790")

# Grid is based on rows and columns
# the ipadx and ipady are for internal padding where padx and pady are for external

label1.grid(row=0, column=0, padx=10, pady=20)
label2.grid(row=0, column=1, ipadx=10, ipady=20)
label3.grid(row=1, column=0, pady=20, ipadx=40, columnspan=2)  # takes two columns
label4.grid(row=2, column=0, rowspan=2, sticky="e")  # takes two rows. sticky="w" is alignment within the cell
# label5.grid(row=2, column=1, sticky="e")
# label6.grid(row=3, column=1, sticky="e")

# exercise
label6.grid(row=6, column=0, sticky="e")
label7.grid(row=7, column=0, sticky="e")

edUserName = Entry(root, font="Tahoma 20" )
edUserName.grid(row=6, column=1, sticky="e")
edUserName = Entry(root, font="Tahoma 20", show="*")
edUserName.grid(row=7, column=1, sticky="e")

btLogin = Button(root, text="Login", bg="Blue", fg="White", font="Tahoma 18")
btLogin.grid(row=7, column=2, sticky="e")




# Finally, opening the Main window
root.mainloop()
