import  TestUnit.add as sum
import  unittest
import  HTMLTestRunner


class Testadd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,sum.add(1,2))
        self.assertNotEqual(3,sum.add(2,2))
        print("这是TestA")
    def test_minus(self):
        self.assertEqual(3,sum.minus(5,2))
        self.assertNotEqual(3,sum.minus(2,2))
if __name__ == '__main__':
    testdir = "./"
    discover = unittest.defaultTestLoader.discover(testdir, pattern='test*.py')
    #确定生成报告的路径
    filePath = "F:\\o.html"
    fp = open(filePath,'wb')

    #生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='xxx接口测试报告t',description='This  is Python  Report')
    runner.run(discover)