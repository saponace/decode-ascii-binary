import sys
from curses import ascii


def bin_to_integer(string):
    ret_val = 0
    for i in range(len(string)):
        if (string[i] == "1"):
            ret_val += 2**(7-i)
    return ret_val


filepath = sys.argv[1]
print(filepath)
with open(filepath) as buffer:
    output = ""
    oct = "beginning"
    while oct != "":
        oct = buffer.read(8)
        char = ascii.unctrl(bin_to_integer(oct))
        output += char
    print(output)


