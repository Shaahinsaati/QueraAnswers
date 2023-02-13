daysOfWeek = ['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jome']

a = int(input())
da = input().strip().split(' ')
b = int(input())
db = input().strip().split(' ')
c = int(input())
dc = input().strip().split(' ')
list_days = da+db+dc
print(len(daysOfWeek)- len(set(list_days)))