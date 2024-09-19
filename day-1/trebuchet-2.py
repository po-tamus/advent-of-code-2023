"""
store the "spelled out" numbers in an iterable
tokenize text
if value from iterable is in spliced text, store that value
treat digits the same way
"""

test_string = "abcone7"
spelled_out = "one, two, three, four, five, six, seven, eight, nine"
spelled_out = spelled_out.split(", ")
print(f"{spelled_out}")

# for num in spelled_out: 
#     if num in test_string: 
#         print(num)

test_dict = {}

for i, string in enumerate(spelled_out):
    test_dict[string] = str(i+1)

# print(test_dict) 

# string = "one"
# numeric = "1"

# group = [string, numeric]

# for i, value in enumerate(group): 
#     if not value.isnumeric(): 
#         group[i] = test_dict[value]

# print(group)

# # test string indexing
# print(string[0:3])
# print(len(string))

# print(f"{spelled_out} \n -----End of Test-----")

"""
END OF TESTING
"""

path = "./trebuchet-1.txt"

with open(path, "r") as f: 
    document = f.read()

document = document.split("\n")
print(document)

sum = 0
all_values = []

for line in document:

    # actual vales
    first = None
    latest = None
    cal_value = 0

    # for char in line: 
    #     # check if the char is a number
    #     if char.isnumeric(): 
    #         curr = char
    #         if first is None:
    #             first = char
    #         latest = char

    # indices
    head = 0
    tail = 0

    while tail < len(line):
        if line[tail].isnumeric(): 
            latest = line[tail]
            head = tail
            if first is None: 
                first = line[tail]
        else: 
            for num in spelled_out: 
                if num in line[head:tail+1]: 
                    head = tail
                    if first is None: 
                        first = num
                    latest = num
        tail+=1

    if latest is not None:
        # convert possible strings to ints using dictionary
        group = [first, latest]
        for i, value in enumerate(group):
            if not value.isnumeric(): 
                group[i] = test_dict[value]

        cal_value = int(group[0] + group[1])
    else: 
        cal_value = 0

    sum += cal_value
    all_values.append(cal_value)

print(f"The list of calibration values is: \n", all_values)
print(f"The sum of the calibration values is: {sum}.")