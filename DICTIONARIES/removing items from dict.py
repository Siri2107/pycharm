from re import S


d={"name":"siri","age":21,"class":15,"branch":"cse"}
print(d.popitem())
print(d.pop("name"))
print(d)

s=d.pop("age")
print(s)

print(d.clear())
print(d)

del d