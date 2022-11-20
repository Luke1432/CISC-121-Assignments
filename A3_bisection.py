"""
-------------------------------------------------------
Get the function from the user and convert it to a list
for future use by the program
-------------------------------------------------------
Parameters:
none
Returns:
new_function_list #list that contains the coefficients for the function
-------------------------------------------------------
"""
def get_function():
    function = input("Please input the coefficients for the function")
    function_list = function.split(" ")
    new_function_list = list();
    i = 0
    while i < len(function_list):
        new_function_list.append(float(function_list[i]))
        i += 1

    return new_function_list

"""
-------------------------------------------------------
Calculate the value of the function at a specific point
-------------------------------------------------------
Parameters:
function #list that contains the coefficients for the function
x_value #contains the value of x to calculate the value of the 
function at

Returns:
function_value #value of the function at x_value
-------------------------------------------------------
"""
def f(function, x_value):
    function_value = 0
    for i in range(0, len(function)):
        function_value += function[i] * x_value ** (len(function) - i - 1)
    return function_value


def bisection_algorithm(function, a, b):
    # calculate the midpoint of a and b
    m_i = (a + b) / 2

    # use the bisection algorithm to find the roots
    while not f(function, m_i) == 0:

        if f(function, a) > 0 and f(function, b) < 0 and f(function, m_i) > 0:
            a = m_i
        if f(function, a) > 0 and f(function, b) < 0 and f(function, m_i) < 0:
            b = m_i

        if f(function, a) < 0 and f(function, b) > 0 and f(function, m_i) > 0:
            b = m_i
        if f(function, a) < 0 and f(function, b) > 0 and f(function, m_i) < 0:
            a = m_i

        m_i = (a + b) / 2

    return m_i



test_1=[1, -7, 10]
a_1=1
b_1=4

test_2=[2, -13, 22, -8]
a_2=-1
b_2=1.5

test_3=[8, 0, 0, -1]
a_3=-1
b_3=3

print("The root for "+str(test_1)+" is "+str(round(bisection_algorithm(test_1, a_1, b_1))))
print("The root for "+str(test_2)+" is "+str(round(bisection_algorithm(test_2, a_2, b_2))))
print("The root for "+str(test_3)+" is "+str(round(bisection_algorithm(test_3, a_3, b_3))))

#get the function
function = get_function()

#get the max value for the interval with roots
a = float(input("a (min): "))
#get the min value for the interval with roots
b = float(input("b (max): "))

m_i=bisection_algorithm(function, a, b)

print(round(m_i, 3)) #print the root