#include <stdio.h>
#include <math.h>

int main() {
    double sum;
    long int k;
    int i;
    double x[]={0.0,0.5,1.0,sqrt(2),10.0,100.0,300.0};

    for(i=0;i<7;i++){
        sum=0;
        for(k=1;k<10000000;k++){
            sum+=1/((k+x[i])*(k));
        }
        printf("x=%.2lf,y=%.15e\n",x[i],sum);
    }
    return 0;
}