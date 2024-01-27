class PagingBook:
    def __init__(self):
        self.book_address = input('enter the absolute path of your book: ')

    def line_read(self):
        with open(self.book_address) as f:
            while True:
                read = f.readline()
                yield read

    def page_write(self, number_of_lines, number_of_pages):
        self.pages_address = input('enter the absolute path of where you want to locate your pages: ')
        self.write = self.line_read()
        for page_num in range(int(number_of_pages)):
            with open(f'{self.pages_address}/page_{page_num+1}.txt', 'w') as f:
                for num in range(int(number_of_lines)):
                    f.write(next(self.write))
                f.flush()
