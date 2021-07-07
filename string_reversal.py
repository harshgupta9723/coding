# check palindrom

class Solution:
    #method 1
	def isPlaindrome(self, S):
		# code here
        if S[::-1] == S:
            return 1
        else:
            return 0
    
    #method 2
    def isPlaindrome(self, S):
        last = len(S) - 1
        test_string = list(S)
    
        for i in range(int(len(test_string)/2)):
            temp = test_string[i]
            test_string[i] = test_string[last]
            test_string[last] = temp
            last -= 1
    
        if "".join(test_string) == S:
            return 1
        else:
            return 0

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPlaindrome(S)
		print(answer)