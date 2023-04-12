#include<iostream>
using namespace std;
void smallest_int(int a);
int main()
{
    int a;
    cin>>a;
    smallest_int(a);
 return 0;
}

void smallest_int(int a)
{
    int i,j=0;
    int small[10000];
    if(a<10)
    {
        a=a+10;
    }
    for(i=9;i>1;--i)
    {
        while(a%i==0)
        {
          a=a/i;
          small[j]=i;
          j++;
        }
    }
    if(a>10)
    {
        cout<<"Not Possible!!";
        return; 
    }
    for(i=j-1;i>=0;i--)
    {
        cout<<small[i];
    }

}