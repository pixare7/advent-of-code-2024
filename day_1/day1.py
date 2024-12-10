# ------------------------------------------------------------------------

# Day 1 Part 1

# ------------------------------------------------------------------------

# opens the file in read mode
file = open('input.txt', 'r')

# initialize list to add info from .txt file
col1 = [] 
col2 = []
distance = 0

# loops over each row in the file, reads the lines and return list of strings
for row in file.readlines():
    row = row.rstrip("\n") # remove newline character if exists
    numbers = row.split() # split rows
    col1.append(int(numbers[0])) # convert from string to integer
    col2.append(int(numbers[1])) # convert from string to integer

col1.sort()
col2.sort()

for a, b in zip(col1, col2):
    distance += abs(a-b)

print(f"The total between the two lists is {distance}")
# part 1 solution: 2344935

# ------------------------------------------------------------------------

# Day 1 Part 2

# ------------------------------------------------------------------------

# opens the file in read mode
file = open('input.txt', 'r')

# initialize list to add info from .txt file
col1 = [] 
col2 = []
score = 0

# loops over each row in the file, reads the lines and return list of strings
for row in file.readlines():
    row = row.rstrip("\n") # remove newline character if exists
    numbers = row.split() # split rows
    col1.append(int(numbers[0])) # convert from string to integer
    col2.append(int(numbers[1])) # convert from string to integer

for num in col1:
    score += num*(col2.count(num))

print(f"The total similarity score is {score}")
# part 2 solution: 27647262
