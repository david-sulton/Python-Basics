def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    
    for i in input_string:
        
        if i != " ":
            new_string += i
            reverse_string = i + reverse_string
            
    if new_string.lower() == reverse_string.lower():
        return True
    else:
        return False



print(is_palindrome("Never Odd or Even"))


