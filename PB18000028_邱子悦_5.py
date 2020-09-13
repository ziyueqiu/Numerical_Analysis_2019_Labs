import math
dx=1.0E-8 #控制精度
MAX=20

#method1==Newton迭代法
def f(x):
    return x**3/3-x

def ff(x):
    return x**2-1

def g(x):
    return x-f(x)/ff(x)


def method1(x0):
    save=x0
    for k in range(1,MAX):
        x1=g(x0)
        if(math.fabs(x1-x0)<dx):
            print("初值={:.15e},根={:.15e},迭代步数={:.15e}".format(save,x1,k-1))
            return
        x0=x1
    print("在{:}附近f(x)无根".format(save))

list1=[0.1,0.2,0.9,9.0]
for x0 in list1:
    method1(x0)

#method2==弦截法
def method2(x1,x2):
    save=[x1,x2]
    f1=f(x1)
    for k in range(2,MAX):
        f2=f(x2)
        x=x2-f2*(x2-x1)/(f2-f1)
        if(math.fabs(x-x2)<dx or math.fabs(f(x))<dx):
            print("初值=({:.15e},{:.15e}),根={:.15e},迭代步数={:.15e}".format(save[0],save[1],x,k-1))
            return
        f1=f2
        x1=x2
        x2=x
    print("在{:}附近f(x)无根".format(save))

list2=[[-0.1,0.1],[-0.2,0.2],[-2.0,0.9],[0.9,9.0]]
for lx in list2:
    method2(lx[0],lx[1])
