class Solution {
public:
    int minSetSize(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        vector<int> frequency;
        int mid = arr.size() / 2;
        int counter = 1, begin = 0, result = 0;

        for (int i = 1; i < arr.size(); i++)
            {
                if (arr[begin] == arr[i])
                {
                    counter++;
                }
                else
                {
                    frequency.push_back(counter);
                    counter = 1;
                    begin = i;
                }
            }
        frequency.push_back(counter);
        sort(frequency.begin(), frequency.end());

        for(int i = frequency.size() - 1; i >= 0 && mid > 0; i--)
        {
            result++;
            mid -= frequency[i];
        }
        
        return result;
        
    }
};
