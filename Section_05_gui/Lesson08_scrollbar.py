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

MyMemo = Text(root, bd=2, font="Tahoma 20", bg="Yellow", width=40, padx=10, pady=20)  # width and Height are in number of chars
MyMemo.insert(END, "My Memo\ntesting it")

scrollBar = Scrollbar(root, command=MyMemo.yview, orient=VERTICAL)  # link to MyMemo by Y coordinate

# tell memo that is has a scrollbar
MyMemo["yscrollcommand"] = scrollBar

# pack it with left alignment
MyMemo.pack(side='left')
scrollBar.pack(side='left', fill=Y)  # fill=Y is to stretch it vertically

# exercise
fn = 'C:\\Temp\\test.txt'
try:
    fileHandler = open(fn, 'r')
    MyMemo.insert(END, fileHandler.read())
except FileNotFoundError:
    print("File {0} not found".format(fn))
finally:
    fileHandler.close()




# Finally, opening the Main window
root.mainloop()
