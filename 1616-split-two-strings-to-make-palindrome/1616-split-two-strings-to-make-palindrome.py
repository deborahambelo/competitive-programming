class Solution(object):
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def checkPalindromeFormation(self, a, b):
        def can_form_palindrome(s1, s2):
            n = len(s1)
            left, right = 0, n - 1
            while left < right and s1[left] == s2[right]:
                left += 1
                right -= 1
            return self.is_palindrome(s1, left, right) or self.is_palindrome(s2, left, right)

        return can_form_palindrome(a, b) or can_form_palindrome(b, a)
