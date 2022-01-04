a=['y','y','y','n','y','y','n']
count=0
for i in a:
    count=count+1
    if i == 'n':
        print(count)
        continue