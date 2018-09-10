#import nltk
#from nltk.corpus import brown
#cfd = nltk.ConditionalFreqDist(
#    (genre, word)
#    for genre in brown.categories()
#    for word in brown.words(categories=genre)
#)
#genre_word = [(genre, word)
        #for genre in ['news', 'romance']
        #for word in brown.words(categories=genre)]
#print(len(genre_word))
#print(genre_word[:4])
#cfd = nltk.ConditionalFreqDist(genre_word)
#print(cfd)
#print(cfd.conditions())

#print(cfd['news'])
#print(cfd['romance'])

#days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#print(cfd.plot(samples=days))


#def lexical_diversity(my_text_data):
#    word_count = len(my_text_data)
#    vocab_size = len(set(my_text_data))
#    diversity_score = vocab_size / word_count
#    return diversity_score
#from nltk.corpus import genesis
#kjv = genesis.words('english-kjv.txt')
#print(lexical_diversity(kjv))


#def plural(word):
#    if word.endswith('y'):
#        return word[:-1] + 'ies'
#    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
#        return word + 'es'
#    elif word.endswith('an'):
#        return word[:-2] + 'en'
#    else:
#        return word + 's'
#print(plural('can'))

#Exercises
#1
'''phrase = ["one", "though", "to", "when", "however"]
print(phrase.index('though'))
phrase.pop(0)
phrase.sort()
print(phrase)'''
#2
''' from nltk.corpus import gutenberg
#print(gutenberg.fileids())
austen = gutenberg.words('austen-persuasion.txt')
for n in austen:
    num_chars = len(gutenberg.raw(n))
    num_words = len(gutenberg.words(n))
    num_sents = len(gutenberg.sents(n))
    num_vocab = len(set(w.lower() for w in austen(n)))
    print(num_chars, num_sents, num_vocab, num_words) '''

#24
import nltk

def generate_model(cfdist, word, num=15):
        for i in range(num):
            print(word, end = " ")
            word = cfdist[word].max()
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.corpus.Con
cfd['living']