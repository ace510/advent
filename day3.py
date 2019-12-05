with open('day3data.txt','r') as input_file:
    payload1 = input_file.readline()
    payload2 = input_file.readline()

payload1lines = payload1.split(',')
payload2lines = payload2.split(',')

'''
U is up
D is down
R is right
L is left
'''



def calc_line(payloadlines):
    x=0
    y=0
    wire_length = 0
    payloadpoints = set()
    payloaddict = {}
    for i in payloadlines:
        x_vec= 0
        y_vec= 0

        if i[0] == 'U':
            y_vec = 1
        elif i[0] == 'D':
            y_vec = -1
        elif i[0] == 'R':
            x_vec = 1
        elif i[0] == 'L':
            x_vec = -1
        else:
            raise ValueError
        
        magnitude =int(i[1:])
        
        # print(f"moving {magnitude} with x equalling {x_vec} and y equalling {y_vec}")

        for _ in range(magnitude):
            x += x_vec
            y += y_vec
            wire_length += 1
            payloaddict[(x,y)] = wire_length

        # print(f"current coordinates are {x},{y}")

    return payloaddict
print('simulating Gibson routes')

payload1dict = calc_line(payload1lines)
payload2dict = calc_line(payload2lines)

print('Gibson routes simulated, hacking Gibson')
def mergeDict(dict1, dict2):
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = [value , dict1[key]]
 
   return dict3

overlay_dict = mergeDict(payload1dict, payload2dict)

search_space = len(overlay_dict)
search_index = 0.0
skinny_dict = {}

for key, value in overlay_dict.items():
    search_index += 1
    try:
        if len(value) > 1:
            skinny_dict[key] = value
        else:
            print(search_index/ search_space)
    except TypeError:
        pass
distance=9999999
distance_pair = 0

for key,value in skinny_dict.items():
    trial_value = value[0] + value[1]
    if trial_value < distance:
        distance = trial_value
        distance_pair = (key, value)

print(distance_pair)
print(distance)
