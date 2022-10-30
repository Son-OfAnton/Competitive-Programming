# 2086. Minimum Number of Buckets Required to Collect Rainwater from Houses

class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = list(street)

        for i, char in enumerate(street):
            if char == 'H':
                if i > 0 and street[i - 1] == 'B':
                    continue
                if i + 1 < len(street) and street[i + 1] == '.':
                    street[i + 1] = 'B'
                elif i > 0 and street[i - 1] == '.':
                    street[i - 1] = 'B'
                else:
                    return -1

        return street.count('B')
