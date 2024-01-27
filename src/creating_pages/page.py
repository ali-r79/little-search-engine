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
