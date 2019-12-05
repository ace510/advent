import random

''' (1,0,0,3,99)

[0] is opcode (1 Add, 2 multi, 99 Halt)
[1] is operand 1
[2] is operand 2
[3] output location

add 1(0) t0 1(0) and store in 3

[3] = 1
'''
input_clean = [1,12,2,3, # 3      1, 12, 2, 3
         1,1,2,3, # 7
         1,3,4,3, # 11
         1,5,0,3, # 15
         2,13,1,19, # 19
         1,9,19,23, # 23
         2,23,13,27,# 27
         1,27,9,31, #
         2,31,6,35, #
         1,5,35,39, #
         1,10,39,43, #
         2,43,6,47, #
         1,10,47,51, #
         2,6,51,55, #
         1,5,55,59, #
         1,59,9,63, #
         1,13,63,67, #
         2,6,67,71, #
         1,5,71,75, #
         2,6,75,79, #
         2,79,6,83, #
         1,13,83,87, #
         1,9,87,91, #
         1,9,91,95, #
         1,5,95,99, #
         1,5,99,103, #
         2,13,103,107, #
         1,6,107,111, #
         1,9,111,115, #
         2,6,115,119, #
         1,13,119,123, #
         1,123,6,127, #
         1,127,5,131, #
         2,10,131,135, #
         2,135,10,139, #
         1,13,139,143, #
         1,10,143,147, #
         1,2,147,151, #
         1,6,151,0,
         99,2,14,0,
         0]



# 1202 program alarm
# input[1] = 12
# input[2] = 2  

def orbital_comp(noun, verb):
    input_dirty = input_clean[:]
    halting = False
    index = 0
    input_dirty[1] = int(noun)
    input_dirty[2] = int(verb)
    while  not halting:
        output = 0
        op_code, output_loc = input_dirty[0+index], input_dirty[3+ index]
        operand1, operand2 = input_dirty[input_dirty[1+ index]], input_dirty[input_dirty[2+ index]]
        # op_code = input_dirty[0+index]
        # operand1 = input_dirty[input_dirty[1+ index]   ]
        # operand2 = input_dirty[input_dirty[2+ index]   ]
        # output_loc = input_dirty[3+ index]

        if op_code == 1:
            output = operand1 + operand2
        elif op_code == 2:
            output = operand1 * operand2
        elif op_code == 99:
            halting = True
            break
        else:
            halting = True
        input_dirty[output_loc] = output
        index += 4
    return input_dirty[0]


return_value = 42069
while return_value != 19690720:
    noun = random.randrange(0,100)
    verb = random.randrange(0,100)
    return_value = orbital_comp(noun, verb)
print(noun,verb)

