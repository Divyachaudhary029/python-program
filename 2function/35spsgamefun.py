def game(mix):
    import random
    i=0
    A=0
    B=0
    a=['stone' ,'paper', 'sessor']
    while i<5:
        b=input("enter value:")
        com=random.choice(a) 
        print(com)
        if b==com:
            print("drow")
        elif (b=='stone' and com=='paper') or (b=='paper'and com=='sessor') or (b=='sessor'and com=='stone'):
            A=A+1
            print("com wins",A)
        else:
            B=B+1
            print("you wins",B)
        i=i+1
        if(A>B):
            print("com wins tournamant")
        elif (A<B):
            print("you wins tournament")
        else:
            print("draw")
s=input()
o= list(input())
game(o)
         
            
