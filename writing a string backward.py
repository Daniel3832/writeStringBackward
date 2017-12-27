def writeBackward1(string):
    if string == "":
        return string
    else:
        return string[len(string)-1]+writeBackward(string[0:len(string)-1])

def writeBackward2(s):
    if s== "":
        return s
    else:
        return writeBackward2(s[1:]) + s[0]

s = raw_input()
print writeBackward2(s)

