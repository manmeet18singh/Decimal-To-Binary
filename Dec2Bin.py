close=1
while (close != "stop"):
    dec=input("\nPlease enter a POSITIVE decimal number GREATER THAN ONE: ")#Asks user for a positive decimal
    print#adds a new line makes things look nice
    a=[]#array with nothing in it this is where we will store all the remainders
    while (dec>1):#loops until the user-entered decimal is equal to 1
        decN=dec#stores the updated dec variable
        decR=dec%2#figures out the remainder by doing modulus divison and stores it into variable decR
        dec=dec/2#figures out the divison and updates the user-entered number so that the loop is not stuck in an infinite loop
        a.append(decR)#adds the remainder into array a
        print("%s / 2 = %s r %s")% (decN, dec, decR) #prints out user-entered decimal, prints out the answer when divided by 2, prints out remainder
    print("1 / 2 = 0 r 1")#since I cannot divide by zero, I just print out the very last line and find the remainder which is always 1
    a.append(1)#since I did not add the very last remainder to the array a above, I do it here
    a.reverse()#reverses array a so that it is in binary form
    numA=(16-len(a))#calculates the size of array a and because we need a 16 bit number, finds the number of zeros needed to add infront of array a
    c=[0]*numA#creates an array of zeros with the number of zeros needed from the calculation above
    b=map(str, c+a)#typecasts array a and b into strings and puts the zeros infront of the remainders
    print("\nYour 16 Bit Binary Number is:")
    print "".join(b)#allows me to print the arrays without the [] , commas , and spaces
    print #adds a new line to look tidy
    close=raw_input("Press any key to start over, or type \"stop\" to exit: ")
