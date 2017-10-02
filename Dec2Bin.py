close=1
while (close != "stop"):
    dec=input("\nPlease enter a POSITIVE decimal number GREATER THAN ONE: ")
    print
    a=[]#we will store all the remainders
    while (dec>1):
        decN=dec
        decR=dec%2
        dec=dec/2
        a.append(decR)
        print("%s / 2 = %s r %s")% (decN, dec, decR) #prints out user-entered decimal, prints out the answer when divided by 2, prints out remainder
    print("1 / 2 = 0 r 1")#cannot divide by zero, print out last line and find the remainder (1)
    a.append(1)#did not add the last remainder to the array above, I do it here
    a.reverse()#reverses array a so that it is in binary form
    numA=(16-len(a))#calculates the size of array finds the number of zeros needed to add infront of array a
    c=[0]*numA#creates an array of zeros with the number of zeros needed
    b=map(str, c+a)
    print("\nYour 16 Bit Binary Number is:")
    print "".join(b)#allows me to print the arrays without the [] , commas , and spaces
    print
    close=raw_input("Press any key to start over, or type \"stop\" to exit: ")
