def clean_text(text, punctuation, uninteresting_words):
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
    clean_text = ''
    
    for word in words:
        if word in uninteresting_words:
            words.remove(word)
    return words
        
def word_count(text):
    count = {}
    for word in text:
        if word not in count:
            count[word] = 0
        count[word] += 1
    return count

# def calculate_frequencies(file_contents):
#     # Here is a list of punctuations and uninteresting words you can use to process your text
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
#     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
#     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
#     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
#     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
#     # LEARNER CODE START HERE
#     # Function to clean the text 
#     def clean_text(text, punctuation, uninteresting_words):
#     no_punctuation = ''
#     # Delete all punctuation in the text as it is unnecesary
#     for letter in text:
#         if letter in punctuations:
#             no_punctuation += letter.replace(letter, '')
#         else:
#             no_punctuation += letter
#     # Delete all uninteresting words from text and return a clean text
#     words = no_punctuation.split()
#     clean_text = ''
#     for word in words:
#         if word in uninteresting_words:
#             words.remove(word)
#     return words

#     # Function to count words
#     def word_count
    
    
#     #wordcloud
#     # cloud = wordcloud.WordCloud()
#     # cloud.generate_from_frequencies()
#     # return cloud.to_array()

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

text = 'this is a test, including punctuation and uninteresting words, words, words, words, test, punctuation, Punctuation, PUNCTUATION'
clean_text = clean_text(text, punctuations, uninteresting_words)

print(clean_text)
word_count = word_count(clean_text)
print(word_count)
