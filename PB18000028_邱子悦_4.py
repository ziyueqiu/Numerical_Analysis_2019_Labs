import math

def f(x):
        return math.sin(x)

def T(a,b,N):
        h=(b-a)/N
        I=(f(a)+f(b))/2*h
        for i in range(1,N):
                I+=h*f(a+i*h)
        return I

def S(a,b,m):
        h=(b-a)/m
        I=(f(a)+f(b)+4*f(a+h))/3*h
        for i in range(1,int(m/2)):
                I+=h*(4*f(a+h+i*h*2)+2*f(a+i*h*2))/3
        return I

#上下限
a=1
b=5

k=2

#实际值
s=math.cos(1)-math.cos(5)
#print(s)

print("复化梯形积分")
for l in range(1,13):
        N=2**l
        s1=T(a,b,N)
        e1=math.fabs(s1-s)
        o1=math.log(e1/math.fabs(T(a,b,k*N)-s))/math.log(k)
        print("数值积分值={:.15e},误差={:.15e},误差阶={:.15e}".format(s1,e1,o1))

print("\n")
print("复化Simpson积分")
for l in range(1,13):
        N=2**l
        s2=S(a,b,N)
        e2=math.fabs(s2-s)
        o2=math.log(e2/math.fabs(S(a,b,k*N)-s))/math.log(k)
        print("数值积分值={:.15e},误差={:.15e},误差阶={:.15e}".format(s2,e2,o2))
