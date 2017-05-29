import re

sample_memo = '''
---Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

#
#   Maximum Likelihood Hypothesis
#
#
#   In this quiz we will find the maximum likelihood word based on the preceding word
#
#   Fill in the NextWordProbability procedure so that it takes in sample text and a word,
#   and returns a dictionary with keys the set of words that come after, whose values are
#   the number of times the key comes after that word.
#   
#   Just use .split() to split the sample_memo text into words separated by spaces.

def NextWordProbability(sampletext,word):
    
    text = re.sub('[^a-zA-Z0-9-]', ' ', sampletext)
    array_of_words = filter(None,text.split(' '))
    following_words = {}
    for i in range(len(array_of_words)):
        if(array_of_words[i] == word and (i + 1) != len(array_of_words)):
            next_word = array_of_words[i + 1]
            if(following_words.has_key(next_word)):
                following_words[next_word] += 1
            else:
             following_words[next_word] = 1
    return following_words


print(NextWordProbability(sample_memo, "gonna"))