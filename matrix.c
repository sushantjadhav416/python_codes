#include<stdio.h>
int main(){
   
   /*Counter variables for the loop*/
   int i, j,a,a;
   /* 2D array declaration*/
   int dispa[a][a];
   printf("Enter the row and column:");
   scanf("%d",&a);
   for(i=0; i<=a; i++) {
      for(j=0;j<=a;j++) {
         printf("Enter value for disp[%d][%d]:", i, j);
         scanf("%d", &dispa[i][j]);
      }
   }
   


   //Displaying array elements
   printf("Two Dimensional array elements:\n");
   for(i=0; i<=a; i++) {
      for(j=0;j<=a;j++) {
         printf("%d ", dispa[i][j]);
         if(j==2){
            printf("\n");
         }
      }
   }
   return 0;
}