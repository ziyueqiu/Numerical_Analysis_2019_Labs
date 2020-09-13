import math

def y_x(x,y):
    return -x*x*y*y

# Runge-Kutta
def runge(h):
    x = 0
    y = 3
    while(x < 1.5):
        k1 = y_x(x,y)
        k2 = y_x(x+h/2,y+k1*h/2)
        k3 = y_x(x+h/2,y+k2*h/2)
        k4 = y_x(x+h,y+k3*h)
        y += h/6*(k1+2*k2+2*k3+k4)
        x += h
    return math.fabs(y-3/(1+x*x*x))

error = []
h = []
for l in range(5):
    h.append(0.1/math.pow(2,l))
    error.append(runge(h[l]))

print("四阶Runge-Kutta公式的误差和误差阶")
for l in range(4):
    print("h = ",h[l],"err = {:.15e} ,ok = {:.15e}".format(error[l],math.log(error[l]/error[l+1])/math.log(2)))

# Adams
def adams(h):
    y0=y1=y2=y3=y4=3
    x = 0
    i = 0
    while(x<1.5):
        y0=y1
        y1=y2
        y2=y3
        y3=y4
        if(i<3):
            k1 = y_x(x,y3)
            k2 = y_x(x+h/2,y3+k1*h/2)
            k3 = y_x(x+h/2,y3+k2*h/2)
            k4 = y_x(x+h,y3+k3*h)
            y4=y3+h/6*(k1+2*k2+2*k3+k4)
        else:
            y4_=y3+h/24*(55*y_x(x,y3)-59*y_x(x-h,y2)+37*y_x(x-2*h,y1)-9*y_x(x-3*h,y0))
            y4=y3+h/24*(9*y_x(x+h,y4_)+19*y_x(x,y3)-5*y_x(x-h,y2)+y_x(x-2*h,y1))
        i+=1
        x+=h
    return math.fabs(y4-3/(1+x*x*x))

err = []
for l in range(5):
    err.append(adams(h[l]))

print("四阶隐式Adams公式")
for l in range(4):
    print("h = ",h[l],"err = {:.15e} ,ok = {:.15e}".format(err[l],math.log(err[l]/err[l+1])/math.log(2)))
