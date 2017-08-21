import nltk
import gensim
import pandas as pd
import numbers
from nltk import tokenize
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import TweetTokenizer
from nltk.util import ngrams
from collections import Counter
tknzr = TweetTokenizer()


import sys

post = str(sys.argv)
postid = #id
title =  #title
isself =  #is_self
numcomments = #num_comments




def get_features(post):

    num_features = 15
    Feature_vector = np.zeros(num_features)

    words = tknzr.tokenize(post)


    # content w/ punctuations -- unigram, trigram, bigram -- tfidf
    Feature_vector[0] = #unigram, trigram, bigram
    unigram = ngrams(words,1)
    bigrams = ngrams(token,2)
    trigrams = ngrams(token,3)


    # num sent, num word, num char for post
    sents = nltk.sent_tokenize(str(post))

    Feature_vector[1] = len(sents) #num sentence
    Feature_vector[2] = len(words) #num words
    Feature_vector[3] = len(post) #num char


    # num sent, num word, num char for title
    sents_t = nltk.sent_tokenize(str(title))
    words_t = tknzr.tokenize(title)
    Feature_vector[4] = len(sents_t) #num sentence
    Feature_vector[5] = len(words_t) #num words
    Feature_vector[6] = len(title) #num char


    # more -- selfpost or linkpost, num comment, num branche
    Feature_vector[7] = selfpost
    Feature_vector[8] = numcomments


    # punctuation, 1st person pronouns
    #Feature_vector[] = # num punctuation
    #Feature_vector[] = # num 1st person pronouns


    return feature_vector



# put feature vectors into rows of pandas dataframe.
