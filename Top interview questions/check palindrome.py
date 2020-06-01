def is_palindrome(str):
    
    original_str = str
    reverse_str = str[::-1]
    
    if original_str == reverse_str:
        return True
    
    return False

#alternative
def is_palindrome_python(str): 
    return str == ''.join(str[::-1])

if __name__ == "__main__":
    
    str = 'radar'
    print(is_palindrome_python(str))