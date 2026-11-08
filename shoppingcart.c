#include <stdio.h>
 #include <string.h> 

 int main(){

    char item[50] = "";
    float price = 0.0f;
    int quantity = 0;
    char currency ='$';
    float total = 0.0f ;

    printf("what item would you like to buy?: ");
    fgets(item, sizeof(item), stdin);
    
    printf("what is the price of each? ");
    scanf("%f", &price);

    printf("how many would you like to buy ?");
    scanf("%d", &quantity );

    total = price * quantity ;
    printf("\n you have bought %d %s",quantity ,item);
    printf("your total is %c%.2f", currency ,total);

  return 0;
 }