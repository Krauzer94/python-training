# Question 1
# Alongside this notebook, four CSV files are specified (one is in fact a TSV file).
# For each file, load it using the CSV module, and find the smallest and largest numbers in the data.
# All these files contain just lists of numbers - with the exception of a possible header row.

# `file1.csv`
import csv

file = './file1.csv'
print(f'{file}:')

with open(file) as f:
    for row in f:
        print(row, end='')

def min_max(file):
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Skip the header row
        data = []
        for row in reader:
            for element in row:
                data.append(element)

    return int(min(data)), int(max(data))

print('\n')
print(f'Smallest/largest: {min_max(file)}')


# `file2.csv`
file = './file2.csv'
print(f'{file}:')

with open(file) as f:
    for row in f:
        print(row.strip())

with open(file) as f:
    reader = csv.reader(f)
    data = list(reader)
    data = [[float(x) for x in row] for row in data]

def min_max(data):
    row_maxes = [max(row) for row in data]
    row_mins = [min(row) for row in data]
    
    max_ = max(row_maxes)
    min_ = min(row_mins)
    return min_, max_

print('')
print(f'Smallest/largest: {min_max(data)}')


# `file3.tsv`
file = './file3.tsv'
print(f'{file}:')

with open(file) as f:
    for row in f:
        print(row.strip())

with open(file) as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)  # Skip the header row
    data = list(reader)
    data = [[int(x) for x in row] for row in data]

def min_max(data):
    row_maxes = [max(row) for row in data]
    row_mins = [min(row) for row in data]
    
    max_ = max(row_maxes)
    min_ = min(row_mins)
    return min_, max_

print('')
print(f'Smallest/largest: {min_max(data)}')


# `file4.csv`
file = './file4.csv'
print(f'{file}:')

with open(file) as f:
    for row in f:
        print(row.strip())

with open(file) as f:
    reader = csv.reader(f, delimiter='|', quotechar='-')
    next(reader)  # Skip the header row
    data = list(reader)
    data = [[float(x) for x in row] for row in data]

def min_max(data):
    row_maxes = [max(row) for row in data]
    row_mins = [min(row) for row in data]
    
    max_ = max(row_maxes)
    min_ = min(row_mins)
    return min_, max_

print('')
print(f'Smallest/largest: {min_max(data)}')


# Question 2
# Given this data structure consisting of a list of dictionaries, write a function 
# that will write this data out to a file, where the column headers (in the first row) 
# are based on the dictionary keys, and the values are flattened out to one row per dictionary 
# (under the corresponding column header).
# Note that not all dictionaries contain all the same keys, nor are the keys necessarily in the same order when present.
# For "missing" values, your function should just write an empty string.

data = [
    {'a': '1_a', 'b': '1_b', 'c': '1_c'},
    {'c': '2_c', 'd': '2_d'},
    {'a': '3_a', 'c': '3_c', 'e': '3_e'}
]

# Your output file should look like this:
# a,b,c,d,e
# 1_a,1_b,1_c,,, 
# ,,2_c,2_d, 
# 3_a,,3_c,,3_e

out_file = './output.csv'

def flatten_to_csv(data, out_file):
    keys = {}
    for d in data:
        keys = keys | d.keys()
    keys = list(keys)
    flattened = [[d.get(key, '') for key in keys] for d in data]
    
    with open(out_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        for row in flattened:
            writer.writerow(row)

flatten_to_csv(data, 'test.csv')
