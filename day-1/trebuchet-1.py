"""
open and read document
import document into a string
separate into lines with split
parse each line, recording first and latest, use latest as last at the end of the line
this can be done with regex since the entire document is a string
keep a list of the calibration values or simply add the calibration values to a sum
"""

path = "./trebuchet-1.txt"

with open(path, "r") as f: 
    document = f.read()

document = document.split("\n")
print(document)

sum = 0
all_values = []

for line in document:

    first = None
    latest = None
    cal_value = 0

    for char in line: 
        # check if the char is a number
        if char.isnumeric(): 
            curr = char
            if first is None:
                first = char
            latest = char

    if latest is not None: 
        cal_value = int(first + latest)

    sum += cal_value
    all_values.append(cal_value)

print(f"The list of calibration values is: \n", all_values)
print(f"The sum of the calibration values is: {sum}.")