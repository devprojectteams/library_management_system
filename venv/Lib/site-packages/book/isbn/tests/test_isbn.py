# -*- coding: utf-8 -*-

import unittest
from book import isbn


class TestISBN(unittest.TestCase):

    def setUp(self):
        pass

    def test_check10(self):
        goodcase = (
            u'0306406152',
            )
        for isbn10 in goodcase:
            self.assertTrue(isbn.check10(isbn10))

        badcase = (
            u'1234567890',
            )
        for isbn10 in badcase:
            self.assertFalse(isbn.check10(isbn10))

        errorcase = (
            u'',
            #1, #TODO: Number
            u'123456789',
            u'12345678901',
            )
        for invalid_isbn in errorcase:
            try:
                isbn.check10(invalid_isbn)
                self.fail()
            except ValueError:
                pass

    def test_check13(self):
        goodcase = (
            u'9780306406157',
            )
        for isbn13 in goodcase:
            self.assertTrue(isbn.check13(isbn13))

        badcase = (
            )

    def test_modulus11weight10to2(self):
        goodcase = (
            (u'030640615', u'2',),
            )
        for (isbn9, digit) in goodcase:
            self.assertEqual(isbn.modulus11weight10to2(isbn9), digit)

    def test_modulus11weight3(self):
        goodcase = (
            (u'978030640615', u'7',),
            )
        for (isbn10, digit) in goodcase:
            self.assertEqual(isbn.modulus11weight3(isbn10), digit)

    def test_encode10to13(self):
        goodcase = (
            (u'0306406152', u'9780306406157'),
            (u'487311361X', u'9784873113616'),
            (u'4873114209', u'9784873114200'),
            )
        for (isbn10, isbn13) in goodcase:
            self.assertEqual(isbn.encode10to13(isbn10), isbn13)

    def test_encode13to10(self):
        goodcase = (
            (u'0306406152', u'9780306406157'),
            (u'487311361X', u'9784873113616'),
            (u'4873114209', u'9784873114200'),
            )
        for (isbn10, isbn13) in goodcase:
            self.assertEqual(isbn.encode13to10(isbn13), isbn10)


if __name__ == '__main__':
    unittest.main()
