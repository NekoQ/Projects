#include <stdio.h>

int board[11][11];
int qx[3] = {0, 1, -1};
int qy[3] = {1, 0, 0};

void print_board();
void solve(int x, int y);
int solved();
int check_square(int num, int x, int y);
int check_lines(int num, int x, int y);

int main()
{
    for (int i = 0; i < 11; i++)
    {
        for (int j = 0; j < 11; j++)
        {
            board[i][j] = -1;
        }
        
    }
    
    FILE *b = fopen("sudoku_board.txt", "r");
    for (int i = 1; i < 10; i++)
    {
        for (int j = 1; j < 10; j++)
        {
            fscanf(b, "%d", &board[i][j]);
        }
    }
    for (int i = 0; i < 11; i++)
    {
        for (int j = 0; j < 11; j++)
        {
            printf("%2d ", board[i][j]);
        }
        printf("\n");
        
    }
    solve(1,1);
    
}

void print_board()
{
    for (int i = 1; i < 10; i++)
    {
        for (int j = 1; j < 10; j++)
        {
            printf("%d ", board[i][j]);
            if(j % 3 == 0 && j != 9)
                printf(" ");
        }
        if(i % 3 == 0)
            printf("\n");
        printf("\n");
    }
}

int check_lines(int n, int x, int y)
{
    for (int i = 1; i < 10; i++)
        if (board[x][i] == n)
            return 0;

    for (int i = 1; i < 10; i++)
        if (board[i][y] == n)
            return 0;

    return 1;    
}

int check_square(int n, int x, int y)
{
    int xp = (int)((x-1) / 3) * 3 + 1;
    int yp = (int)((y-1) / 3) * 3 + 1;
    for (int i = xp; i < xp + 3; i++)
        for (int j = yp; j < yp + 3; j++)
            if (board[i][j] == n)
                return 0;

    return 1;
    
}

int solved()
{
    for (int i = 1; i < 10; i++)
        for (int j = 1; j < 10; j++)
            if(board[i][j] == 0)
                return 0;

    return 1;
}

void solve(int x, int y)
{
    if(board[x][y] != -1){
        if(board[x][y] == 0){
            for (int num = 1; num < 10; num++)
            {
                if(check_lines(num, x, y) && check_square(num, x, y))
                {
                    board[x][y] = num;
                    print_board();
                    for (int i = 0; i < 3; i++)
                    {
                        solve(x + qx[i], y + qy[i]);
                    }
                    board[x][y] == 0;
                    if(solved())
                    {
                        print_board();
                        exit(1);
                    }
                }
            }
        }
        else
        {
            for (int i = 0; i < 2; i++)
            {
                solve(x + qx[i], y + qy[i]);
            }
        }
        
    }
}