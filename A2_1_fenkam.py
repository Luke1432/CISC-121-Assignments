""""
CISC-121 2022F
Name: Lukas Fenkam
Student Number: 20353712
Email: 21lrf7@queensu.ca
Date: 2022-10-05
I confirm that this assignment solution is my own work and
conforms to Queen’s standards of Academic Integrity """
 

tryAgain=True #Variable that will check if the user wants to try again

while(tryAgain): #while the tryAgain variable is true

    numbers=input("Enter two numbers separated by a space: ").strip().split(" ") #Get the number

    try:
        numbers[0] = int(numbers[0])
    except ValueError:
        print("First number "+numbers[0]+" is invalid ")


    try:
        numbers[1] = int(numbers[1])
    except ValueError:
        print("Second number "+numbers[1]+" is invalid ")




    while (len(numbers) != 2) or ((int(numbers[0])) < -20) or (int(numbers[1]) > 20):
        try:
            numbers = input("Enter two numbers between -20 and 20 separated by a space: ").strip().split(" ")
        except Exception:
            numbers = input("The characters entered are invalid, please try again. ").strip().split(" ")


    firstNumber = int(numbers[0])
    secondNumber = int(numbers[1])


    if(firstNumber<secondNumber):
        i = firstNumber #set i to the first number

        while(i<secondNumber): #while i is smaller than the secondNumber
            i += 5
            if i>=secondNumber:
                break
            print(i)
    elif(secondNumber<firstNumber):
        i = firstNumber  # set i to the first number

        while (i > secondNumber) and (i<20) :  # while i is greater than the second number and i is smaller than 20 decrease the value of i and print i
            if i>=secondNumber:
                break
            print(i)
            i -= 5

    yesOrNo = (input("Would you like to try again? (yes/no) ")) #ask the user if he would like to try again

    if(yesOrNo=="yes"): #if the user inputted yes
        tryAgain=True #set the tryAgain variable to true

    else: #if the user did not input true
        tryAgain=False #set the tryAgain variable to false


