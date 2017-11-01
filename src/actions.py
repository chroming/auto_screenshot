# -*- coding:utf-8 -*-

import pyautogui as pg


def click(x=None, y=None):
    pg.click(x, y)


def scroll(n=-10):
    pg.scroll(n)


def pagedown():
    pg.press("pagedown")


def pageup():
    pg.press("pageup")