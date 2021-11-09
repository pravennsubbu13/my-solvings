k=input()
m=['H','Q','9']
for i in range(len(k)):
    if k[i] in m:
        j=1
        break
    else:
        j=0
        continue
if j==1:
    print("YES")
elif j==0:
    print("NO")
