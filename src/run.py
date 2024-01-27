from searching_1.searching import search
from indexing_1.index import index_words


indexx = index_words()
while True:
    search_input = input('search(Q for quit): ')
    if search_input == 'Q':
        break
    search_tokens = search_input.split()
    final_dict = {}
    for word in search_tokens:
        final_dict[word] = search(word, indexx)
    final_list = list(zip(*final_dict.values()))
    for item in final_list:
        print(item)
        print()
