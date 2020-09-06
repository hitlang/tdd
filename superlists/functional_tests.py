#测试驱动开发
from time import sleep

from selenium import  webdriver
import unittest
#
# browser = webdriver.Firefox()
#
#
# browser.get("http://localhost:8000") # 网址
#
# sleep(3)
#
# try:
#     assert  'to-do' in browser.title # 不执行成功，下一句无法执行
#
# finally:
#     browser.close()

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get("http://localhost:8000")

        self.assertIn("Django" , self.driver.title)

        # self.fail("finish the test") # 总会失败
        pass


    # 即使测试执行失败，也会执行，特列：setup方法抛出异常. 此方法不执行.
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

