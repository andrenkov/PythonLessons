# open file with modificator
handler = open('C:\\Temp\\test.txt', 'w')
# 'w' is opening for writing and/or creating new file. Data will be overwritten
# 'x' - open existing file
# 'a' - open existing without overwriting the context (append)
# 'r' - open for read
# 'rt' - open text file (default and can be skipped)
# 'rb' - open binary file

# working with file read or write
handler.write("my new file to open\nnew line goes here")

# close file
handler.close()

#reading file
fn = 'C:\\Temp\\test.txt'
try:
    handler = open(fn, 'r')
    print(handler.read(2))  # read two symbols only
    print(handler.read())  # read the rest
except FileNotFoundError:
    print("File {0} not found".format(fn))
if handler.closed == False:
    handler.seek(0)  # return position to the beginning of the file
    print("----------------------")
    for line in handler:
        print(line)

    handler.close()
