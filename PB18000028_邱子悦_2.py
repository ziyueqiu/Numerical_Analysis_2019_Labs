import math

nums=[5,10,20,40]

def func(x):
    return 1/(1+x**2)

def lg1(t,num):
        fx=0
        x=[]
        y=[]
        for i in range(num+1):
            x.append(-5+10*i/num)
            y.append(func(x[i]))
        for i in range(num+1):
            tmp=1
            for j in range(i):
                tmp*=(t-x[j])/(x[i]-x[j])
            for j in range(i+1,num+1):
                tmp*=(t-x[j])/(x[i]-x[j])
            fx+=tmp*y[i]
        return fx
        #print(fx)

def lg2(t,num):
        fx=0
        x=[]
        y=[]
        for i in range(num+1):
            x.append(-5*math.cos((2*i+1)*math.pi/(2*num+2)))
            y.append(func(x[i]))
        for i in range(num+1):
            tmp=1
            for j in range(i):
                tmp*=(t-x[j])/(x[i]-x[j])
            for j in range(i+1,num+1):
                tmp*=(t-x[j])/(x[i]-x[j])
            fx+=tmp*y[i]
        return fx
        #print(fx)

for num in nums:
    max1=0
    for j in range(501):
        y=-5+10*j/500
        z=math.fabs(func(y)-lg1(y,num))
        if z>max1:
            max1=z
    print("n={}".format(num))
    print("等距节点误差为{:.15e}".format(max1))

for num in nums:
    max2=0
    for j in range(501):
        y=-5+10*j/500
        z=math.fabs(func(y)-lg2(y,num))
        if z>max2:
            max2=z
    print("n={}".format(num))
    print("余弦节点误差为{:.15e}".format(max2))

