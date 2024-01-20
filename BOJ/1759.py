from itertools import combinations

l, c = map(int, input().split())
chars = input().split()
chars.sort()

vowels = ['a','e','i','o','u']
answers = []

for c in combinations(chars,l):
    passcode = ''.join(c)
    vowel_flag, consonant_flag = False, 0
    for i in passcode:
        if i in vowels:
            vowel_flag = True
        else:
            consonant_flag += 1
    
        if vowel_flag and consonant_flag >= 2:
            answers.append(passcode)
            break

for i in answers:
    print(i)