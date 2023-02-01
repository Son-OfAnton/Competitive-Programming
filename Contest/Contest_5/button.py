# https://codeforces.com/gym/424075/problem/B

number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    text = input()
    length = len(text)
    left = 0
    faulty_keys = set()
    
    while left < length:
        right = left + 1
        same_letter_count = 0
        
        while right < length and text[right] == text[right - 1]:
            same_letter_count += 1
            right += 1
            left += 1
            
        if same_letter_count % 2 == 0:
            faulty_keys.add(text[left])
        
        left += 1
        
    faulty_keys = sorted(list(faulty_keys))
    print("".join(faulty_keys))

    
