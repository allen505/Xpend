

def textext():
    # Open the file with read only permit
    f = open('prctxt.txt', "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    # close the file after reading the lines.
    amt=0
    amt1 = ''
    for i in lines:
        i = i.lower()

        if i.startswith('net amount '):
            for j in i:
                if not j.isalpha():
                    amt1 = amt1 + j
    a = (amt1.split())
    print(a[1])
    amt += a[1]
    f.close()
    return amt