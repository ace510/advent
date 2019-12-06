input_clean = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,35,92,225,1101,25,55,225,1102,47,36,225,1102,17,35,225,1,165,18,224,1001,224,-106,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1101,68,23,224,101,-91,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,2,217,13,224,1001,224,-1890,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,69,77,224,1001,224,-5313,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,102,50,22,224,101,-1800,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1102,89,32,225,1001,26,60,224,1001,224,-95,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,51,79,225,1102,65,30,225,1002,170,86,224,101,-2580,224,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,101,39,139,224,1001,224,-128,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,54,93,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1005,224,329,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,419,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,677,226,224,1002,223,2,223,1006,224,449,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,1007,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,524,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,539,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,554,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
input_var = 5

input_dirty = input_clean[:]
halting = False
index = 0

def reverse(string):
    output = "".join(reversed(string))    
    return output



while  not halting:
    output = 'Vince'
    instruction_length = 4
    instruction_slice = input_dirty[index:index+4]


    opcode_and_param = reverse(str(input_dirty[0+index]))
    #print(f'the whole parameter bundle is{opcode_and_param}')

    op_code = int(opcode_and_param[:2].rstrip('0'))
    #print(f'the opcode is {op_code}')

    try:
        operand1_mode = int(opcode_and_param[2])
    except IndexError:
        operand1_mode = 0
    try:
        operand2_mode = int(opcode_and_param[3])
    except IndexError:
        operand2_mode = 0
    try:
         output_loc_mode = int(opcode_and_param[4])
    except IndexError:
        output_loc_mode = 0





    if operand1_mode ==1:
        operand1 = input_dirty[1+ index]
    elif operand1_mode == 0: 
        operand1 = input_dirty[input_dirty[1+ index]   ]
    else:
        operand1 = None

    if operand2_mode ==1:
        operand2 = input_dirty[2+ index]
    elif operand2_mode == 0 and op_code in (1,2,5,6,7,8):
        operand2 = input_dirty[input_dirty[2+ index]   ]
    else:
        operand2 = None
    
    try:
        output_loc = input_dirty[3+ index]
    except IndexError:
        print(f'{op_code} better be 99')
    

    if op_code == 1:
        output = operand1 + operand2
    elif op_code == 2:
        output = operand1 * operand2
    elif op_code == 3:
        instruction_length = 2
        output_loc = input_dirty[1+ index]
        output = input_var
    elif op_code == 4:
        instruction_length = 2
        # output_loc = input_dirty[1+ index]
        print(f'printing {operand1}')
    elif op_code == 5:
        instruction_length = 3
        if operand1 != 0:
            instruction_length = 0
            index = operand2
    elif op_code == 6:
        instruction_length = 3
        if operand1 == 0:
            instruction_length = 0
            index = operand2
    elif op_code == 7:
        if operand1 < operand2:
            output = 1
        else:
            output = 0
    elif op_code == 8:
        if operand1 == operand2:
            output = 1
        else:
            output = 0
    elif op_code == 99:
        halting = True
        break
    else:
        print(f'opcode {op_code} not found halting')
        halting = True
    
    if output != 'Vince':    
        input_dirty[output_loc] = output
    index += instruction_length