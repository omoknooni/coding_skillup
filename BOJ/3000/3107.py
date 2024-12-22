import sys
input = sys.stdin.readline
ipv6 = input().rstrip()

ipv6 = ipv6.split(":")

# :: 으로 시작하거나 끝나는 것들은 split하면 공백 2개 생김
if ipv6[0] == "":
    ipv6 = ipv6[1:]
if ipv6[-1] == "":
    ipv6 = ipv6[:-1]

answer = ""
for i in ipv6:
    if i == "":
        answer += "0000:" * (8-len(ipv6)+1)
    else:
        # zfill : 자릿수 맞게 앞에 0채우기
        answer += i.zfill(4) + ":"
print(answer.rstrip(":"))
