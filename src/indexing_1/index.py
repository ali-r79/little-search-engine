import operator

from collections import Counter
from main import crawling


def indexing():
    index = {}
    for doc_name, doc_content in crawling.data.items():
        words = doc_content.split()

        for word in words:
            if word in index:
                index[word].append(doc_name)
            else:
                index[word] = [doc_name]

    for word in index:
        index[word] = dict(sorted(Counter(index[word]).items(), key=operator.itemgetter(1), reverse=True))
    return index
