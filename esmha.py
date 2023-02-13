adad_vorodi = int(input())
names = []
for i in range(adad_vorodi):
    names.append(len(set(input())))
print(max(names))