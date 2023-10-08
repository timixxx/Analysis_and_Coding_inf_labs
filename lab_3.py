import re
import numpy as np
from PIL import Image
import collections


file = input("Enter the filename:")
my_string = np.asarray(Image.open(file),np.uint8)
sudhi = my_string
shape = my_string.shape
print ("Enetered string is:",my_string)
message = str(my_string.tolist())

c = {}


def create_list(message):
    list = dict(collections.Counter(message))
    list_sorted = sorted(iter(list.items()), key = lambda k_v:(k_v[1],k_v[0]),reverse=True)
    final_list = []
    for key,value in list_sorted:
        final_list.append([key,value,''])
    return final_list


#print("Shannon tree with merged pathways:")


def divide_list(list):
    if len(list) == 2:
       # print([list[0]],"::",[list[1]])               #printing merged pathways
        return [list[0]],[list[1]]
    else:
        n = 0
        for i in list:
            n+= i[1]
        x = 0
        distance = abs(2*x - n)
        j = 0
        for i in range(len(list)):               #shannon tree structure
            x += list[i][1]
            if distance < abs(2*x - n):
                j = i
    #print(list[0:j+1],"::",list[j+1:])               #printing merged pathways
    return list[0:j+1], list[j+1:]


def label_list(list):
    list1,list2 = divide_list(list)
    for i in list1:
        i[2] += '0'
        c[i[0]] = i[2]
    for i in list2:
        i[2] += '1'
        c[i[0]] = i[2]
    if len(list1)==1 and len(list2)==1:        #assigning values to the tree
        return
    label_list(list2)
    return c

code = label_list(create_list(message))
print("Shannon's Encoded Code:")
output = open("compressed.txt", "w+")          # generating output binary
letter_binary = []
for key, value in code.items():
    print(key, ' : ', value)
    letter_binary.append([key,value])
print("Compressed file generated as compressed.txt")

for a in message:
    for key, value in code.items():
        if key in a:
            #print(key, ' : ', value)
            output.write(value)
output = open("compressed.txt", "r")
intermediate = output.readlines()
bitstring = ""
for digit in intermediate:
    bitstring = bitstring + digit
uncompressed_string =""
code =""
for digit in bitstring:
    code = code+digit
    pos=0
    for letter in letter_binary:               # decoding the binary and genrating original data
        if code ==letter[1]:
            uncompressed_string=uncompressed_string+letter_binary[pos] [0]
            code=""
        pos+=1

print("Your UNCOMPRESSED data is:")

temp = re.findall(r'\d+', uncompressed_string)
res = list(map(int, temp))
res = np.array(res)
res = res.astype(np.uint8)
res = np.reshape(res, shape)
print("Input image dimensions:",shape)
print("Output image dimensions:",res.shape)
data = Image.fromarray(res)
data.save('uncompressed.png')
if sudhi.all() == res.all():
    print("Success")
