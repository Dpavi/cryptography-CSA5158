#include<stdio.h>

int main()
{
    char p[]="SEND";
    int k[]={9,0,1,7};

    for(int i=0;i<4;i++)
        printf("%c",((p[i]-'A'+k[i])%26)+'A');

    return 0;
}
