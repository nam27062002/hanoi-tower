a = 7007
def b(a):
    array = []
    for i in range(2,a,1):
        check = 0
        for j in range(2,i,1):
            if i%j == 0:
                check += 1
        if check == 0:
            array.append(i)
    return array
c = b(a)
s = 1
i = 0
a1 = a
a3 = 0
a4 = 1
while(s != a1):
    f = []
    if (a%c[i] != 0):
        i += 1
    else:
        s = s*c[i]
        a /= c[i] 
        if (s== a1):
            print(c[i],end = " ")
        else:
            print(c[i],"x",end = " ")
        a3 = c[i]