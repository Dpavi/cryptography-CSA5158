#include<stdio.h>

int main()
{
    int p1=12,p2=4;
    int c1=(9*p1+4*p2)%26;
    int c2=(5*p1+7*p2)%26;

    printf("%c%c",c1+'A',c2+'A');
    return 0;
}
