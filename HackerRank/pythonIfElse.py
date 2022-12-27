# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    output = None
    if n % 2 == 1:
        output = "Weird"
    elif n % 2 == 0:
        if n >= 2 and n <= 5:
            output = "Not Weird"
        elif n >= 6 and n <= 20:
            output = "Weird"
        elif n > 20:
            output = "Not Weird"
            
    print(output)
            
  
