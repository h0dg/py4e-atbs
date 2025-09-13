counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

# .get(key, defaultvalue)
    # if key is in dictionary, return the value,
    # else, add key and set value to defaultvalue