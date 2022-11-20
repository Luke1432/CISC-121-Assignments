n=int(input("Amount of terms for fibonacci number: "))

number_list=[0, 1, 1]

i=2
number=0

while i<=n:
    number+=number_list[i-1]
    number_list.append(number)
    i += 1
print(number_list[len(number_list)-1])