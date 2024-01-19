l = input()
arr = [i for i in l.split('-')]
sub_sum = []

for a in arr:
    i = map(int, a.split('+'))
    sub_sum.append(sum(i))

answer = sub_sum.pop(0)
for s in sub_sum:
    answer -= s
print(answer)    