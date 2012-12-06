# -*- coding: utf-8 -*-

import unittest

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from skosprovider_oe.providers import (
    OnroerendErfgoedProvider
    )

class OnroerendErfgoedProviderTests(unittest.TestCase):
    def setUp(self):
        self.typologie = OnroerendErfgoedProvider(
            {'id': 'TYPOLOGIE'},
            'https://inventaris.onroerenderfgoed.be/thesaurus/typologie'
        )

    def tearDown(self):
        pass

    def test_get_vocabulary_id(self):
        self.assertEquals('TYPOLOGIE', self.typologie.get_vocabulary_id())

    def test_get_metadata(self):
        self.assertEquals({'id':'TYPOLOGIE', 'default_language': 'nl'}, 
                          self.typologie.get_metadata())

    def test_get_by_unexisting_id(self):
        self.assertFalse(self.typologie.get_by_id('RESTAFVAL'))

    def test_find(self):
        result = self.typologie.find({'label': 'kerken'})
        self.assertGreater(len(result),0)
        for c in result:
            self.assertIn('id',c)
            self.assertIn('label',c)

    def test_get_all(self):
        result = self.typologie.get_all()
        self.assertGreater(len(result),0)
        for c in result:
            self.assertIn('id',c)
            self.assertIn('label',c)

    def test_expand_concept(self):
        result = self.typologie.expand_concept(100)
        self.assertGreater(len(result),0)
