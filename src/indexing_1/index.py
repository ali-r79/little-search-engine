import operator

from crawling_1.crawler import Crawling
from collections import Counter


def indexing():
    db_address = input('enter the absolute path of where you want to locate pages: ')
    crawling = Crawling(db_address)
    crawling.crawl()
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
