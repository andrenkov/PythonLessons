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

# Place is more complicated than Pack, but is more powerful
# Place allows coordinates of the locations in pixels where Pack is just left, top etc. Plus Width and Height of a control
# Place is the best and widely used !!!!!!!!!!!!!!!!!!!!!!!!!

# absolute coordinate
label1.place(x=10, y=5)  # n s w s or combinations plus anchor="center"... . nw (top-left) is the default
# relational coordinates
label2.place(relx=0.5, rely=0.5, anchor="center")  # middle of the form. rel 0..1
label3.place(relx=0.5, rely=0, anchor="n")  # n is Top edge
label4.place(relx=0.5, rely=0.6, width=500, height=25, anchor="center")
label5.place(relx=1, rely=0, anchor='ne')  # top right corner

# exercise
label6.place(relx=0.1, rely=0.7, anchor="w")
label7.place(relx=0.1, rely=0.8, anchor="w")

edUserName = Entry(root, font="Tahoma 20" )
edUserName.place(relx=0.4, rely=0.7, anchor="w")
edUserName = Entry(root, font="Tahoma 20", show="*")
edUserName.place(relx=0.4, rely=0.8, anchor="w")

btLogin = Button(root, text="Login", bg="Blue", fg="White", font="Tahoma 18")
btLogin.place(relx=0.1, rely=0.9, anchor="w")

# Finally, opening the Main window
root.mainloop()
