"""
This algorithm retrives recognized entities from a body of text using the stanfordNlp library.Currently it identifies named noun type entities such as PERSON, LOCATION, ORGANIZATION, MISC and numerical MONEY, NUMBER, DATA, TIME, DURATION, SET types.
"""
# Further reading: https://algorithmia.com/algorithms/StanfordNLP/NamedEntityRecognition?utm_source=blog&utm_medium=post&utm_campaign=nlp

import Algorithmia

input = {"document": "Jim went to Stanford University, Tom went to the University of Washington. They both work for Microsoft."}
client = Algorithmia.client('simNjBefAAP0jc1S8UIniEnh7381')
algo = client.algo('StanfordNLP/NamedEntityRecognition/0.2.0')
print(algo.pipe(input))
