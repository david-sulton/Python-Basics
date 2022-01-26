def initials(phrase):
    #join - it will concatenate string
    #split - it will separate words in a string
    #upper
    #lower
    #strip - gets rid of surrounding spaces
        #rstrip or lstrip will get rid of right or left characters
    #count - hoy many times a susbtring appears within a string
    #endswith - wether a string ends with a specific substring
    #isnumeric  - wether the string is made of just number2*


    words = phrase.split()
    result = ""
    for word in words:
        result += word.index[0]
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
