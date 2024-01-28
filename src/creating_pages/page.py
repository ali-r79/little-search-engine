import os
from pathlib import Path

class PagingBook:
    def __init__(self):
        self.book_address = input('enter the absolute path of your book: ')

    def line_read(self):
        with open(self.book_address) as f:
            while True:
                read = f.readline()
                yield read

    def page_write(self):
        self.pages_address = input('enter the absolute path of where you want to locate your pages: ')
        dir = Path(self.pages_address)
        if not dir.is_dir():
            os.mkdir(dir)
            print('directory you have entered was not exist but we made it!')

        self.number_of_lines = input('number of lines in each page: ')
        self.number_of_pages = input('number of pages: ')

        self.write = self.line_read()
        for page_num in range(int(self.number_of_pages)):
            with open(f'{self.pages_address}/page_{page_num+1}.txt', 'w') as f:
                for num in range(int(self.number_of_lines)):
                    f.write(next(self.write))
                f.flush()
