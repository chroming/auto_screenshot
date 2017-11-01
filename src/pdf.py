# -*- coding:utf-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader


class Pdf(object):
    def __init__(self, path):
        self.path = path
        self.writer = PdfFileWriter()

    def add_page_from_pdf(self, path):
        """Add a pdf to the final pdf"""
        reader = PdfFileReader(open(path, "rb"))
        self.writer.appendPagesFromReader(reader)

    def save_pdf(self):
        """save the writer to a pdf file with name 'name_new.pdf' """
        with open(self.path, 'wb') as out:
            self.writer.write(out)
        return self.path


if __name__ == '__main__':
    p = Pdf("new_demo.pdf")
    p.add_page_from_pdf("demo.pdf")
    p.save_pdf()