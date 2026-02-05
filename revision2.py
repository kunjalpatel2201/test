#list of dictionaries

# 1. Store student details and display them.
# Input:
# students = [
#  {'name':'Aarav','age':20,'marks':85},
#  {'name':'Diya','age':22,'marks':90}
# ]

#  students = [
#  {'name':'Aarav','age':20,'marks':85},
# {'name':'Diya','age':22,'marks':90}
#  ]

# for s in students:
#     print(s["name"],s["age"],s["marks"])

#2 Find student with highest marks.
# Input:
# [{'name':'A','marks':70},{'name':'B','marks':90}]
# Output:
# B has highest marks

# students = [{'name':'A','marks':70},{'name':'B','marks':90}]
# topper = max(students,key= lambda x : x["marks"])
# print(topper["name"],"has highest marks")

# 3. Count number of students.
# Input:
# [{'id':1},{'id':2},{'id':3}]
# Output:
# Total students = 3

# students = [{'id':1},{'id':2},{'id':3}]
# print("total students = ",len(students))


#4  Update marks of a student.
# Input:
# {'name':'Rahul','marks':60} → update to 75
# Output:
# {'name':'Rahul','marks':75}

students = {'name':'Rahul','marks':60} 
students["marks"] = 75
print(students)

#5  Remove a student by name.
# Input:
# ['Amit','Neha','Ravi']
# Remove: Neha
# Output:
# ['Amit','Ravi']

students = ['Amit','Neha','Ravi']
students.remove("Neha")
print(students)

#DICTIONARY OF LISTS

#6Store employee data and display row-wise.
# Input:
# {'name':['Rohit','Sneha'],'salary':[50000,60000]}
# Output:
# Rohit 50000
# Sneha 60000

emp = {'name':['Rohit','Sneha'], 'salary':[50000,60000]}
for i in range (len(emp["name"])):
    print(emp["name"][i],emp["salary"][i])

#7 Find average salary.
# Input:
# {'salary':[30000,40000,50000]}
# Output:
# Average salary = 40000

data = {'salary':[30000,40000,50000]}
average = sum(data["salary"]) // len(data["salary"])
print("average salary=",average)


#8 Add new employee details.
# Input:
# {'name':['A'],'salary':[20000]}
# Add: B, 30000
# Output:
# {'name':['A','B'],'salary':[20000,30000]}

emp = {'name':['A'],'salary':[20000]}
emp["name"].append("b")
emp["salary"].append(30000)

print(emp)

# #9 Count total employees.
# Input:
# {'name':['A','B','C']}
# Output:
# Total employees = 3

emp = {'name':['A','B','C']}
total = len(emp["name"])
print(total)

#10 Find highest salary.
# Input:
# {'salary':[25000,45000,30000]}
# Output:
# Highest salary = 45000

data = {'salary':[25000,45000,30000]}
highest = max(data["salary"])
print("highest")

#11 Store marks and calculate total.
# Input:
# [['Anu',80,90],['Raj',70,75]]
# Output:
# Anu total = 170
# Raj total = 145

data = [['Anu',80,90], ['Raj',70,75]]
for s in data:
    print(s[0],"total =",s[1]+s[2])

#12 Find maximum value from list of lists.
# Input:
# [[1,2,3],[4,5,6]]
# Output:
# Maximum = 6

lst = [[1,2,3],[4,5,6]]

max_val = max(max(i) for i in lst)
print("Maximum =", max_val)

#13 Convert list of lists to flat list.
# Input:
# [[1,2],[3,4]]
# Output:
# [1,2,3,4]

lst = [[1,2],[3,4]]

flat = []
for i in lst:
    flat.extend(i)

print(flat)


#14. Count number of rows.
# Input:
# [[1,2],[3,4],[5,6]]
# Output:
# Rows = 3

data = [[1,2],[3,4],[5,6]]

print("Rows =", len(data))

#15  Find student with highest total.
# Input:
# [['A',50,50],['B',60,70]]
# Output:
# B

data = [['A',50,50],['B',60,70]]
top = max(data,key = lambda x:x[1]+x[2])
print(top[0])

#16
# Store product details.
# Input:
# {101:{'name':'Pen','price':10}}
# Output:
# Product 101 Pen 10

product = {101:{'name':'Pen','price':10}}
for pid,details in product.items():
    print("product",pid,details["name"],details["price"])

# 17. Find product with highest price.
# Input:
# {1:{'price':10},2:{'price':20}}
# Output:
# Product ID 2

product = {1:{'price':10},2:{'price':20}}
max_id = max(product,key = lambda x:product[x]["price"])
print(max_id)

# 18. Update product stock.
# Input:
# {'stock':5} → update to 8
# Output:
# Stock updated

product = {'stock':5}
product["stock"] = 8
print("stoke updated")

# 19. Delete a product.
# Input:
# {1:{},2:{}}
# Delete key:1
# Output:
# {2:{}}

products = {1:{}, 2:{}}
del products[1]
print(products)

# 20. Count total products.
# Input:
# {1:{},2:{},3:{}}
# Output:
# Total products = 3

products = {1:{}, 2:{}, 3:{}}
print("Total products =", len(products))

#MIXED PROGRAMS 

# 21. Find average marks using list of dict.
# Input:
# {'marks':[80,90,100]}
# Output:
# Average = 90

data = {'marks':[80,90,100]}
marks = data["marks"]
average = sum(marks) / len(marks)
print(int(average))

# 22Convert dictionary of lists to list of dicts.
# Input:
# {'name':['A','B'],'age':[20,22]}
# Output:
# [{'name':'A','age':20},{'name':'B','age':22}]

data = {'name':['A','B'],'age':[20,22]}
result = []
for i in range(len(data["name"])):
    result.append({
        "name":data["name"][i],
        "age":data["age"][i]
    })
print(result)

#23 Sort list of dictionaries by key. 
# Input: [{'age':30},{'age':20}] 
# Output: [{'age':20},{'age':30}]

lst = [{'age':30}, {'age':20}]
lst.sort(key=lambda x: x['age'])
print(lst)

#24 Count occurrences using dict.
# Input:
# ['a','b','a','c']
# Output:
# {'a':2,'b':1,'c':1}

data = ['a', 'b', 'a', 'c']

count = {}
for item in data:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

print(count)


# 25. Merge two dictionaries.
# Input:
# {'a':1} and {'b':2}
# Output:
# {'a':1,'b':2}

dict1 = {'a': 1}
dict2 = {'b': 2}

dict1.update(dict2)
print(dict1)


