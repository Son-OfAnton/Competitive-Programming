#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

int main() {
    int n, q;
    std::cin >> n >> q;

    std::vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        std::cin >> nums[i];
    }

    std::map<int, std::vector<int>> queries;

    int maxx = 0;
    for (int i = 0; i < q; i++) {
        int query;
        std::cin >> query;
        queries[query] = std::vector<int>();
        maxx = std::max(maxx, query);
    }

    for (int i = 0; i < maxx; i++) {
        if (queries.find(i + 1) != queries.end()) {
            queries[i + 1] = {nums[0], nums[1]};
        }
        int A = nums[0];
        int B = nums[1];

        nums.erase(nums.begin(), nums.begin() + 2);

        if (A > B) {
            nums.push_back(B);
            nums.insert(nums.begin(), A);
        } else {
            nums.push_back(A);
            nums.insert(nums.begin(), B);
        }
    }

    for (const auto& pair : queries) {
        for (int num : pair.second) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}