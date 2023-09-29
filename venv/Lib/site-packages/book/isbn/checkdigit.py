# -*- coding: utf-8 -*-

from functools import wraps


def check_num_length(length):
    def _check_num_length(func):
        @wraps(func)
        def __check_num_length(num_str):
            _len = len(num_str)
            if _len != length:
                raise ValueError(_len)
            return func(num_str)
        return __check_num_length
    return _check_num_length


@check_num_length(10)
def check10(isbn10):
    u"""
    >>> check10(u'0306406152')
    True
    """
    check_sum = modulus11weight10to2(isbn10[:-1])
    return isbn10[-1] == check_sum


@check_num_length(13)
def check13(isbn13):
    u"""
    >>> check13(u'9780306406157')
    True
    """
    check_sum = modulus11weight3(isbn13[:-1])
    return isbn13[-1] == check_sum


@check_num_length(9)
def modulus11weight10to2(c9):
    u"""
    >>> modulus11weight10to2(u'030640615')
    u'2'
    """
    sum_ = 0
    for i in range(len(c9)):
        try:
            c = int(c9[i])
        except ValueError:
            return False
        sum_ += (10 - i) * c

    result = 11 - (sum_ % 11)
    return u'X' if result == 10 else unicode(result)


@check_num_length(12)
def modulus11weight3(c12):
    u"""
    >>> modulus11weight3(u'978030640615')
    u'7'
    """
    sum_ = 0
    for i in range(len(c12)):
        try:
            c = int(c12[i])
        except ValueError:
            return False
        weight = 3 if i % 2 else 1
        sum_ += weight * c

    result = 10 - (sum_ % 10)
    return u'0' if result == 10 else unicode(result)


@check_num_length(10)
def encode10to13(isbn10):
    u"""
    >>> encode10to13(u'0306406152')
    u'9780306406157'
    >>> encode10to13(u'487311361X')
    u'9784873113616'
    >>> encode10to13(u'4873114209')
    u'9784873114200'
    """
    prefix = u'978' + isbn10[:-1]
    check_digit = modulus11weight3(prefix)
    return prefix + check_digit


@check_num_length(13)
def encode13to10(isbn13):
    u"""
    >>> encode13to10(u'9780306406157')
    u'0306406152'
    >>> encode13to10(u'9784873113616')
    u'487311361X'
    >>> encode13to10(u'9784873114200')
    u'4873114209'
    """
    prefix = isbn13[3:-1]
    check_digit = modulus11weight10to2(prefix)
    return prefix + check_digit
