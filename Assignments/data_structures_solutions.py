
# Part A: Lists 

# A1. First and last element
nums = [3, 1, 4, 1, 5]
print("A1 First:", nums[0], "Last:", nums[-1])

# A2. Length of a list
colors = ['red', 'blue', 'green']
print("A2 Length:", len(colors))

# A3. Append 'yellow'
colors = ['red', 'blue']
colors.append('yellow')
print("A3 After append:", colors)

# A4. Insert 'orange' at index 1
fruits = ['apple', 'banana']
fruits.insert(1, 'orange')
print("A4 After insert:", fruits)

# A5. Remove 'banana'
fruits = ['apple', 'banana', 'grapes']
fruits.remove('banana')
print("A5 After remove:", fruits)

# A6. Pop the last element
items = [10, 20, 30]
popped = items.pop()
print("A6 Popped value:", popped)

# A7. Check if 3 is in the list
nums = [1, 2, 3, 4]
print("A7 3 in list:", 3 in nums)

# A8. Slice [2, 3] from [0, 1, 2, 3, 4]
a = [0, 1, 2, 3, 4]
print("A8 Slice:", a[2:4])

# A9. Replace element at index 1 with 12
a = [5, 10, 15]
a[1] = 12
print("A9 After replace:", a)

# A10. Count how many times 2 appears
print("A10 Count of 2:", [1, 2, 2, 3, 2].count(2))


# Part B: Tuple


# B1. Second element

t = (10, 20, 30)
print("B1 Second element:", t[1])

# B2. Length of a tuple
print("B2 Length:", len(('a', 'b', 'c')))

# B3. Unpack (4, 5) into x and y
x, y = (4, 5)
print("B3 x =", x, "y =", y)

# B4. Check if 'b' is in the tuple

print("B4 'b' in tuple:", 'b' in ('a', 'b', 'c'))

# B5. Empty tuple and its type
empty = ()
print("B5 Empty tuple:", empty, "Type:", type(empty))

# B6. Concatenate (1, 2) and (3, 4)
print("B6 Concatenated:", (1, 2) + (3, 4))

# B7. Repeat (7,) three times
print("B7 Repeated:", (7,) * 3)

# B8. Index of 2 in (1, 2, 3, 2)
print("B8 Index of 2:", (1, 2, 3, 2).index(2))

# B9. Count of 2 in (1, 2, 3, 2)
print("B9 Count of 2:", (1, 2, 3, 2).count(2))

# B10. Single-element tuple containing 5
single = (5,)
print("B10 Single tuple:", single, "Type:", type(single))


# Part C: Sets 



# C1. Create a set from [1, 2, 2, 3]
s = set([1, 2, 2, 3])
print("C1 Set:", s)

# C2. Add 4 to {1, 2, 3}
s = {1, 2, 3}
s.add(4)
print("C2 After add:", s)

# C3. Remove 2 from {1, 2, 3}
s = {1, 2, 3}
s.remove(2)
print("C3 After remove:", s)

# C4. Check if 5 is in {1, 3, 5}
print("C4 5 in set:", 5 in {1, 3, 5})

# C5. Length of {10, 20, 30}
print("C5 Length:", len({10, 20, 30}))

# C6. Clear all elements from {1, 2, 3}
s = {1, 2, 3}
s.clear()
print("C6 After clear:", s)

# C7. Add 'c' to {'a', 'b'} only if it is missing
s = {'a', 'b'}
if 'c' not in s:
    s.add('c')
print("C7 Set:", s)

# C8. Remove duplicates from ['a', 'a', 'b']
unique = set(['a', 'a', 'b'])
print("C8 Unique:", unique)

# C9. Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("C9 Union:", set1 | set2)

# C10. Intersection of two sets
print("C10 Intersection:", set1 & set2)


# Part D: Dictionaries 


# D1. Print the name
d = {'name': 'Ali', 'age': 25}
print("D1 Name:", d['name'])

# D2. Add key 'city'
d['city'] = 'Lahore'
print("D2 After add:", d)

# D3. Change 'age' to 30
d = {'name': 'Ali', 'age': 25}
d['age'] = 30
print("D3 After change:", d)

# D4. Delete key 'age'
d = {'name': 'Ali', 'age': 25}
del d['age']
print("D4 After delete:", d)

# D5. Check if key 'salary' exists
d = {'name': 'Ali', 'age': 25}
print("D5 'salary' exists:", 'salary' in d)

# D6. Print all keys

d = {'a': 1, 'b': 2}
print("D6 Keys:", list(d.keys()))

# D7. Print all values

d = {'a': 1, 'b': 2}
print("D7 Values:", list(d.values()))

# D8. Print key-value pairs\
    
d = {'x': 10, 'y': 20}
for k, v in d.items():
    print("D8", k, "=", v)

# D9. Safely read 'score' from an empty dictionary
empty_d = {}
print("D9 Score:", empty_d.get('score', 0))

# D10. Dictionary from two lists
keys = ['a', 'b']
values = [1, 2]
print("D10 Dictionary:", dict(zip(keys, values)))





