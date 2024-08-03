def get_LPS(s):
    '''
        Args:
            s: string
        Returns:
            LPS: longest proper prefix which is also suffix
    '''
    
    LPS = [0]*len(s)
    i, j = 1, 0

    while i < len(s):
        if s[i] == s[j]:
            j += 1
            LPS[i] = j
            i += 1
        elif j > 0:
            j = LPS[j-1]
        else:               # case where j == 0
            LPS[i] = 0
            i += 1

    return LPS


def KMP(haystack, needle):
    '''
        Args:
            haystack: string
            needle: string  
        Returns:
            index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    '''    


    haystack_len, needle_len = len(haystack), len(needle)
    LPS = get_LPS(needle)
    i, j = 0, 0

    while i < haystack_len and j < needle_len:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        elif j > 0:
            j = LPS[j-1]
        else:
            i += 1
        
    return -1 if j < needle_len else i - needle_len

