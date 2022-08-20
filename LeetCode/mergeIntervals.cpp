class Solution
{
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals)
    {
        if (intervals.size() <= 1)
            return intervals;

        sort(intervals.begin(), intervals.end());
        vector<vector<int>> merged;

        for (int i = 0; i < intervals.size(); i++)
        {
            int firstNum= intervals[i][0];
            int secondNum = intervals[i][1];
            for (int j = i + 1; j < intervals.size(); j++)
            {
                int NextFirstNum = intervals[j][0];
                int NextSecondNum = intervals[j][1];
                if (secondNum >= NextFirstNum)
                {
                    secondNum = max(secondNum, NextSecondNum);
                    i = j;
                }
            }
            merged.push_back({firstNum, secondNum});
        }
        return merged;
    }
};
