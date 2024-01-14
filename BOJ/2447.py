# n = int(input())

# def square(size):
#     s = []
#     if size == 1:
#         return ['*']
#     sliced_size = int(size // 3)
#     block = square(sliced_size)
    
#     for i in block:
#         s.append(i*3)
#     for i in block:
#         s.append(i + ' '*sliced_size + i)
#     for i in block:
#         s.append(i*3)
#     return s

# for j in square(n):
#     print(j)

n = int(input())

field = [[0 for i in range(n)] for j in range(n)]

def square(size):
    global field

    if size == 3:
        field[0][:3] = field[2][:3] = [1,1,1]
        field[1][:3] = [1,0,1]
        return

    s_size = int(size // 3)
    square(s_size)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for block in range(s_size):
                field[s_size*i+block][s_size*j:s_size*(j+1)] = field[block][:s_size]

square(n)
for i in field:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()