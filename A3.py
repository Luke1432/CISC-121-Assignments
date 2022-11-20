def defineFunction(function):
    function_list = str(function).split()
    function_num_list = []
    for i in function_list:
        function_num_list.append(float(i))
    return function_num_list

def f(function, x_value):
    function_value=0

    for i in range(0, len(function_list)):
        function_value += function[i]*x_value**(len(function)-i-1)
    print(function_value)
    return function_value

def getZeroes(function):
    a_0=100
    b_0=-100
    c_0=(a_0+b_0)/2

    while not (f(function, c_0)==0):
        if(f(function, c_0)>0):
            a_0-=1
            b_0-=1
        elif(f(function, c_0)<0):
            a_0+=1
            b_0+=1
        c_0=(a_0+b_0)/2
        print(f(function, c_0))

    return c_0


function=input("Please input the coefficients for a function: ")
new_function=defineFunction(function)
print(getZeroes(new_function))

