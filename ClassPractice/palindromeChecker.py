

def isPalindrome(word):
    word = word.lower()
    if len(word) <= 1:
        return True
    if word[0] == " ":
        word = word[1:]
    if word[-1] == " ":
        word = word[:-1]
    if word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    else:
        return False

print isPalindrome("hannah")
print isPalindrome("hello")
print isPalindrome("a man a plan a canal panama")

