# -*- coding: utf-8 -*-
import unittest
from parse_ikon import *

""" Utilities """
def collect_artists_contains(df, sub):
    for index, row in df.iterrows():
        artists = row['artists']
        for artist in artists:
            if sub in artist:
                print(index, row)
                yield artist
                
""" TESTS """
class TestParsing(unittest.TestCase):
    def test_results(self):
        with open("./tmp/IkOn2018.05.14.Mon-2018.05.20.Sun.html", encoding="utf-8") as file:
            page = file.read()
            data = parse_page(page)
            self.assertGreater(len(data), 0)
            self.assertEqual(len(data), 24)
    
    def test_no_results(self):
        with open("./tmp/IkOn2018.12.24.Mon-2018.12.30.Sun.html", encoding="utf-8") as file:
            page = file.read()
            data = parse_page(page)
            self.assertEqual(len(data), 0)
            
if __name__ == "__main__":
    unittest.main()
    
    for a in collect_artists_contains(df, "&&"):
        print(a)


