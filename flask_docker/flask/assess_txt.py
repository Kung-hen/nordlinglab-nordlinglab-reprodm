import pprint
from gensim import corpora
from gensim.utils import simple_preprocess
import os

def txt_BoW(txt):
    doc = simple_preprocess(txt, deacc=True)
    dictionary = corpora.Dictionary()
    BoW_corpus = dictionary.doc2bow(doc, allow_update=True)
    # id_words = [[(dictionary[id], count) for id, count in line] for line in BoW_corpus]
    # print(id_words)
    return (dictionary, BoW_corpus)
def assess_reprod(dictionary, query, criterion):
    assess_yes = 'Your ' + criterion + ' is available'
    assess_no = 'Your ' + criterion + ' is not available'
    query_result = True
    for block in query:
        block_result = False
        for word in block:
            if word in dictionary:
                block_result = True
        if block_result == False:
            query_result = False
    if query_result == True:
        assess_result = assess_yes
    else:
        assess_result = assess_no
    return assess_result

def txt_reprod(txt, query, criterion):
    (mydict, corpus) = txt_BoW(txt)
    assess_result = assess_reprod(mydict.token2id, query, criterion)
    return assess_result

