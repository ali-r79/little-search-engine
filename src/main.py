from creating_pages.page import PagingBook
from run_file_1.run import running
from indexing_1.index import indexing

file_address = input('enter the absolute path of your book: ')
paging = PagingBook(file_address)
paging.page_write(number_of_lines=10, number_of_pages=100)

indexing()
running()
