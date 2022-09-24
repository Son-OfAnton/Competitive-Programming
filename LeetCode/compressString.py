class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """ 
        ptr1, ptr2 = 0, 0
        size = len(chars)
        while ptr1 < size:
            k = ptr1
            while ptr1 < size and chars[ptr1] == chars[k]:
                ptr1 += 1
            chars[ptr2] = chars[k]
            ptr2 += 1
            if ptr1 - k != 1:
                for s in str(ptr1-k):
                    chars[ptr2] = s
                    ptr2 += 1
        return ptr2     
