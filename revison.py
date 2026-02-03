# 1. Recursive Digit Sum
# Input: 9875
# Output: 2 # (9+8+7+5 = 29 -> 2+9 = 11 -> 1+1 = 2)


# number = 9875

# while number>=10:
#     output = 0
#     while number > 0:
#         output += number % 10
#         number //= 10
#     number = output
# print(number)

# 2. Custom Map Function
# Input: square = lambda x: x*x, lst = [1, 2, 3]
# Output: [1, 4, 9]

# square = lambda x: x * x
# list = [1,2,3]
# output = []
# for i in list:
#     output.append(square(i))
# print(output)

#3. Variable Scope Problem
# Input: None
# Output: UnboundLocalError: local variable 'x' referenced before assignment

# x = 10
# def test():
#     print(x)
#     x = 5
# test()

#4 Flatten a Nested List
# Input: [1, [2, 3], [4, [5, 6]], 7]
# Output: [1, 2, 3, 4, 5, 6, 7]


# lst = [1, [2, 3], [4, [5, 6]], 7]
# result = []

# stack = lst[:]   

# while stack:
#     item = stack.pop(0)
#     if type(item) == list:
#         stack = item + stack
#     else:
#         result.append(item)

# print(result)

#5. List Rotation (Left by K)
# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [3, 4, 5, 1, 2]

# list = [1,2,3,4,5]
# k = 2
# for i in range(k):
#     first = list.pop(0)
#     list.append(first)
# print(list)

#6. Find Pairs With Sum
#Input: lst = [1, 5, 7, -1, 5], target = 6
#Output: [(1, 5), (7, -1)]

# lst = [1,5,7,-1,5]
# target = 6
# pairs = []
# used = set()
# for i in lst:
#     rem = target - i
#     if rem in used:
#         pairs.append((rem,i))
#     used.add(i)
# print(pairs)

#7. Modify a Tuple (Tricky Immutability)
# Input: tup = (1, [2, 3], 4); tup[1].append(5)
# Output: (1, [2, 3, 5], 4)

# tup = (1,[2,3],4)
# tup[1].append(5)
# print(tup)

#8. Find Missing Number Using Sets
# Input: A = [1, 2, 3, 4], B = [1, 2, 4]
# Output: Missing: 3

# A = [1,2,3,4]
# B = [1,2,4]

# missing = set(A) - set(B)
# print(missing.pop())

#9. Symmetric Difference of Sets

# Input: A = {1, 2, 3}, B = {3, 4, 5}
# Output: {1, 2, 4, 5}

# A = {1, 2, 3}
# B = {3, 4, 5}
# print(A ^ B)

#10 Group Anagrams
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# groups = {}
# for output in words:
#     key = ''.join(sorted(output))
#     if key not in groups:
#         groups[key] = []
#     groups[key].append(output)

# result = list(groups.values())
# print(result)

#11 Merge Nested Dictionaries
# Input:
# a = {'x': {'a': 1}}, b = {'x': {'b': 2}}
# Output: {'x': {'a': 1, 'b': 2}}

a = {'x': {'a': 1}}
b = {'x': {'b': 2}}

a['x'].update(b['x'])
print(a)

#12

#13. Duplicate Characters in String
# Input: "programming"
# Output: ['r', 'g', 'm']

s="programming"; d=[]
for c in s:
    if s.count(c)>1 and c not in d: d.append(c)
print(d)

#14 Class-level vs Instance-level Attributes
# Input: Set `cls.count = 0` and modify inside __init__
# Output: Different values for class and instance

class A:
    count=0
    def __init__(self): self.count=1

#15 Method Overriding Example
# Input: class A, class B(A)
# Output: Prints from overridden method in B

class A: 
    def show(self): print("A")
class B(A):
    def show(self): print("B")
B().show()

#16 Operator Overloading
# Input:
# v1 = Vector(1, 2); v2 = Vector(3, 4); v1 + v2
# Output: Vector(4, 6)

#17 Custom Exception
# Input: raise NegativeNumberError if input < 0
# Output: "NegativeNumberError: Negative value not allowed"
class NegativeNumberError(Exception): pass

n = -5
if n < 0:
    raise NegativeNumberError("Negative value not allowed")

#18 Safe File Open
# Input: read_file("no_file.txt")
# Output: FileNotFoundError caught -> "File does not exist!"
try:
    open("no_file.txt")
except FileNotFoundError:
    print("File does not exist!")

#19 Days Until Birthday
# Input: birthday = datetime.date(2025, 12, 25)
# Output: Days left: 162
import datetime
today = datetime.date(2025, 7, 16)
birthday = datetime.date(2025, 12, 25)

print("Days left:", (birthday - today).days)

#20 Date Range Generator
# Input: start = 2025-07-01, end = 2025-07-04
# Output: ['2025-07-01', '2025-07-02', '2025-07-03', '2025-07-04']
import datetime

start = datetime.date(2025,7,1)
end = datetime.date(2025,7,4)

dates = []
while start <= end:
    dates.append(str(start))
    start += datetime.timedelta(days=1)

print(dates)

#21 Diamond Pattern
n = 3

for i in range(1, n+1):
    print("*" * (2*i-1))

for i in range(n-1, 0, -1):
    print("*" * (2*i-1))

#22 Number Pyramid
n = 3

for i in range(1, n+1):
    print((str(i) + " ") * i)

#23 Read File Word Count
# Input: "hello world hello"
# Output: {'hello': 2, 'world': 1}
text = "hello world hello"
words = text.split()
count = {}
for w in words:
    count[w] = count.get(w,0)+1
print(count)

#24 CSV to Dictionary
# Input CSV: name,age\nAlice,30\nBob,25
# Output: [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]

#25 Custom Reduce (Multiply)
# Input: [1, 2, 3, 4]
# Output: 24
lst = [1,2,3,4]
result = 1
for i in lst:
    result *= i
print(result)

#26 Lambda With Condition
# Input: [1, 2, 3, 4]
# Output: ['Odd', 'Even', 'Odd', 'Even']
lst = [1,2,3,4]
result = list(map(lambda x: 'Even' if x%2==0 else 'Odd', lst))
print(result)

#27Time Logger Decorator
# Input: decorated function
# Output: "Execution time: 0.001s"

#28 Closure Access Counter
# Input: call f() 3 times
# Output: 1, 2, 3
def counter():
    count=0
    def inner():
        nonlocal count
        count+=1
        print(count)
    return inner

f=counter()
f(); f(); f()

#29 Dict to Key=Value Strings
# Input: {'a': 1, 'b': 2}
# Output: ['a=1', 'b=2']

d = {'a':1,'b':2}
res = [f"{k}={v}" for k,v in d.items()]
print(res)

#30 Swap Without Temp or Arithmetic
# Input: a = 5, b = 7 -> using tuple unpacking
# Output: a = 7, b = 5
a,b = 5,7
a,b = b,a
print(a,b)
