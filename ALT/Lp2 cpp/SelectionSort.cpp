#include <bits/stdc++.h>
using namespace std;
void printArray(vector<int>&arr, int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout<<endl;
}
// Function for Selection sort
void selectionSort(vector<int>&arr, int n)
{
    int i, j, min_idx;
    for (i = 0; i < n - 1; i++)
    {
        min_idx = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        if (min_idx != i)
            swap(arr[min_idx], arr[i]);
        cout<<"After iteration"<<i+1<<": ";
        printArray(arr,n);
    }
}

int main()
{
    int n;

    cout<<"enter size of array: ";
    cin>>n;
    vector<int> arr(n);
    // Function Call
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    selectionSort(arr, n);
    cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}

// This is code is contributed by rathbhupendra
