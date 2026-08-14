#dictionary --collection of key-value pairs 
#{unordered,mutable,indexed,cannot contain duplicate keys}

d={"key":"value",
    "bhumika":"goood",
    "marks":"98",
    }

d["key"] #prints "value"
print(d["key"])

print(d.items())
print(d.keys())
print(d.values())

d.update({"marks":87})
print(d)

d.update({"bhumika":92,"naina":89})
print(d)

print(d.get("naina"))
print(d.get("riya"))

d.copy()  # still does nothing unless assigned, e.g. d2 = d.copy()
print(d)

d.pop("bhumika")     # fixed: use pop() to remove by key
print(d)

print(len(d))

d.clear()
print(d)   # {}
