import sys
input = sys.stdin.readline
r1 = input().rstrip()
r2 = input().rstrip()

# 기호 테이블
table = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
table2 = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}
table3 = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

# V,L,D는 한 번만, I,X,C,M은 연속해서 3번까지만
# 로마 -> 아라비아
def rtoa(rom_str):
    num = 0
    i = 0
    while i < len(rom_str):
        if i+1 < len(rom_str):
            # 연속문자(작은수가 앞에)로 표현가능한 부분
            if rom_str[i:i+2] in table2:
                num += table2[rom_str[i:i+2]]
                i += 2
                continue
        
        if rom_str[i] in table:
            num += table[rom_str[i]]
            i += 1
    return num


# 아라비아 -> 로마
def ator(num):
    tmp = ""
    while num > 0:
        # 큰 수부터 변환할 수 있는지 확인
        for i,v in table3.items():
            while num >= i:
                num -= i
                tmp += v
    return tmp


n1 = rtoa(r1)
n2 = rtoa(r2)
print(n1+n2)
print(ator(n1+n2))