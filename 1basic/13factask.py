a=['y','y','y','n','y','y','n','m']
count=0
for i in a:
    count=count+1
    if i == 'n':
        print("n is",count)
        continue