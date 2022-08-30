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

# data for the List
dataList = ['Apples', 'Oranges', 'Lemons', 'Peaches', 'Berries']
listBox = Listbox(root, font="Tahoma 20", width=20, height=8, selectmode=MULTIPLE)
for data in dataList:
    listBox.insert(END, data)

# select element(s) by default
listBox.selection_set(2,3)  # 1st and last index
# get selected element(s) as str
print(listBox.selection_get())
# get selected element(s) indx as tuple2
selIndex = listBox.curselection()
print("selected: ", selIndex)

# print by index
for i in selIndex:
    print(dataList[i])

listBox.pack()

# Finally, opening the Main window
root.mainloop()
