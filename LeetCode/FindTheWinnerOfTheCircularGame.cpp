// 1823. Find the Winner of the Circular Game

class Solution {
public:
    int findTheWinner(int n, int k) {
        if (n == 1)
            return 1;
        else
            return (findTheWinner(n - 1, k) + k - 1) % n + 1; 

    }
};

/*
* An iterative soluiton
*
* class Solution {
* public:
*   int findTheWinner(int n, int k) {
*       vector<int> arr;
*       int i = 1, current = 0, remove;
*       while(i <= n)
*       {
*           arr.push_back(i);
*           i++;
*       }
*       
*       while(arr.size() > 1)
*       {
*           remove = (current + k - 1) % arr.size();
*           arr.erase(arr.begin() + remove);
*           current = remove;
*        }
*        
*        return arr[0];
*
*    }
* };
*
*
*
*/

