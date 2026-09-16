import os
import fileio
import curses
import logging

logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG
)
file = [
    " "#<-cursor starts here
] #make screen a global variable in which it will allow all functions across the file to access it hassle free
lefty = False
screen = curses.initscr()
righty = False
cursorcol = 0
cursorrow = 0
delete_key_pressed = False
tempfile = file
key = ""
#fileinputname = screen.get_wch(cursorcol,cursorrow) #ask for input file
#ui
#screen = curses.initscr()
def on_start(screen):
    logging.info("program init...\n")
    screen.keypad(True)
    curses.noecho()
    curses.cbreak()
    global enter_key_pressed,file_name,testgrid
    file_name = "/home/farisz/programming/textedit/text.txt"#input("enter the absolute path to the file you want.. or if its in the same directory as the place the code is ran from you just enter the name. enter path here:\n")
    enter_key_pressed = False
    testgrid = [char for item in file for char in item]; screen.addstr(cursorrow,cursorcol,str(testgrid)) #flatten file into a character list
    logging.info("program done initializing, moving to main loop() function\n")
    loop(screen)
def string_to_list(turnlist):
    turnlist = [char for item in file for char in item]
def list_to_string(turnstring):
     global key,cursorcol,file
     turnstring = list(file);turnstring.insert(cursorcol, key);file = "".join(turnstring); cursorcol += 1
def stdin(screen):#read one keypress and set input flags
    global lefty, righty, delete_key_pressed,cursorcol,cursorrow,enter_key_pressed, key,file; key = screen.get_wch()
    #if key: in ("\x00", "\xe0"):#extended key, read the second code
    #key = screen.getch()
    if key == 19:#ctrl+s
        fileio.writefile()
        screen.clear()
        screen.addstr(0, 0, "file saved!")
        screen.refresh()
    if key == '\x13':
        fileio.writefile()
    if key == curses.KEY_LEFT:
        lefty = True
    elif key == curses.KEY_RIGHT:
        righty = True
    elif key == curses.KEY_UP:
        screen.addstr(cursorrow,cursorcol, "Up arrow")
    elif key == curses.KEY_DOWN:
        screen.addstr(cursorrow,cursorcol,"Down arrow")
    elif key == curses.KEY_BACKSPACE:
        delete_key_pressed = True
    elif key == curses.KEY_ENTER:
        enter_key_pressed = True
    else:
        if key != '\x13':
            line = list(file);line.insert(cursorcol, key);file = "".join(line); cursorcol += 1
        else:
            pass
def action_move_r():#consume right arrow input
    global righty
    if righty:
        righty = False
        return True
        screen.refresh()
    else:
        pass
def action_move_l():#consume left arrow input
    global lefty
    if lefty:
        lefty= False
        return True
        screen.refresh()
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
        cursorcol -= 1; #screen.addstr(cursorrow,cursorcol,str(cursorcol));screen.refresh()
    else:
        (cursorrow,cursorcol,cursorcol)
    if action_move_r() and cursorcol < len(testgrid):#right boundary check
        cursorcol += 1; #screen.addstr(cursorrow,cursorcol,str(cursorcol)); screen.refresh()
    else:
        pass
        #screen.addstr(cursorrow,cursorcol,str(cursorcol));screen.refresh()
def check_item_on_left():#inspect/delete the character left of the cursor
    global delete_key_pressed,cursorcol,file
    if delete_key_pressed:
        line = list(file)
        if line != []:
            line.pop(cursorcol -1)
            screen.clear()
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
TODO: finish the row system(done), then column UPDATE: column system COMPLETE. now just rows..
i accidentally designed the whole system around 1 row.. shit
h|e|l|l|o
1 2 3 4 5
"""
def loop(screen):
    try:
        global testgrid
        fileio.readfile()
        while True:#main editor loop
            stdin(screen)
            cursor()
            check_item_on_left()
            testgrid = [char for item in file for char in item]
            logging.info("about to write")
            fileio.writefile()
            logging.info("write function returned value")
            #screen.addstr(cursorrow,cursorcol,str(file))
            screen.refresh()

            screen.addstr(0, 0, str(file))
            screen.addstr(cursorrow,cursorcol,"")#trick curses into updating cursor position in real time by giving constant input
            #screen.addstr(cursorrow, cursorcol, str(cursorcol)) #commented out so it stops printing col number. you can uncomment for debuggin

            screen.refresh()
    except KeyboardInterrupt:
        logging.critical("keyboard interrupt\n")
        screen.addstr(0,0,"quitting..")
        fileio.writefile()
        screen.addstr(0,1,"done! exiting shortly")
        logging.info("program exited safely\n")

def testfunc():
    print("test passed")








