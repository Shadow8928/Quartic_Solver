a = int(input('enter A value'))
b = int(input('enter B value'))
c = int(input('enter C value'))
d = int(input('enter D value'))
e = int(input('enter E value'))
a_fac = []
e_fac = []
pos_zero = []
zero = []
for i in range(1,a+1):
    if a % i == 0:
        a_fac.append(i)
for i in range(1,e+1):
    if e % i == 0:
        e_fac.append(i)
for i in a_fac:
    for j in e_fac:
        pos_zero.append(j/i)
        pos_zero.append(-j/i)
for i in pos_zero:
    t = (a*(i**4))+(b*(i**3))+(c*(i**2))+(d*i)+e
    if t == 0:
        zero.append(i)
zero = set(zero)
print(zero)
