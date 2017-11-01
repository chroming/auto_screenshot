# -*- coding:utf-8 -*-

import time
import os
import gc

from src.pdf import Pdf
from src.screenshot import screenshot
from src.actions import click


def douban_pdf(path='douban_demo.pdf', page_num=1):
    pdf = Pdf(path)
    shot = None
    while page_num:
        time.sleep(3)
        shot = screenshot('tmp.pdf', (614, 0, 1274, 1070))
        pdf.add_page_from_pdf(shot)
        click()
        page_num -= 1
        pdf.save_pdf()
    del shot
    del pdf
    gc.collect(2)
    os.remove('tmp.pdf')


if __name__ == '__main__':
    douban_pdf('douban_demo.pdf', 2)

