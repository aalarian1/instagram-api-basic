from xount import count
def serial_code():
    called = True
    #opens reads grabs exists edits rewrites
    if called:
        count_file = open("xount.py", "r") # open file in read mode
        x = count_file.read() # read data 
        count_file.close() # close file
        z, (y) = x.split( ' = ',2) #split count from number
        num = str(int(y) + 1)#map(int, y) #adds int one and returns back as string 
        count_file = open("xount.py", "w") # open file again but in write mode
        count_file.write(z + " = " + num + "\n") #write new count number
        count_file.close() # close file
    return count
