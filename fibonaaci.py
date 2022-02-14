"""
Creating a python function that when you input 
a number the function you have created checks 
whether the number belongs to the Fibonacci 
sequence or not.
   
"""


# Declaring the function

def checking_fibonaaci():
    
    # User enters a prefered number
    check_number = int(input("Enter Number: "))
    
#Taking the first three numbers 0,1 and 1 of the Fibonacci sequence

    first_number = 0
    second_number = 1
    third_number = 1

# checking user enters a 0 & 1

    if (check_number == 0 or check_number == 1):
        print("The Number belongs to Fibonacci Sequence")

# To calculate the Fibonacci number at position n, 
# you store the first two numbers of the sequence, 0 and 1, in cache. 
# Then, calculate the next numbers consecutively until you can return cache[n].

    else:
        while first_number < check_number:
            first_number = second_number + third_number
            third_number = second_number
            second_number = first_number
        if first_number == check_number:
            print("The Number belongs to Fibonacci Sequence")
        else:
            print("The Number doesn't belong to Fibonacci Sequence")

# Call the function    
checking_fibonaaci()