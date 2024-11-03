#include <stdio.h>
#include <stdbool.h>
int count = 0;
bool isPrime(int n)
{
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}
void sumIsPrime(int *a, int n, int k, int start, int sum)
{
    if (k == 0)
    {
        if (isPrime(sum))
        {
            count++;
        }
        return;
    }
    for (int i = start; i < n; i++)
    {
        sumIsPrime(a, n, k - 1, i + 1, sum + a[i]);
    }
}
int main(void)
{
    int n, k;
    scanf("%d %d", &n, &k);
    int nums[25] = {0};
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &nums[i]);
    }
    sumIsPrime(nums, n, k, 0, 0);
    printf("%d\n", count);

    return 0;
}