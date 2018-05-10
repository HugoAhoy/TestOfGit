#include<iostream>
using namespace std;

struct Pair
{
    int length;
    int difficulty;
} typedef P;

int main()
{
    P Parr[25];
    int lenMax, n, result = 0;
    cin >> lenMax >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> Parr[i].length >> Parr[i].difficulty;
    }
    for (int i = 0; i < n - 1; i++)
    {
        int maxIndex = n - 1;
        int j;
        for (j = n - 2; j >= i; j--)
        {
            if(Parr[maxIndex].difficulty < Parr[j].difficulty)
            {
                maxIndex = j;
            }
            else if(Parr[maxIndex].difficulty == Parr[j].difficulty)
            {
                if(Parr[maxIndex].length < Parr[j].length)
                {
                    maxIndex = j;
                }
            }
        }
        P temp;
        temp.difficulty = Parr[i].difficulty;
        temp.length = Parr[i].length;
        Parr[i].difficulty = Parr[maxIndex].difficulty;
        Parr[i].length = Parr[maxIndex].length;
        Parr[maxIndex].difficulty = temp.difficulty;
        Parr[maxIndex].length = temp.length;
    }
/*    for (int i = 0; i < n; i++)
    {
        cout << Parr[i].length << ' ' << Parr[i].difficulty << endl;
    }*/
    for (int i = 0; i < n; i++)
    {
        if (Parr[i].length < lenMax)
        {
            lenMax = lenMax - Parr[i].length;
            result = result + Parr[i].length * Parr[i].difficulty;
        }
    }
    cout << result << endl;
    system("pause");
    return 0;
}
