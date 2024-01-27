from pathlib import Path


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
