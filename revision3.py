#LIST OF DICTIONARY (1–8)

#1
data = [{"a":10,"b":20},{"a":5,"c":15},{"b":10,"c":5}]
result = {}
for d in data:
    for key,value in d.items():
        result[key] = result.get(key,0) + value
print(result)

#2
data = [{"a":1,"b":2},{"b":2,"a":1},{"a":2,"b":3}]
result = []
seen = set()
for d in data:
    t = tuple(sorted(d.items()))
    if t not in seen:
        seen.add(t)
        result.append(d)
print(result)

#3
data = [{"a":0,"b":0},{"a":1,"b":0},{"a":0,"b":2}]
result = [d for d in data if any(v != 0 for v in d.values())]
print(result)

#4
data = [{"x":10,"y":20},{"x":5,"y":30}]
total = {}
for d in data:
    for k,v in d.items():
        total[k] = total.get(k,0)+v
print(max(total,key = total.get))

#5
data = [{"name":"A","score":90},{"name":"B","score":80}]
result = {}
for d in data:
    for k,v in d.items():
        result.setdefault(k,[]).append(v)
print(result)

#6
data = data = [{"a":1,"b":2},{"a":5},{"a":2,"b":1}]  
print(sorted(data,key = lambda d: sum(d.values())))    

#7 
data = [{"a":1},{"b":2}]
keys = set().union(*data)
result = [{k:d.get(k,0)for k in keys}for d in data]
print(result)

#8
data = [{"a":1,"b":1},{"a":1,"b":2}]
print(max(data,key = lambda d:len(set(d.values()))))

#DICT OF LIST 

#9
data = {"a":[1,2,2],"b":[3,3,4]}
print({k:list(dict.fromkeys(v))for k,v in data.items()})

#10
data = {"a":[1,2],"b":[2,3]}
result = {}
for k ,values in data.items():
    for v in values:
        result.setdefault(v,[]).append(k)
print(result)

#11
data = {"a":[1,2],"b":[10],"c":[2,2]}
print({k:v for k,v in data.items()if sum(v) >= 5})

#12
d = {"x":[3,1],"y":[2,3]}
print(sorted(set(sum(d.values(), []))))

#13
data = {"a":[1],"b":[1,2,3]}
print(max(data,key = lambda k:len(data[k])))

#14
data = {"a":[1,2],"b":[3]}
print(sum(len(v)for v in data.values()))

#15
data = print({k: sum(v)//len(v) for k,v in d.items()})

#LIST OF LIST (16–22)
#16
data = [[1,2],[3,4]]
print(list(map(list, zip(*data[::-1]))))

#17
data = [[1,2],[3,3],[4,5]]
print([x for x in data if sum(x) % 2 != 0])

#18
data = [[1,2],[3,4]]
print([[sum(r)-x for x in r] for r in data])

#19
data = [[1,2,3],[4,5,6],[7,8,9]]
print([data[i][i] for i in range(len(data))])

#20
data = [[1,2],[3,4]]
print(sum(data, []))

#21
lst = [[1,2],[5],[3,4]]
print(max(lst, key=sum))

#22
data = [[1,2],[2,1],[1,2]]
result = []
for x in result:
    if x not in result:
        result.append(x)
print(result)

#DICT OF DICT (23–30)

#23
data = {"a":{"x":1},"b":{"y":2}}
print({f"{k}.{ik}":iv for k,v in data.items() for ik,iv in v.items()})

#24
data = {"p1":{"a":10},"p2":{"a":20}}
print(max(data,key = lambda k: sum(data[k].values())))

#25
data = {"x":{"a":1},"y":{"a":2}}
result = {}
for o,inner in data.items():
    for k,v in inner.items():
        result.setdefault(k, {})[0]=v
print(result)

#26
data = {"a":{"x":0,"y":2},"b":{"x":1,"y":0}}
print({k:{ik:iv for ik,iv in v.items() if iv!=0} for k,v in data.items()})

#27
#data = {"a":{"x":1}}, {"a":{"x":4,"y":2}}

#28
data = {"a":{"x":1,"y":2},"b":{"z":3}}
print(sum(len(v) for v in data.values()))

#29
data = {"a":{"x":1,"y":2},"b":{"x":5}}
print(list(set.intersection(*(set(v) for v in data.values()))))


#30
data = {"a":{"x":1},"b":{"y":2}}
print([(o,ik,iv) for o,v in data.items() for ik,iv in v.items()])
