from operator import itemgetter

a = {1: "one", 2: "two"}
print(type(a))
print(id(a))
a[3] = "three"
print(a)
print(id(a))
for k, v in a.items():
    print(k, v)
for v in a.values():
    print(v)
for k in a.keys():
    print(k)
a = sorted(a.items(), key=itemgetter(0))
print(a)

