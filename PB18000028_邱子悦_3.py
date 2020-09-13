import math

#数据表
x=[0.25,0.50,0.75,1.00,1.25,1.50,1.75,2.00,2.25,2.50]
y=[1.284,1.648,2.117,2.718,3.427,2.798,3.534,4.456,5.465,5.894]

#计算sinx与cosx
s=[]
c=[]
for i in range(0,10):
	s.append(math.sin(x[i]))
	c.append(math.cos(x[i]))

#计算各种求和
s_sum=0
c_sum=0
sc_sum=0
ys_sum=0
yc_sum=0
for i in range(0,10):
	s_sum+=s[i]**2
	c_sum+=c[i]**2
	sc_sum+=s[i]*c[i]
	ys_sum+=y[i]*s[i]
	yc_sum+=y[i]*c[i]

#计算系数a,b
a=(ys_sum*c_sum-yc_sum*sc_sum)/(s_sum*c_sum-sc_sum*sc_sum)
b=(yc_sum*s_sum-ys_sum*sc_sum)/(s_sum*c_sum-sc_sum*sc_sum)

#计算均分误差
k=0
for i in range(0,10):
        k+=(a*s[i]+b*c[i]-y[i])**2
k/=10

#输出结果
print("a={:.15e},b={:.15e},均方误差={:.15e}".format(a,b,k))
