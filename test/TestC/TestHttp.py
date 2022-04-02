#!/usr/bin/python3

import  requests
from functools import partial
import json
import unittest
'''
url = 'https://api.douban.com/v2/movie/search'
params=dict(q=u'刘德华')
r = requests.get(url, params=params)
print('Search Params:\n', json.dumps(params, ensure_ascii=False))
print('Search Response:\n', json.dumps(r.json(), ensure_ascii=False, indent=4))
'''



class Testh(unittest.TestCase):
     def search(self,params):
         print("ser1")
         url = 'https://api.douban.com/v2/movie/search'
         r = requests.get(url , params = params)
         print( 'Search Params:\n', json.dumps(params, ensure_ascii=False))
         print('Search Response:\n', json.dumps(r.json(), ensure_ascii=False, indent=4))

     def test_q(self):
         url = 'https://api.douban.com/v2/movie/search'
         qs = [u'白夜追凶', u'大话西游', u'周星驰', u'张艺谋', u'周星驰,吴孟达', u'张艺谋,巩俐', u'周星驰,西游', u'白夜追凶,潘粤明']
         list = ["白夜追凶","大话西游"]
        # params = {"q":"白夜追凶"}
        # self.search(params)
       #  print("ser")

         for q in list:
             params = dict(q=q)
             print(q)
             print(params)
             self.search(params)
            # r = requests.get(url, params=params)
             f = partial(self.search,params)
             #f.description = json.dumps(params, ensure_ascii=False)
#             #f.description = json.dumps(params, ensure_ascii=False)
             # yield (f,)
             #  print('Search Response:\n', json.dumps(r.json(), ensure_ascii=False, indent=4))









#a = Testh()
#a.test_q( )
if __name__ == "__main__":
    unittest.main()#运行所有的测试用例
    print("1ser")


