def search(word, index):
    # print(index)
    if word in index:
        return index[word].items()
    else:
        return {None: None}
