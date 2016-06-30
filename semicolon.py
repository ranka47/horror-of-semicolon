import sys
import os

cppAllowed = ("{", "}", ">", "else")

def cppRectify(fileName):
    nextLine = ""
    with open(fileName, 'r+') as file:
        lines = file.readlines()
        for i in range(0, len(lines) - 1):
            curLine = lines[i].rstrip()
            nextLine = lines[i+1].rstrip()
            if(len(curLine) == 0):
               pass
            elif(curLine.endswith(")}")):
                curLine = curLine[0:-2] + ");}"
            elif curLine.endswith(cppAllowed):
                pass
            elif(curLine[-1:] == ")" and nextLine.strip().startswith("{")):
                pass
            elif(curLine[-1:] == ")" and curLine.strip().startswith(("if", "else", "for"))):
                pass
            elif(curLine[-1:] != ";"):
                curLine = curLine + ";"
            curLine = curLine + "\n"
            lines[i] = curLine

    with open(fileName, 'w') as file:
        file.writelines(lines)

def main():
    files = sys.argv[1:]
    if(len(files) < 1):
        print "Input file not given"
        exit()
    for i in range(0, len(files)):
        fileName,extension = os.path.splitext(files[i])
        if (extension == ".c" or extension == ".cpp"):
            print "Rectifying " + files[i]
            cppRectify(files[i])

if __name__ == "__main__":
    main()