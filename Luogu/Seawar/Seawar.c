#include <stdio.h>
char map[1001][1001];
int fx[] = {0, 1, 0, -1};
int fy[] = {1, 0, -1, 0};
int isValid(int x, int y, char a[][1001])
{
    int count = 0;
    if (a[x][y] == '#')
    {
        count++;
    }
    if (a[x + 1][y] == '#')
    {
        count++;
    }
    if (a[x][y + 1] == '#')
    {
        count++;
    }
    if (a[x + 1][y + 1] == '#')
    {
        count++;
    }
    if (count == 3)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
void tianchong(int x, int y, char a[][1001], int row, int col)
{
    for (int i = 0; i < 4; i++)
    {
        if (x + fx[i] < 0 || x + fx[i] >= row || y + fy[i] < 0 || y + fy[i] > col)
        {
            break;
        }
        else
        {
            if (a[x + fx[i]][y + fy[i]] == '#')
            {
                a[x + fx[i]][y + fy[i]] = '*';
                tianchong(x + fx[i], y + fy[i], a, row, col);
            }
        }
    }
}
int main(void)
{
    int row, col;
    scanf("%d %d", &row, &col);

    for (int i = 0; i < row; i++)
    {
        scanf("%s", map[i]);
    }

    int flag = 1;
    for (int i = 0; i < row - 1; i++)
    {
        for (int j = 0; j < col - 1; j++)
        {
            if (!isValid(i, j, map))
            {
                printf("Bad placement.\n");
                flag = 0;
                break;
            }
        }
        if (!flag)
        {
            break;
        }
    }

    // 撞船的话不用数条数了
    int count = 0;
    if (flag)
    {
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                if (map[i][j] == '#')
                {
                    tianchong(i, j, map, row, col);
                    count++;
                }
            }
        }
        printf("There are %d ships.\n", count);
    }

    return 0;
}