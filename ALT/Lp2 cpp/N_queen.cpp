#include<iostream>
#include<bits/stdc++.h>
#include<vector>
using namespace std;
class Solution {
public:
    void prepare_ans(vector<vector<char>> &arr,int col,int n)
    {
        for(auto i: arr)
        {
            for(auto j:i)
            {
                cout<<j<<" ";
            }
            cout<<endl;
        }
        cout<<endl;
    }
    bool isSafe(vector<vector<char>> &arr,int row,int col,int n)
    {
        // Upper left diagonal
        int i=row;
        int j=col;
        while(i >= 0 && j >= 0)
        {
            if(arr[i][j] == 'Q')
            {
                return false;
            }
            i--;
            j--;
        }

        // Left row check
        j=col;
        while(j >= 0)
        {
            if(arr[row][j] == 'Q')
            {
                return false;
            }
            j--;
        }

        // Bottom diagonal check
        i=row;
        j=col;
        while(i < n && j >= 0)
        {
            if(arr[i][j] == 'Q')
            {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    void N_queen(vector<vector<char>> &arr,int col,int n,int &i)
    {
        if(col >= n)
        {
            i++;
            prepare_ans(arr,col,n);
            return;
        }

        for(int row=0;row<n;row++)
        {
            if(isSafe(arr,row,col,n))
            {
                arr[row][col]='Q';
                N_queen(arr,col+1,n,i);
                arr[row][col]='.';
            }
        }
    }
    void solveNQueens(int n) {
        vector<vector<char>> arr(n,vector<char>(n,'.'));
        int i=0;
        N_queen(arr,0,n,i);
        cout<<"Total solutions are: "<<i;
    }
};
int main()
{
    Solution obj;
    obj.solveNQueens(8);
}