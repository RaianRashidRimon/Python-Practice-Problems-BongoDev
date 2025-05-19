def checkpalindrome(word):
    normalized = ''.join(char.lower() for char in word if char.isalnum())
    return normalized == normalized[::-1]
inputt = "Madam"


check = checkpalindrome(inputt)
print(check)