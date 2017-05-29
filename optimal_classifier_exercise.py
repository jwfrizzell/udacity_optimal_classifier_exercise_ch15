import re
#------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We 
have some new people coming in, and we need all the space we can get. So if you 
could just go ahead and pack up your stuff and move it down there, that would be 
terrific, OK? Oh, and remember: next Friday... is Hawaiian shirt day. So, you 
know, if you want to, go ahead and wear a Hawaiian shirt and jeans. Oh, oh, and 
I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, 
too... Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and 
come in tomorrow. So if you could be here around 9 that would be great, mmmk... 
oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in 
on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to 
play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''
words_to_guess = ["ahead", "could"]

def LaterWords(sample, word, distance):
    '''
    @param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which has the most likely possibility
    '''
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.

    word = re.sub('[^a-zA-Z0-9- ]', '', word)
    following_words = NextWordProbability(sample, word)
    len_words = float(len(following_words))
    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.
    next_word = {}
    nested_predictions = {}
    for i in range(2, distance + 1):
        for k, v in following_words.items():
            probability = v / len_words
            next_word[k] = NextWordProbability(sample, k)
            for key, value in next_word[k].items():
                next_word[k][key] = value * probability
                nested_predictions.update({key: next_word[k][key]})

    if(distance > 1):
        following_words = nested_predictions
            
    return max(following_words, key=following_words.get)

def NextWordProbability(sample_text, word):
    '''
        @sample_text: a sample of text to draw from
        @word: word being search on to find the preceeding word. 
        @returns: dictionary list.
    '''
    text = re.sub('[^a-zA-Z0-9- ]', '', sample_text)
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

print(LaterWords(sample_memo, "we", 2))
