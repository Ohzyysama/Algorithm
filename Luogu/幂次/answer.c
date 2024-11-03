#include <stdio.h>
#include <math.h>
#include <stdbool.h>
// 可以看作一个十进制转二进制的题目
void divide(int n);
int main(void)
{
    int n = 0;
    scanf("%d", &n);
    divide(n);
    return 0;
}
void divide(int n)
{

    bool flag = false;
    while (n != 0)
    {
        int num = (int)(log2(n));
        if (flag)
            printf("+");
        if (num == 1)
        {
            printf("2");
        }
        else if (num == 0)
        {
            printf("2(0)");
        }
        else
        {
            printf("2(");
            divide(num);
            printf(")");
        }
        n = n - pow(2, (double)num);
        flag = true;
    }
}