squad = []
for i in range(3):
    x,y = map(int, input().split())
    squad.append([x,y])

if squad[0][0] != squad[1][0]:
    # y = mx + n
    m = (squad[0][1] - squad[1][1]) / (squad[0][0] - squad[1][0])
    n = squad[0][1] - (m * squad[0][0])
    if squad[2][1] == m * squad[2][0] + n:
        print('WHERE IS MY CHICKEN?')
    else:
        print('WINNER WINNER CHICKEN DINNER!')
else:
    if squad[2][0] == squad[0][0]:
        print('WHERE IS MY CHICKEN?')
    else:
        print('WINNER WINNER CHICKEN DINNER!')