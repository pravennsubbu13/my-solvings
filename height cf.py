k=2
m=[int(k) for k in input().split(" ")]
j=m[0]
a=[int(j) for j in input().split(" ")]
c=0
b=m[1]
for i in a:
    if i>b:
        c=c+2
    else:
        c=c+1
print(c)

    
