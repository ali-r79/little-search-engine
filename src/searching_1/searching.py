from indexing_1.index import Indexuing


def search(word):
    index = Indexuing.indexing()
    if word in index:
        return index[word].items()
    else:
        return {None: None}
