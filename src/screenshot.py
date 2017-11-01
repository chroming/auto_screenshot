# -*- coding:utf-8 -*-

from PIL import ImageGrab


def screenshot(path='demo.pdf', bbox=(0, 0, 100, 100)):
    """
    Take a screenshot with size and save it to file.
    :param path: file path
    :param bbox: locate and size.
    """
    img = ImageGrab.grab(bbox)
    img.save(path)
    return path


if __name__ == '__main__':
    screenshot()
