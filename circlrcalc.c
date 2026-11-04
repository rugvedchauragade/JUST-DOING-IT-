#include <stdio.h>
#include <math.h> 

 int main(){
    double radius = 0.0 ; 
    double area = 0.0 ;
    double surfacearea = 0.0 ;
    double volume = 0.0;
    const double pi = 3.14159 ;

    printf ("enter the radius :");
    scanf ("%lf", &radius ) ; 

    area = pi * pow(radius , 2 );
    surfacearea = 4 * pi * pow(radius , 2 );
    volume = (4.0/3.0) * pi * pow(radius ,3);

    printf ("area : %lf\n",area );
    printf ("surface area :%lf\n" ,surfacearea);
    printf ( "volume : %lf " , volume );


    return 0 ;
 }