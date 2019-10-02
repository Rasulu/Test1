import unittest
from selenium import webdriver


class Mytest(unittest.TestCase):
    @classmethod
    def setUp(self):

        Chrome_path = "C:\Auto_QA\chromedriver"
        self.driver = webdriver.Chrome(Chrome_path)
        
        self.driver.get("https://mail.google.com")

        print("Test")

    def test_work(self):
        self.driver.find_element_by_xpath("//*[@id=\"identifierId\"]").send_keys("Test")
        self.driver.implicitly_wait(30)

    def test_work1(self):
        self.driver.find_element_by_xpath("//*[@id=\"view_container\"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/button").click()
    @classmethod
    def teardown():
        driver.quit()

if __name__ == '__main__':
    unittest.main()