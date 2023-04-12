#include<stdio.h>

int main(){
    int i=1;
    while (1)
    {  
       i++;
       printf("%d",i);
       if(i==100-1)
       {
           break;
       }
    }
    

return 0;
}