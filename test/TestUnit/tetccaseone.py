import  TestUnit.add as sum
import  unittest
from HTMLTestRunner import HTMLTestRunner
import  time
class Testadd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,sum.add(1,2))
        self.assertNotEqual(3,sum.add(2,2))
        print("add")
    def test_minus(self):
        self.assertEqual(3,sum.minus(5,2))
        self.assertNotEqual(3,sum.minus(2,2))
        print("minus")


'''
#运行测试用例
if __name__ == '__mian__':
    #unittest.main()
    test = unittest.TestSuite()
    test.addTest(Testadd("test_add"))
    test.addTest(Testadd("test_minus"))
    runner = unittest.TextTestRunner()
    runner.run(test)
'''

#print("o8")
if __name__ == '__main__':
    print("q")
    testdir = "./"
    discover = unittest.defaultTestLoader.discover(testdir, pattern='test*.py')
   # unittest.main()
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    filename = 'F:\\p.html'

    fp = open(filename, "wb+")
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title=u"xxx接口测试报告",
                            description=u"测试用例执行情况：")
    # 运行测试
    runner.run(discover)
  #  fp.close()  # 关闭报告文件
