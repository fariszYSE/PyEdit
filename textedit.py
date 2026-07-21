import os
#import Tkinter as tk
#import tkFileDialog
#import tkMessageBox
file =input("write the absolute path to the file you wish to edit in absolutely no double or single quotes:\n")
textfile =""
os.system("")
with open("file","r") as f:
  data = f.read()
  textfile += data
print(f"data is: {data} \n")
print(f"textfile data is {textfile} \n")
def update():
    global textfile
    with open(file,"r") as f:
      data = f.read()
      textfile += data
      textfile += stdin
    print(f"new textfile is: {textfile}")
    with open(file,"w") as f:
       f.write(textfile)
while True:
  stdin = input()
  update()
