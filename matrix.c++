#include<iostream>
using namespace std;

int main()
{
    int i,j;
    int a[3][3];
    for(i=0;i<=2;i++)
    {
        for(j=0;j<=2;j++)
        {
          cin>>a[i][j];

        }
    }
         
    a[0][0]= a[0][1] + a[1][0] + a[1][1];
    a[1][1]= a[0][0] + a[0][1] + a[0][2]+ a[1][0] + a[1][2] + a[2][0] + a[2][1] + a[2][2];
    a[2][2]= a[2][1] + a[1][1] + a[1][2];

    for(i=0;i<=2;i++)
    {
        for(j=0;j<=2;j++)
        {
          cout<<a[i][j]<<"\t";
          if(j==2){
            cout<<"\n";
         }

        }
    } 
 return 0;
}
