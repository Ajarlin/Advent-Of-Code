file = open("nums.txt", "r")
mylist = []
for line in file:
    mylist.append(int(line))
print(mylist)

target = 2020
two_nums_list = []
final_numbers = []
for num in mylist:
    if target-num in two_nums_list:
        print([num, target-num])
        print()
        final_numbers.append(num)
        final_numbers.append(target-num)
    else:
        two_nums_list.append(num)

print()
print(final_numbers[0]*final_numbers[1])
