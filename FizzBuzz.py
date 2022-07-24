Fizz = 3;
Buzz = 5;

for i in range(1,21):
    if (i % Fizz == 0) & (i % Buzz == 0):
        print("FizzBuzz") 
    elif i % Fizz == 0:
        print("Fizz")
    elif i % Buzz == 0:
        print("Buzz")
    else:
        print(i)