def none():
    a=['abc' ,'xyz' ,'123' ,'qqq' ,None,'edfg']
    for i in a:
        if i ==None:
            continue
        return a
o=none()
print(o)