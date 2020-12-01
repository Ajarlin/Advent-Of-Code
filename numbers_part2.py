file = open("nums.txt", "r")
mylist = []
for line in file:
    mylist.append(int(line))
#print(mylist)

target = 2020
two_nums_list = []
final_numbers = []

test = {}
for num1 in mylist:
     test[num1] = target-num1

print(test)
for num in mylist:
    for key, value in test.items():
        if value-num in two_nums_list:
            print([key, num, value-num])
            print()
            final_numbers.append(key)
            final_numbers.append(num)
            final_numbers.append(value-num)
        else:
            two_nums_list.append(num)

print(final_numbers[0]+final_numbers[1]+final_numbers[2])
print()
print(final_numbers[0]*final_numbers[1]*final_numbers[2])
