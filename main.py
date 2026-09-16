#the starting point
import curses
import logging
with open("debug.log", "w") as f:
    f.write("")
logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG
)
from textedit import loop, on_start,file
logging.info("running textedit..\n")
logging.info(f"file before value:\n{file}\n")
curses.wrapper(on_start)
#on_start()
def gui():
    pass
print("log written in 'debug.log' file")



