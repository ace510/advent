
start = 357253
end = 892942
decrease_set = list()
subsequent_set = list()


for i in range(start, end + 1):
    digits_increase = True
    first_num = 0
    i_str = str(i)

    while digits_increase and first_num < 6:
        for second_num in range(first_num+1,6):
            if i_str[first_num] > i_str[second_num]:
                # print(f"{i_str} does not suffice")
                # print(f'{i_str[first_num]} is less than {i_str[second_num]}')
                digits_increase = False
        first_num += 1

    if digits_increase:
        decrease_set.append(i_str)

for i in decrease_set:
    subsequent_same = False
    index = 0
    while not subsequent_same and index < 5:
        if index == 0 and i[index] == i[index+1] and i[index] != i[index+2]:
            subsequent_same = True
        elif index == 4 and i[index] == i[index+1] and i[index] != i[index-1]:
            subsequent_same = True
        elif i[index] == i[index+1] and i[index] != i[index-1] and i[index] != i[index+2]:
            subsequent_same = True
        index += 1
    
    if subsequent_same:
        subsequent_set.append(i)

for i in subsequent_set:
    print(i)

print(len(subsequent_set))