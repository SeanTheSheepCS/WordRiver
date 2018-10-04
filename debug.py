#prints string to a file

debug_FileName = "out.txt"

def change_file_name(s):
    debug_FileName = s

def print(s):
    with open(debug_FileName, "a") as f:
        f.write("%s\n"%(s))

def init():
    with open(debug_FileName,"w") as f:
        f.write("")
