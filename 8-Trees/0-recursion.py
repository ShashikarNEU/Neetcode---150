# You can refer to the notes on recursion
# Recursive
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

#Iterative
def iterative_factorial(n):
    result = 1
    while n>0:
        result*=n
        n-=1
    return result

# Function to print numbers recursively
def printnum(n):
    if n == 0:
        return 1
    print(n%10, end=" ")
    return printnum(n//10)

# Function to print numbers in order
# This function prints the digits in order because, it only print the n when going back(returning to the top)
def printnumOrder(n):
    if n == 0:
        return 1
    printnumOrder(n//10)
    print(n%10, end=" ")

# Reversing a number 
def iterative_reverse(n):
    s = 0
    while n > 0:
        s = s * 10 + n % 10
        n = n // 10
    return s

# Here you need to remember s variable also, include s as an argument in the function(recursive call is done on n//10)
# s will be updated in the final recursion so you return it and save it to get the final answer as s.
def recursive_reverse(n,s):
    if n == 0:
        return s
    s = s * 10 + n % 10
    x = recursive_reverse(n//10, s)
    return x
    
# Call the test function
if __name__ == "__main__":
    a = factorial(5)
    b = iterative_factorial(5)
    print(a,b)
    assert(a == b)

    # Recursion works like a stack, it goes into a new depth 
    # untill the termination condition. After the termination codn, 
    # the stack falls and each depth returns to the previous depth untill it reaches the starting

    # Some points to note
    # each depth should have a return statement to return the data to the previous depth, 
    # if there is no return, None will be returned
    c = printnum(1987) # 7 8 9 1
    print(" ")
    d = printnumOrder(1987) # 1 9 8 7
    print(c,d) # 1 None

    print(iterative_reverse(1987))
    print(recursive_reverse(1987,0))