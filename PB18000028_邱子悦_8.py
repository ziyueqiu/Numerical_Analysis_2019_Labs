import math

a=[[3,2,5,4,6],[2,1,3,-7,8],[5,3,2,5,-4],[4,-7,5,1,3],[6,8,-4,3,8]]
b=[[3,2,5,4,6],[2,1,3,-7,8],[5,3,2,5,-4],[4,-7,5,1,3],[6,8,-4,3,8]]
P=[0,0,0,0,0]
Q=[0,0,0,0,0]
n=5
e=0.000001
sum=0

for i in range(n):
    for j in range(n):
        if(i!=j):
            sum+=a[i][j]*a[i][j]
v=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(n):
    v[i][i]=1

while(sum>e):
    max=0
    for i in range(n):
        for j in range(n):
            if(i!=j and math.fabs(a[i][j])>max):
                p=i
                q=j
                max=math.fabs(a[i][j])
    if(a[p][q]!=0):
        s=(a[q][q]-a[p][p])/(2*a[p][q])
        if(s==0):
            t=1
        else:
            t1=-s-math.pow(s*s+1,0.5)
            t2=-s+math.pow(s*s+1,0.5)
            if(math.fabs(t1)>math.fabs(t2)):
                t=t2
            else:
                t=t1
        c=1/math.pow(1+t*t,0.5)
        d=t/math.pow(1+t*t,0.5)
    else:
        c=1
        d=0

    for i in range(n):
        if(i!=p and i!=q):
            k1=c*a[p][i]-d*a[q][i]
            k2=c*a[q][i]+d*a[p][i]
            b[i][p]=b[p][i]=k1
            b[i][q]=b[q][i]=k2
    b[p][p]-=t*b[p][q]
    b[q][q]+=t*b[p][q]
    b[p][q]=0
    b[q][p]=0
    a=b

    for i in range(n):
        P[i]=c*v[i][p]-d*v[i][q]
        Q[i]=c*v[i][q]+d*v[i][p]

    for i in range(n):
        v[i][p]=P[i]
        v[i][q]=Q[i]
    
    sum = 0
    for i in range(n):
        for j in range(n):
            if(i!=j):
                sum+=a[i][j]*a[i][j]

print("r1 = {:.15e}".format(a[0][0]),end=" ")
print("v1 = [",end="")
for i in range(n-1):
    print("{:.15e}, ".format(v[i][0]),end="")
print("{:.15e}]".format(v[n-1][0]))

print("r2 = {:.15e}".format(a[1][1]),end=" ")
print("v2 = [",end="")
for i in range(n-1):
    print("{:.15e}, ".format(v[i][1]),end="")
print("{:.15e}]".format(v[n-1][1]))

print("r3 = {:.15e}".format(a[2][2]),end=" ")
print("v2 = [",end="")
for i in range(n-1):
    print("{:.15e}, ".format(v[i][2]),end="")
print("{:.15e}]".format(v[n-1][2]))

print("r1 = {:.15e}".format(a[3][3]),end=" ")
print("v1 = [",end="")
for i in range(n-1):
    print("{:.15e}, ".format(v[i][3]),end="")
print("{:.15e}]".format(v[n-1][3]))

print("r1 = {:.15e}".format(a[4][4]),end=" ")
print("v1 = [",end="")
for i in range(n-1):
    print("{:.15e}, ".format(v[i][4]),end="")
print("{:.15e}]".format(v[n-1][4]))
