x = int(input())
y = int(input())
field = 0
if x > 0:
    field = 1 if y > 0 else 4
else:
    field = 2 if y > 0 else 3
print(field)