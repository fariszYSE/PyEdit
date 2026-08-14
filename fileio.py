import textedit
import os
def readfile():
    try:
        with open(textedit.file_name,"r") as f:
            textedit.file = f.read()
    except:
        writefile()
def writefile():
    with open(textedit.file_name,"w") as f:
        textedit.testgrid = "".join(textedit.testgrid)
        f.write(textedit.testgrid)