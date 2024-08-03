#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

vector<int> generate_palindromes(int max_n) {
    vector<int> palindromes;
    for (int num = 1; num <= max_n; ++num) {
        string s = to_string(num);
        string rev_s = string(s.rbegin(), s.rend());
        if (s == rev_s) {
            palindromes.push_back(num);
        }
    }
    return palindromes;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    vector<int> palindromes = generate_palindromes(40000);
    vector<int> dp(40001, 0);
    dp[0] = 1;  

    for (int p : palindromes) {
        for (int i = p; i <= 40000; ++i) {
            dp[i] = (dp[i] + dp[i - p]) % MOD;
        }
    }

    while (t--) {
        int n;
        cin >> n;
        cout << dp[n] << '\n';
    }

    return 0;
}
