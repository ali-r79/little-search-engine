import operator
from creating_pages.page import PagingBook
from crawling_1.crawler import Crawling
from collections import Counter



def index_words():
    paging = PagingBook()
    paging.page_write()
    crl = Crawling(paging.pages_address)
    crl.crawl()
    index = {}
    for doc_name, doc_content in crl.data.items():
        words = doc_content.split()

        for word in words:
            if word in index:
                index[word].append(doc_name)
            else:
                index[word] = [doc_name]

    for word in index:
        index[word] = dict(sorted(Counter(index[word]).items(),\
            key=operator.itemgetter(1), reverse=True))
    # print(index)
    return index
