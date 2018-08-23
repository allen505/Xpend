


def mess(self):
    # Open the file with read only permit
    f = open('bank1.txt', "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    # close the file after reading the lines.
    amt1 = ''
    for i in lines:
        i = i.lower()

        if i.startswith('rs.'):
            for j in i:
                if not j.isalpha():
                    amt1 = amt1 + j
                    a = (amt1.split())
                    print(a[1])
                    for i in lines:
                        i = i.lower()
                        if i.find('debited') != -1:
                            (a[1]) = -float(a[1])
    print(float(a[1]))
    f.close()
    #change Xpnse to return the credited or debited amount and adjust accordingly in the calling function
    return Xpnse += a[1]


######################End of message################################################



######################End of Textext################################################