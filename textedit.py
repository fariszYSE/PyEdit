import os
import fileio
import msvcrt
file = [
    ""#<-cursor starts here
]
lefty = False
righty = False
cursorcol = 0
cursorrow = 0
delete_key_pressed = False
tempfile = file
key = ""
def on_start():
    global enter_key_pressed,file_name,testgrid
    enter_key_pressed = False
    file_name = input("enter the absolute path to the file you want.. or if its in the same directory as the place the code is ran from you just enter the name. enter path here:\n")
    testgrid = [char for item in file for char in item]; print(testgrid) #flatten file into a character list
    loop()
def string_to_list(turnlist):
    turnlist = [char for item in file for char in item]
def list_to_string(turnstring):
     global key,cursorcol,file
     turnstring = list(file);turnstring.insert(cursorcol, key);file = "".join(turnstring); cursorcol += 1
def stdin():#read one keypress and set input flags
    global lefty, righty, delete_key_pressed,cursorcol,cursorrow,enter_key_pressed, key,file; key = msvcrt.getwch()
    if key in ("\x00", "\xe0"):#extended key, read the second code
        key = msvcrt.getwch()
        if key == "K":
            lefty = True
        elif key == "M":
            righty = True
        elif key == "H":
            print("Up arrow")
        elif key == "P":
            print("Down arrow")
    elif key == '\b':
        delete_key_pressed = True
    elif key == '\r':
        enter_key_pressed = True
    else:
        line = list(file);line.insert(cursorcol, key);file = "".join(line); cursorcol += 1
def action_move_r():#consume right arrow input
    global righty
    if righty:
        righty = False
        return True
    else:
        pass
def action_move_l():#consume left arrow input
    global lefty
    if lefty:
        lefty= False
        return True
    else:         pass 
def cursor():#update cursor position
    global testgrid
    global grid
    global cursorcol
    global cursorrow
    grid=[
        1,2,3,
        4,0,6,#cursor is the 0. imagine it is just one row
        7,8,9
    ]
    if action_move_l() and cursorcol > 0:#left boundary check
        cursorcol -= 1; print(cursorcol)
    else:
        print(cursorcol)
    if action_move_r() and cursorcol < len(testgrid):#right boundary check
        cursorcol += 1; print(cursorcol)
    else:
        print(cursorcol)
def check_item_on_left():#inspect/delete the character left of the cursor
    global delete_key_pressed,cursorcol,file
    if delete_key_pressed:
        line = list(file)
        if line != []:
            line.pop(cursorcol -1)
            file = "".join(line)
        else:
            pass
        if cursorcol > 0:
            cursorcol -= 1
    delete_key_pressed = False
"""
the text editors internal format goes like:
row1:hello indent
row2:world indent
None
(still wip)
TODO: finish the row system, then column UPDATE: column system COMPLETE. now just rows..
i accidentally designed the whole system around 1 row.. shit
h|e|l|l|o
1 2 3 4 5
"""
def loop():
    global testgrid
    while True:#main editor loop
        fileio.readfile()
        stdin()
        cursor()
        check_item_on_left()
        testgrid = [char for item in file for char in item]
        fileio.writefile()
        print(file)
def testfunc():
    print("test passed")
