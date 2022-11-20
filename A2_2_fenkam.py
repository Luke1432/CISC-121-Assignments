""""
CISC-121 2022F
Name: Lukas Fenkam
Student Number: 20353712
Email: 21lrf7@queensu.ca
Date: 2022-10-05
I confirm that this assignment solution is my own work and
conforms to Queen’s standards of Academic Integrity """

f = open("C:\\Users\\Lukas Fenkam\\Documents\\University\\Queen's\\CISC 121\\friendship.txt", "r")  # opens the file containing the text
friendCounts = {}  # creates a dictionary for the names of the friends and the amount of repetitions
for line in f:  # for every line in the file
    friend_pair = line.strip("\n").split("\t")  # split the names
    for name in friend_pair:  # for every name in the pair
        if name not in friendCounts & name!=2:  # if the name is not in the list of friends
            friendCounts[name]=1  # add the name to the dictionary and set the count to 1
        else:  # if the name is in the list of friends
            friendCounts[name] += 1  # add one to the amount of friends of the

for name in friendCounts:  # for every name in the list of friends
    print(name+" has "+str(friendCounts[name])+" friends. ")  # print the name and the amount of friends the person has

sum_a=0
sum_b=0
