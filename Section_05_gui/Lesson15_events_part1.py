import random
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

def OnClck1():
    print("Clicked")

def OnClck2(args):
    print(args)

def OnClck3(event):  # event required for right click
    print("Right button clicked")
    print(event)  #<ButtonPress event state=Mod1 num=3 x=74 y=30>
    print(event.widget.cget('text'))  # .!button3

def OnClickRoot(event):
    print(event)
    print('Event occurred')
    # print("You clicked on : ", event.widget.cget('char'))

# if command event is writen as ObClick1(), it will be triggered on control Create only
# if command event is writen as ObClick1,   it will be triggered as normal event

button1 = Button(root, text="Click me 1", font="Tahoma 18", command=OnClck1)
# event with param need lambda
button2 = Button(root, text="Click me 2", font="Tahoma 18", command= lambda :OnClck2("Button clicked"))
# right click example using bind() method
button3 = Button(root, text="Click me 3", font="Tahoma 18")
button3.bind("<Button-3>", OnClck3)  # <Button-1> - left button, <Button-2> wheel and <Button-3> right
# Bt2OnClickHandle is an event handle to use later on for Unbind() the event
Bt2OnClickHandle = button2.bind("<Button-3>", OnClck3)

# the following is like a KeyPress() where "a" is a key
root.bind("a", OnClickRoot)
root.bind("<Control-a>", OnClickRoot)  # ctrl+a

# unbind()
button2.unbind(OnClck3, Bt2OnClickHandle)

button1.pack()
button2.pack()
button3.pack()

# exercise
lbRandomNum = Label(root, text="Randon", font="Tahoma 20")

def OnClck4(args):
    num = int(random.random() * 100)
    lbRandomNum.config(text=num)

button4 = Button(root, text="Get randon #", font="Tahoma 18")
button4.bind("<Button-1>", OnClck4)

button4.pack()
lbRandomNum.pack()

# Finally, opening the Main window
root.mainloop()


