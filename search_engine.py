'''Mini Search engine dont read every page when you search. 
They build an INDEX in advance and then use math to rank it.
Three rankers battle it out.
1)COUNT - how many time do the query words appear
2)TF - what fraction of the article is the query word
3)TF IDF - like TF rare words matter more than common ones.


'''
import math
from collections import Counter,defaultdict
from articles import ARTICLES

def tokenize(text):
    chars = [ch if ch.isalnum() else " " for ch in text.lower()]
    return "".join(chars).split()

def build_INDEX(articles):
    index = defaultdict(dict)
    lenghts = {}
    for doc_id,(title,text) in enumerate(articles):
        words = tokenize(title+" "+text)
        lenghts[]

