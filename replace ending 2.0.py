from hashlib import new


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = []
old = 'hpp'
new = 'h'
for x in filenames:
    if x.endswith("hpp"):
        index=x.index(old)
        newfilenames.append(x[:index]+new)
    else:
        newfilenames.append(x)

print(newfilenames)
    