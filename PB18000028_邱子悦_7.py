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

#(1)
print("Gauss-Seidel")
x1=[0,0,0,0,0,0,0,0,0]
x2=[0,0,0,0,0,0,0,0,0]

def compare(x1,x2,num):
    for i in range(num):
        if(math.fabs(x1[i]-x2[i])>0.0000001):
            return 1
    return 0

for u in range(n):
    x1[u]=x2[u]
for i in range(n):
    s=0
    for j in range(n):
        s+=a[i][j]*x2[j]
    x2[i]=(b[i]-s+a[i][i]*x2[i])/a[i][i]

count=1
while(compare(x1,x2,n)):
    count+=1
    for u in range(0,n):
        x1[u]=x2[u]
    for i in range(0,n):
        s=0
        for j in range(n):
            s+=a[i][j]*x2[j]
        x2[i]=(b[i]-s+a[i][i]*x2[i])/a[i][i]

print("迭代步数",count)
print("方程的解")
for i in range(0,n):
    print("x{}={:.15e}".format(i+1,x2[i]))

#(2)
print("SOR")

def compare(x1,x2,num):
    for i in range(num):
        if(math.fabs(x1[i]-x2[i])>0.0000001):
            return 1
    return 0

def equation(n,a,b,k):
    x1=[0,0,0,0,0,0,0,0,0]
    x2=[0,0,0,0,0,0,0,0,0]
    count=0
    while(1):
        count+=1
        for u in range(0,n):
            x1[u]=x2[u]
        for i in range(0,n):
            s=0
            for j in range(n):
                s+=a[i][j]*x2[j]
            x2[i]=k*(b[i]-s+a[i][i]*x2[i])/a[i][i]+(1-k)*x1[i]
        if(compare(x1,x2,n)==0):
            return count,x2
        if(count>=100):
            return count,x2

min=100
save=[0,0,0,0,0,0,0,0,0]

for i in range(1,100):
    k=i/50
    count,save=equation(n,a,b,k)
    if(count<min):
        w=k
        min=count
        x2=save
print("最佳迭代步数",min)
print("最佳松弛因子",w)
print("方程的解")
for i in range(0,n):
    print("x{}={:.15e}".format(i+1,x2[i]))
