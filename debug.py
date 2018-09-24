#prints string to a file

debug_FileName = "out.txt"

def change_file_name(s):
    debug_FileName = s

def print(s):
    with open("out.txt", "a") as f:
        f.write("%s\n"%(s))
