#include <stdio.h>
int main(void)
{
    long long int x = 1, y = 1;
    long long int N;
    scanf("%lld", &N);
    int vx = -1, vy = 1;
    for (int i = 1; i < N; i++)
    {
        if (y == 1 && (x % 2 == 0))
        {
            x += 1;
            vx = -1 * vx;
            vy = -1 * vy;
        }
        else if (x == 1 && !(y % 2 == 0))
        {
            y += 1;
            vx = -1 * vx;
            vy = -1 * vy;
        }
        else
        {
            x = x + vx;
            y = y + vy;
        }
    }
    printf("%lld/%lld", x, y);
    return 0;
}