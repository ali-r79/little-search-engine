from indexing_1.index import indexing


def search(word):
    index = indexing()
    if word in index:
        return index[word].items()
    else:
        return {None: None}
