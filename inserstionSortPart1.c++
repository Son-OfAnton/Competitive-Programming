// HackerRank
void insertionSort1(int n, vector<int> arr) 
{
    int temp = arr[n-1];
    for (int i = n - 2; i >= 0; i--)
    {
        if (arr[i] > temp)
        {
            arr[i + 1] = arr[i];
            for (int i : arr)
                cout << i << " ";
            cout << endl;
        }
        else
        {
            arr[i + 1] = temp;
            for (int i : arr)
                cout << i << " ";
            cout << endl;
            break;
        }
        if(i == 0 && arr[i] >= temp)
        {
            arr[0] = temp;
            for (int i : arr)
                cout << i << " ";
            cout << endl;
        }
    }
}
