fib_sequence = [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
'''
REMINDER: FIBONACCI SEQUENCE IN PYTHON CODE IS
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

'''
inp =int(input())
list_out = []
for i in range(1,inp+1):
    if i in fib_sequence:
        list_out.append('+')
    else:
        list_out.append('-')
print(''.join(list_out))