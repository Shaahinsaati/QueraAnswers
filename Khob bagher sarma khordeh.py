f_list = []
for each in range(5):
  line = input()
  if line.find("MOLANA")!=-1 or line.find("HAFEZ")!=-1:
    f_list.append(each+1)
if len(f_list):
  print(*f_list)
else:
  print("NOT FOUND!")