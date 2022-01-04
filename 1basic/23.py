a=['y','y','y','n','y','y','m']
count=0
for i in a:
    count=count+1
    if i == 'n':
        print("n is",count)
    elif i == 'm':
        print("m is",count)
    elif i == 'y':
        print("y is",count)
        continue