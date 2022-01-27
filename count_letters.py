def count_letters(text):
    result = {}
    for letter in text:
        if letter.isalpha() and letter not in result:
            result[letter] = 0
        if letter.isalpha():
            result[letter] +=1
    return print(result)

count_letters('me gusta el coffee and code')