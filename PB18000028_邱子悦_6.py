import math

a=[
   [31,-13,0,0,0,-10,0,0,0],
   [-13,35,-9,0,-11,0,0,0,0],
   [0,-9,31,-10,0,0,0,0,0],
   [0,0,-10,79,-30,0,0,0,-9],
   [0,0,0,-30,57,-7,0,-5,0],
   [0,0,0,0,-7,47,-30,0,0],
   [0,0,0,0,0,-30,41,0,0],
   [0,0,0,0,-5,0,0,27,-2],
   [0,0,0,-9,0,0,0,-2,29]
  ]
b=[-15,27,-23,0,-20,12,-7,7,10]
n=9

for i in range(0,n):
    k=i
    for j in range(i+1,n):
        if(math.fabs(a[k][i])<math.fabs(a[k][j])):
            k=j
    for j in range(i,n):
        t=a[i][j]
        a[i][j]=a[k][j]
        a[k][j]=t
    t=b[i]
    b[i]=b[k]
    b[k]=t
    for j in range(i+1,n):
        a[j][i]/=a[i][i]
        for k in range(i+1,n):
            a[j][k]-=a[j][i]*a[i][k]
        b[j]-=a[j][i]*b[i]
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        b[i]-=a[i][j]*b[j]
    b[i]/=a[i][i]

for i in range(0,n):
    print("x{}={:.15e}".format(i+1,b[i]))
