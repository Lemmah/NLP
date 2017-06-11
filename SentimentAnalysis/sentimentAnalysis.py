"""
Identify and extract sentiment in given string. Sentiment analysis (also known as opinion mining) refers to the use of natural language processing, text analysis and computational linguistics to identify and extract subjective information in source materials. This algorithm takes an input string and assigns a sentiment rating in the range [-1 t0 1] (very negative to very positive).
"""
# Further reading: https://algorithmia.com/algorithms/nlp/SentimentAnalysis?utm_source=blog&utm_medium=post&utm_campaign=nlp

import pprint

import Algorithmia

sentence = input("Input sentence: ")
sentiment = {
    "document": sentence
}

client = Algorithmia.client('simNjBefAAP0jc1S8UIniEnh7381')
algo = client.algo('nlp/SentimentAnalysis/1.0.3')
print(pprint.pformat(algo.pipe(sentiment)))
