from django.test import TestCase
from django.test.client import Client
from generator.consts import *
import json
import logging
# Create your tests here.

class SimpleTest(TestCase):
    def setUp(self):
    # Every test needs a client.
        self.client = Client()


    def test_fit_tops(self):
        for key in FIT_TOPS_SELECT:
            data = {'main_category': "メンズ",
            'sub_category': 'トップス',
            'sub_category_2': '',
            'fit': FIT_TOPS_SELECT[key],
            'design': 'メンズ',
            'response': 'メンズ',
            'neck': 'メンズ',
            'coller': 'メンズ',
            'zipbutton': 'メンズ',
            'length': 'メンズ',
            'skirt_length': 'メンズ',
            'leg': 'メンズ',
            'effect': 'メンズ',}
            response = self.client.post('/generator/index', data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            # レスポンスが 200 OK であるか調べます。
            self.failUnlessEqual(response.status_code, 200)
            self.assertTrue(response.content.decode('utf-8') != "")
            self.assertIn(response.content.decode('utf-8'), FIT_TOPS_DESCRIPTION[key])
            logging.debug(response.content.decode('utf-8'))
    def test_fit_tops_women(self):
        for key in FIT_TOPS_SELECT:
            data = {'main_category': "レディース",
            'sub_category': 'トップス',
            'sub_category_2': '',
            'fit': FIT_TOPS_SELECT[key],
            'design': '',
            'response': '',
            'neck': '',
            'coller': '',
            'zipbutton': '',
            'length': '',
            'skirt_length': '',
            'leg': '',
            'effect': '',}
            response = self.client.post('/generator/index', data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            # レスポンスが 200 OK であるか調べます。
            self.failUnlessEqual(response.status_code, 200)
            self.assertTrue(response.content.decode('utf-8') != "")
            self.assertIn(response.content.decode('utf-8'), FIT_TOPS_DESCRIPTION_WOMEN[key])
            logging.debug(response.content.decode('utf-8'))

    def test_fit_bottoms(self):
        for key in FIT_BOTTOMS_SELECT:
            data = {'main_category': "メンズ",
            'sub_category': 'パンツ',
            'sub_category_2': '',
            'fit': FIT_BOTTOMS_SELECT[key],
            'design': '',
            'response': '',
            'neck': '',
            'coller': '',
            'zipbutton': '',
            'length': '',
            'skirt_length': '',
            'leg': '',
            'effect': '',}
            response = self.client.post('/generator/index', data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            # レスポンスが 200 OK であるか調べます。
            self.failUnlessEqual(response.status_code, 200)
            self.assertTrue(response.content.decode('utf-8') != "")
            self.assertIn(response.content.decode('utf-8'), FIT_BOTTOMS_DESCRIPTION[key])
            logging.debug(response.content.decode('utf-8'))


    def test_fit_bottoms_women(self):
        for key in FIT_BOTTOMS_SELECT:
            data = {'main_category': "レディース",
            'sub_category': 'パンツ',
            'sub_category_2': '',
            'fit': FIT_BOTTOMS_SELECT[key],
            'design': '',
            'response': '',
            'neck': '',
            'coller': '',
            'zipbutton': '',
            'length': '',
            'skirt_length': '',
            'leg': '',
            'effect': '',}
            response = self.client.post('/generator/index', data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
            # レスポンスが 200 OK であるか調べます。
            self.failUnlessEqual(response.status_code, 200)
            self.assertTrue(response.content.decode('utf-8') != "")
            self.assertIn(response.content.decode('utf-8'), FIT_BOTTOMS_DESCRIPTION_WOMEN[key])
            logging.debug(response.content.decode('utf-8'))



