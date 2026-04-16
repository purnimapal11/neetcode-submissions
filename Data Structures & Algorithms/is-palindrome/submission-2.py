import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_converted = s.lower()
        new_string = ""
        for char in s_converted:
            if char not in string.punctuation:
                new_string += char
        new_string = new_string.replace(" ", "")
        if new_string == new_string[::-1]:
            return True
        else:
            return False

        