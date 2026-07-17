import sys
from Tkinter import *
from ScrolledText import *

# Initialize main window
root = Tk()
root.title("Python Text Editor - Windows Classic")
root.geometry("600x400")

# Create a text frame and scrollbar
text_area = ScrolledText(root, wrap=WORD)
text_area.pack(expand=True, fill='both')

# Run the application frame
root.mainloop()
