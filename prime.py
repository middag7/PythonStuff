someVal = False
a = 0;
while (a<1000):
    print(a)
    for i in xrange(2,a):
        if(a%i==0):
            someVal = False;
            break;
        else:
            someVal = True;
        
    if(someVal == True):
        print("It's a prime")
    else:
        print("It's not a prime")
    a = a + 4
            


'''

ladkahskdjask
'''
