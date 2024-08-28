from functools import *
from collections import *
from typing import *
from math import *
import re 
def load_testcase(filename): 
    with open(filename, "r", encoding='utf-8') as f:
        data = f.readlines() 
    n = len(data)
    pattern = r'\b[a-zA-Z_]+\w*\b'
    testcase = {}
    for i in range(0, n, 2): 
        matched = re.findall(pattern, data[i])
        testcase[matched[0]] = eval(data[i+1].strip('\n'))
    return testcase

#-----------------------------------------------------------------------------------------------
# Paste the code to be debugged following. 
#-----------------------------------------------------------------------------------------------
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s) 
        f = [0] + [inf] * n 
        for i in range(n): 
            cnt = defaultdict(int) 
            max_cnt = 0 
            for j in range(i, -1, -1): 
                cnt[s[j]] += 1
                max_cnt = max(max_cnt, cnt[s[j]]) 
                if i - j + 1 == len(cnt) * max_cnt: 
                    f[i + 1] = min(f[i+1], f[j] + 1) 
        return f[n]

#-----------------------------------------------------------------------------------------------
# Replace the above code with the code to be debugged. 
#-----------------------------------------------------------------------------------------------
def main(): 
    test = Solution() 
    function_names = [name for name in dir(test) if callable(getattr(test, name)) and not name.startswith("__")]
    test_function = eval("test."+function_names[0])
    testcase = load_testcase('testcase.txt')
    print(test_function(**testcase))

if __name__ == '__main__': 
    main()
    