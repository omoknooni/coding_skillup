n = int(input())

solutions = []
# tower : pillar 1, 2, 3
def tower(disk_cnt, src, via, dst):
    if disk_cnt == 1:
        solutions.append([src, dst])            # 옮길 disk가 1개 -> 도착지로 옮기면 됨
    else:
        tower(disk_cnt-1, src, dst, via)        # n-1개의 disk를 중간 기둥으로
        solutions.append([src,dst])             # n번쨰 disk를 도착지(3번)기둥으로
        tower(disk_cnt-1, via, src, dst)        # 중간 기둥의 n-1개 disk를 도착지 기둥으로

tower(n, 1, 2, 3)
print(len(solutions))
for i in solutions:
    print(f'{i[0]} {i[1]}')