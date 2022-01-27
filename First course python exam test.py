def text_cleanup(text, punctuation, uninteresting_words):
    lower_text = text.lower()
    no_punctuation = ''
    #Delete all punctuation in the text as it is unnecesary
    for letter in lower_text:
        if letter in punctuation:
            no_punctuation += letter.replace(letter, '')
        else:
            no_punctuation += letter

    #Delete all uninteresting words from text and return a clean text
    words = no_punctuation.split()
    clean_text = []
    
    for word in words:
        if word not in uninteresting_words:
            clean_text.append(word)
    return clean_text
        
def count_words(text):
    count = {}
    for word in text:
        if word not in count:
            count[word] = 0
        count[word] += 1
    return count

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
"there", "in"]

file_contents = "This is a text !!!! with Varios VARIOUS words teams bla bla the the the the the the the the"

clean_text = text_cleanup(file_contents, punctuations, uninteresting_words)
word_count = count_words(clean_text)

print(word_count)