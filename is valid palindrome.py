def is_palindrome(s: str) -> bool:
    
    str1 = ''.join(char.lower() for char in s if char.isalnum())
    return str1 == str1[::-1]
print(is_palindrome("A man, a plan, a canal: Panama")) 
print(is_palindrome("race a car"))
print(is_palindrome(" right to now"))                              
