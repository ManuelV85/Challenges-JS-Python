import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

int_to_str = list(map(lambda str_num: str(str_num), numbers)) 
print (int_to_str)

f=[]
s=[]
t=[]

for i in range (3):
    f.append(random.randint(0, len(int_to_str)-1))
    s.append(random.randint(0, len(int_to_str)-1))
for i in range (4):
    t.append(random.randint(0, len(int_to_str)-1))


print (f"+({f[0]}{f[1]}{f[2]}) {s[0]}{s[1]}{s[2]}-{t[0]}{t[0]}{t[0]}{t[0]}")