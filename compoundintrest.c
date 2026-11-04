#include <stdio.h>
#include <math.h> 
#include <string.h>

 int main(){ 

  double principal =  0.0 ;
  double rate  = 0.0 ; 
  int years = 0 ;
  int timescompounded = 0;
  double total = 0.0 ;

  printf("commpound intrest calculator :");

  printf(" \nenter the principal : ");
  scanf("%lf ",&principal);

  printf("\nenter the interest rate  :");
  rate = rate/100;
  scanf("%lf",&rate );
 

  printf("\n enter the number of years:  ");
  scanf("%d" , &years );

  printf("\nenter no. of times compounded:  ");
  scanf("%d", &timescompounded );

  total = principal * pow(1 + rate / timescompounded , timescompounded * years );

  printf("after %d years , the total bill will be : %lf" , years , total);


  return 0 ;
 }