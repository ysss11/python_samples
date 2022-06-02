from unittest import TestCase

from fortune import fortune


class Testfortune(TestCase):
    def test_OK_001(self):
        """ 大吉の確認 """
        self.assertEqual("【大吉】です。", fortune(10))

    def test_OK_002(self):
        """ 中吉の確認 """
        self.assertEqual("【中吉】です。", fortune(9))
        self.assertEqual("【中吉】です。", fortune(8))
        self.assertEqual("【中吉】です。", fortune(7))
        self.assertEqual("【中吉】です。", fortune(6))

    def test_OK_003(self):
        """ 吉の確認 """
        self.assertEqual("【吉】です。", fortune(5))
        self.assertEqual("【吉】です。", fortune(4))
        self.assertEqual("【吉】です。", fortune(3))

    def test_OK_004(self):
        """ 凶の確認 """
        self.assertEqual("【凶】です。", fortune(2))
        self.assertEqual("【凶】です。", fortune(1))

    def test_OK_005(self):
        """ 大凶の確認 """
        self.assertEqual("【大凶】です。", fortune(0))
