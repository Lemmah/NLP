"""
This algorithm takes an English sentence and assigns sentiment ratings of "positive", "negative" and "neutral".
"""
# More reading: https://algorithmia.com/algorithms/nlp/SocialSentimentAnalysis

import Algorithmia

input = {
    "sentence": "This old product sucks! But after the update it works like a charm!"

}
client = Algorithmia.client('simNjBefAAP0jc1S8UIniEnh7381')
algo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
output = algo.pipe(input)
print(output)
