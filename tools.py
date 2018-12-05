# -*- coding: utf-8 -*-
"""
Created on Sat Aug 06 17:24:34 2016

@author: Sargas
"""
import sys
import time
from datetime import datetime


def trace(func):
  “”“
  用来显示当前运行函数所在的文件名，行号，函数名，运行耗时。
  ”“”
    def _trace(*args, **kwargs):
        frame = sys._getframe(1)
        s = "{0}->{1}->{2}".format(
            frame.f_code.co_filename, frame.f_lineno, func.__name__
        )
        print("running:", s)
        begin = datetime.now()
        ret = func(*args, **kwargs)
        print("time(ms):", (datetime.now() - begin).microseconds)
        return ret

    return _trace
