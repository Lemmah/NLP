# Parsey McParseface
# Google's extension of syntaxnet
# https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html
# https://algorithmia.com/algorithms/deeplearning/Parsey

import Algorithmia

input = {
    "src": "James is a brilliant kid.",
    "format": "conll",
    "language": "english"
}
client = Algorithmia.client('simNjBefAAP0jc1S8UIniEnh7381')
algo = client.algo('deeplearning/Parsey/1.0.2')
print(algo.pipe(input))
