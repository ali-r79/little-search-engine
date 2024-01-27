from creating_pages.page import PagingBook
from crawling_1.crawler import Crawling
from run_file_1.run import running


file_address = input('enter the absolute path of your book: ')
paging = PagingBook(file_address)
paging.page_write(number_of_lines=10, number_of_pages=100)
db_address = input('enter the absolute path of where you want to locate pages: ')
crawling = Crawling(db_address)
crawling.crawl()
running()
