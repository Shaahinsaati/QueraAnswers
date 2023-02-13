def isPalindrome(s):
	return s == s[::-1]
s =input().lower()
ans = isPalindrome(s)
print("YES") if ans else print("NO")