from __future__ import print_function

'''
Creates dictionary with color names 
matched to their RGB tuple values.
Color names are capitalized.
'''

def colors ():
    clrs = open("colors.txt", 'r')
    clr = {}                                #Dictionary that will be returned
    name = ""
    i = 0
    
    for line in clrs:
        list = line.strip().split()
        
        while (i < len(list)-1):
            name += list[i] + " "
            i += 1
        name = name.strip().upper()
        value = list[-1].split("-")
        value = (int(value[0]),int(value[1]),int(value[2]))
        clr[name] = value
        name = ""
        i = 0
       
    return clr
