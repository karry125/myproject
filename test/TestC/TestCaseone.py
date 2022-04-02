#!/usr/bin/python3

import unittest

import HTMLTestRunner

class MyTest(unittest.TestCase):
     def tearDown(self):
          print("1")
     def setUp(self):
          print("2")
     def testa(self):
          self.assertEqual(1, 1)
     def testb(self):
          self.assertEqual(2, 2)
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTest("testa"))
    suite.addTest(MyTest("testb"))
    fp = open('F:\\result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
    runner.run(suite)
    fp.close()