li = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for row in li:
    for item in row:
        if item == 1 :
            print ("*",end="")
        else:
            print (" ",end="")
    print()