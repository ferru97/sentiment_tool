#https://lda.readthedocs.io/en/latest/autoapi/lda/index.html
import numpy as np
import pandas as pd
import lda
import re
import os

import gensim
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import gensim.corpora as corpora
from pprint import pprint

import pyLDAvis.gensim
import pickle 
import pyLDAvis

alpha = 0
beta = 0

def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))

def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]


df = pd.read_csv("dataset.csv", dtype=object)
for index, row in df.iterrows():
    print("- Record {}/{}".format(str(index+1), str(len(df.index))))

    # Remove punctuation
    # Convert the titles to lowercase
    row['article_processed'] = str(row['article']).lower()
    row['article_processed'] = re.sub('[,!?]', '', row['article_processed'])


    #to list of sentences
    text = row['article_processed']
    new_data = pd.DataFrame()
    for index, t in enumerate(text.split('.')):
        new_data.loc[index,"article_processed"] = t.replace(".",'')

    #Prepare text for LDA analysis 
    stop_words = stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

    data_ready = new_data.article_processed.values.tolist()
    #data_ready = data.title_processed.values.tolist() + data_ready
    data_words = list(sent_to_words(data_ready))
    # remove stop words
    data_words = remove_stopwords(data_words)



    #Create dictionary and terms frequencies
    id2word = corpora.Dictionary(data_words)
    # Create Corpus
    texts = data_words
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]
    if corpus == [[]]:
        continue

    #LDA modeling
    # number of topics
    num_topics = 3
    # Build LDA model
    lda_model = gensim.models.LdaModel(corpus=corpus,id2word=id2word,num_topics=num_topics, eta="auto", alpha="auto" )
    # Print the Keyword in the 3 topics
    for i in range(0,num_topics):
        df.loc[index,"topic "+str(i+1)] = str((lda_model.print_topics())[1])
    


df.to_csv("results/res.csv")