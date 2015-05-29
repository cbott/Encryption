#Handles conversion between strings and numbers

def s2n(s):
    """returns number conversion of the string"""
    return sum((10**(3*i))*ord(c) for i, c in enumerate(s))

def n2s(n):
    """reverses effects of s2n()"""
    num = str(n)

    #correct for leading 0's being lost
    l = len(num)
    if l%3 == 1:
        num = "00" + num
    elif l%3 == 2:
        num = "0" + num

    text = ""
    for i in range(0,len(num),3):
        digits = int(num[i:i+3])
        char = chr(digits)
        text = char + text
    return text

##t = input("Text:")
##
##converted = s2n(t)
##print(converted)
##
##unconverted = n2s(converted)
##print(unconverted)
