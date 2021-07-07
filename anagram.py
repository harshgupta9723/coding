# check for anagram

class Solution:
    def isAnagram(self,a,b):
        if len(a) == len(b):
            test = list(a)
            for i in range(len(b)):
                try:    
                    test.remove(b[i])
                except:
                    pass
    
            if test == []:
                return "YES"

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
