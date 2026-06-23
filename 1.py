!pip install gensim
import gensim.downloader as api
m = api.load("glove-wiki-gigaword-50")
print(m.most_similar("king"))
print(m.similarity("king","queen"))
