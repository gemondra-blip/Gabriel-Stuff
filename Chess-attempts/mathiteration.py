def main():
    try:
        x=input("Type a number yo or type c to cancel or type L to start a list or P for the second version:\n" )
        if x=="c":
            return 0
        elif x=="L":
            listmaker()
            return
        elif x=="P":
            Listmaker2()
            return
        x=int(x)
        reiteration(x)
    except ValueError:
        print("you didn't choose the options try again:")
        main()
def reiteration(x,y=0):
    if (x%2==0):
        x=x//2
        print(x)
    else:
        x=x*3+1
        print(x)
    if (x==1 and y!=1):
        print("aay its done")
        main()
    elif (y==1 and x==1):
        return print("ay that one's done")
    else:
        reiteration(x,y)
def listmaker():
    length=int(input("How long this list gon be fr?\n" ))
    IntList=[]
    for i in range(length):
        IntList.append(int(input("ints only please:" )))
    for i in IntList:
        reiteration(i,1)
    print("Full list processed!")
    return 0
def Listmaker2():
    Intlist2=[]
    while True:
        y=input("put yo number (type d when ur done): ")
        if y=="d":
          break  
        Intlist2.append(int(y))
    for i in Intlist2:
        reiteration(i,1)


main()
