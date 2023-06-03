#include <iostream>

using namespace std;

const int S = 8;


void change_p(string &p)
{
    p[0] = p[0] - 'a';
    p[1] = p[1] - '1';
}

int integer(char latteral)
{
    return (int)(latteral);
}

bool in_boundaries(int i, int j)
{
    return (i >= 0) && (j >= 0) && (i < S) && (j < S);
}

bool is_way(int map[][S], int pos_x, int pos_y)
{
    int ki_di_x[] = {-1, 0, 1};
    int ki_di_y[] = {-1, 0, 1};

    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            if (i == 1 && j == 1) continue;
            
            if (in_boundaries(pos_x + ki_di_x[i], pos_y + ki_di_y[j]))
            {
                if (map[pos_x + ki_di_x[i]][pos_y + ki_di_y[j]] != 2)
                    return true;
            }
        } 
    }

    return false;
}

int main()
{
    string bknight_p, bking_p, bbishop_p;
    string wking_p;
    
    cin >> wking_p;
    cin >> bking_p >> bknight_p >> bbishop_p;

    change_p(wking_p);
    change_p(bking_p);
    change_p(bknight_p);
    change_p(bbishop_p);

    
    int map[S][S];
    
    for (int i = 0; i < S; i++)
    {
        for (int j = 0; j < S; j++)
        {
            map[i][j] = 0;
        }
    }

    map[integer(wking_p[0])][integer(wking_p[1])] = 1;

    int kn_ms_x[] = {-2, -1, 1, 2, -2, -1, 1, 2};
    int kn_ms_y[] = {1, 2, 2, 1, -1, -2, -2, -1};

    int bi_di_x[] = {-1, 1, -1, 1};
    int bi_di_y[] = {1, -1, -1, 1};

    int ki_di_x[] = {-1, 0, 1};
    int ki_di_y[] = {-1, 0, 1};

    // knight
    int bknight_pos[2] = {integer(bknight_p[0]), integer(bknight_p[1])};


    for(int i = 0; i < 8; i++)
    {
        if (!in_boundaries(bknight_pos[0] + kn_ms_x[i], bknight_pos[1] + kn_ms_y[i])) continue;
        map[bknight_pos[0] + kn_ms_x[i]][bknight_pos[1] + kn_ms_y[i]] = 2;
        
    }

    // bishop

    //map[integer(bbishop_p[0])][integer(bbishop_p[1])] = 1;

    for (int i = 0; i < 4; i++)
    {
        int bbishop_pos[2] = {integer(bbishop_p[0]), integer(bbishop_p[1])};
        while(in_boundaries(bbishop_pos[0] + bi_di_x[i], bbishop_pos[1] + bi_di_y[i]))
        {
            if (map[bbishop_pos[0] + bi_di_x[i]][bbishop_pos[1] + bi_di_y[i]] == 2) break;

            map[bbishop_pos[0] + bi_di_x[i]][bbishop_pos[1] + bi_di_y[i]] = 2;
            bbishop_pos[0] += bi_di_x[i];
            bbishop_pos[1] += bi_di_y[i];
        }
    }


    // king
    int bking_pos[2] = {integer(bking_p[0]), integer(bking_p[1])};

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (in_boundaries(bking_pos[0] + ki_di_x[i], bking_pos[1] + ki_di_y[j]))
            {
                map[bking_pos[0] + ki_di_x[i]][bking_pos[1] + ki_di_y[j]] = 2;
            }
        }
    }

    int wking_pos[2] = {integer(wking_p[0]), integer(wking_p[1])};

    if (map[wking_pos[0]][wking_pos[1]] == 2)
    {
        if (is_way(map, wking_pos[0], wking_pos[1]))
        {
            cout << "check";
        }
        else 
        {
            cout << "mate";
        }
    }
    else
    {
        if (is_way(map, wking_pos[0], wking_pos[1]))
        {
            cout << "nothing";
        }
        else 
        {
            cout << "stalemate";
        }
    }
    cout << endl;
}