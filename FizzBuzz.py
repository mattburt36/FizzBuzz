from re import I
from time import sleep

inNum = int(input("Please enter a number to run FizzBuzz to "))
Fizz = int(input("Please enter a number to mulitply FizzBuzz by "))
Buzz = int(input("Please enter a number to multiply FizzBuzz by "))

sleep(2)

FizzBuzz_List = [] 

def FizzBuzz(up_to, fizz, buzz):

    FizzBuzz_Tuple = ()

    for i in range(up_to):
        if (i % fizz == 0) & (i % buzz == 0):
            FizzBuzz_List.append((i, 'FizzBuzz'))
        elif i % fizz == 0:                        
            FizzBuzz_List.append((i, 'Fizz'))
        elif i % buzz == 0:        
            FizzBuzz_List.append((i, 'Buzz'))
        else:
            FizzBuzz_List.append((i, i))

    FizzBuzz_Tuple = tuple(FizzBuzz_List)

    print(FizzBuzz_Tuple)

    '''
    #While loop example
        i = 0 

        while i < up_to:

            if (i % Fizz == 0) & (i % Buzz == 0):
                print("FizzBuzz") 
            elif i % Fizz == 0:
                print("Fizz")
            elif i % Buzz == 0:
                print("Buzz")
            else:
                print(i)
    
            i = i + 1 
    '''   

    '''
    #For loop example 
        for i in range(up_to):
            if (i % Fizz == 0) & (i % Buzz == 0):
                print("FizzBuzz") 
            elif i % Fizz == 0:
                print("Fizz")
            elif i % Buzz == 0:
                print("Buzz")
            else:
                print(i)
    '''


FizzBuzz(inNum, Fizz, Buzz)