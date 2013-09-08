# -*- coding: utf-8 -*-

import sys
import unittest2

from unipath import Path
sys.path.append(Path(__file__).ancestor(2))

from scrapy.selector import HtmlXPathSelector
from scrapy.http.response.html import HtmlResponse

from localgouv.account_network import city_account
from localgouv.account_parsing import CityParser, EPCIParser

def get_response(filepath, encoding='utf-8'):
    body = open(filepath, 'r').read()
    response = HtmlResponse('test', encoding=encoding)
    response.body = body
    return response

class CommuneFinanceParsingTestCase(unittest2.TestCase):
    def setUp(self):
        self.response = get_response('data/commune_2012_account.html')

    def test_parsing(self):
        parser = CityParser('', 2012)
        data = parser.parse(self.response)
        self.assertEqual(data['population'], 394)
        # test data parsed from first table
        self.assertEqual(data['operating_revenues'], 210000.)
        self.assertEqual(data['localtax'], 114000.)
        self.assertEqual(data['operating_costs'], 214000.)

        # test data parsed from second table
        self.assertEqual(data['home_tax']['value'], 47000.)
        self.assertEqual(data['home_tax']['basis'], 562000.)
        self.assertAlmostEqual(data['home_tax']['rate'], 0.0839)

class CommuneFinanceParsingTestCase(unittest2.TestCase):
    def setUp(self):
        self.response = get_response('data/epci_2012_account.html',
                                     encoding='windows-1252')

    def test_parsing(self):
        parser = EPCIParser('', 2012)
        data = parser.parse(self.response)
        self.assertEqual(data['population'], 2701)
        # test data parsed from first table
        self.assertEqual(data['operating_revenues'], 1879000.)
        self.assertEqual(data['localtax'], 395000.)
        self.assertEqual(data['operating_costs'], 1742000.)

        # test data parsed from second table
        self.assertEqual(data['home_tax']['value'], 199000.)
        self.assertEqual(data['home_tax']['basis'], 8489000.)
        self.assertAlmostEqual(data['home_tax']['rate'], 0.023400)
        self.assertEqual(data['home_tax']['cuts_on_deliberation'], 33000)

if __name__ == '__main__':
    unittest2.main()
