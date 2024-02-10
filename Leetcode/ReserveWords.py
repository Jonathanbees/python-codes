class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
# Test cases
print(Solution().reverseWords("the    sky    is    blue"))  # blue is sky the