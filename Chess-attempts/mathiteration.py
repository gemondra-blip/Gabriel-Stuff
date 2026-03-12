import time
counter = 1
countersummary = {}
current_i = 0
GAS_lacher = 10



def counterfunction(y=0):

    global counter

    counter+=1

    if y==1:

        counter=0

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
        counterfunction(1)
        reiteration(x)

    except ValueError:

        print("you didn't choose the options try again:")
        main()

def reiteration(x,y=0):

    global GAS_lacher
    global countersummary
    global current_i

    counterfunction()
    time.sleep(0.5/counter)

    if (x==1 and y!=1):

        print(f'aay its done and it took {counter-1} times to do so')
        main()

    elif (y==1 and x==1):

        if (GAS_lacher==True):
            
            countercomparingfunction()
            return

        countersummary[current_i]=(counter-1)
        print(f'ay that one\'s done and it took {counter-1} times to do so\n')



        return

    if (x%2==0):

        x=x//2
        print(x)

    else:

        x=x*3+1
        print(x)

    reiteration(x,y)

def listmaker():

    global GAS_lacher
    global current_i

    length=int(input("How long this list gon be fr?\n" ))
    IntList=[]

    for i in range(length):

        IntList.append(int(input("ints only please:" )))

    for i in IntList:

        current_i = i
        counterfunction(1)
        reiteration(i,1)

    GAS_lacher=True
    reiteration(1,1)
    print("Full list processed!")

    return 0

def Listmaker2():
    global GAS_lacher
    global current_i
    
    Intlist2=[]

    while True:

        y=input("put yo number (type d when ur done): ")

        if y=="d":

          break 

        Intlist2.append(int(y))

    for i in Intlist2:
        print(f'{i}')
        current_i = i
        counterfunction(1)
        reiteration(i,1)
    
    GAS_lacher=True
    reiteration(1,1)

    print("Full list processed!")

    return

def countercomparingfunction(y=0):

    global counter
    global countersummary
    global current_i
    global GAS_lacher
    text1=''
    text2=''

    first_key, first_value = next(iter(countersummary.items()))
    first_value2=first_value
    text2=(f'{first_key} had the smallest number of interations coming at {first_value}')
    text1=(f'{first_key} had the greatest number of interations coming at {first_value}')
    
    for i, j in countersummary.items():
        
        if first_value<=j:

            first_value=j
            text1=(f'{i} had the greatest number of interations coming at {j}')

        if first_value2>j:

            currentsmallest=j
            text2=(f'{i} had the smallest number of interations coming at {j}')

    GAS_lacher=False
    print(f'{text1}\n\n{text2}')
    return
    

main()
