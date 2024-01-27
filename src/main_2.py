import operator
from pathlib import Path
from collections import Counter

class PagingBook:
    def __init__(self, book_address):
        self.book_address = book_address

    def line_read(self):
        with open(self.book_address) as f:
            while True:
                read = f.readline()
                yield read

    def page_write(self, number_of_lines, number_of_pages):
        self.write = self.line_read()
        for page_num in range(number_of_pages):
            with open(f'./db/page_{page_num}.txt', 'w') as f:
                for num in range(number_of_lines):
                    f.write(next(self.write))
                f.flush()

file_address = input('enter absolute path of your main file: ')
paging = PagingBook(file_address)
paging.page_write(number_of_lines=10, number_of_pages=100)

class Crawling:
    def __init__(self, address):
        self.address = address
        self.data = {}

    def crawl(self):
        for doc_path in Path(self.address).iterdir():
            if doc_path.suffix != '.txt':
                continue
            with open(doc_path) as f:
                self.data[doc_path.stem] = f.read()

db_address = input('enter db absolute path: ')
crawling = Crawling(db_address)
crawling.crawl()

# from collections import Counter
# from main import crawling


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

# from indexing_1.index import indexing

def search(word):
    index = indexing()
    if word in index:
        return index[word].items()
    else:
        return {None: None}

def running():
    while True:
        search_input = input('search(Q for quit): ')
        if search_input == 'Q':
            break
        search_tokens = search_input.split()
        final_dict = {}
        for word in search_tokens:
            final_dict[word] = search(word)
        final_list = list(zip(*final_dict.values()))
        for item in final_list:
            print(item)

running()
